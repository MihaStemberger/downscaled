import asyncio
import sys

from bleak import BleakClient

from collector.characteristic.body_composition.measurement.collector import collect_body_composition_measurement
from collector.characteristic.user_control_point.collector import select_user
from collector.characteristic.weight.collector import collect_weight
from model.scale_response import ScaleResponse
from persist.database import persist_to_database
from persist.file import persist_to_file


async def read_user_data(client):
    USER_INDEX = '00002a9a-0000-1000-8000-00805f9b34fb'
    GENDER = '00002a8c-0000-1000-8000-00805f9b34fb'
    DB_INCREMENT = '00002a99-0000-1000-8000-00805f9b34fb'
    BIRTH = '00002a85-0000-1000-8000-00805f9b34fb'
    ui = await client.read_gatt_char(USER_INDEX)
    g = await client.read_gatt_char(GENDER)
    inc = await client.read_gatt_char(DB_INCREMENT)
    bir = await client.read_gatt_char(BIRTH)

    user_index = int.from_bytes(ui)

    print(f"Selected user index: {user_index}")


async def main(device_address, user_pin):
    print(f"Starting scale script")
    client = BleakClient(device_address)
    scale_response = ScaleResponse()
    try:
        if not client.is_connected:
            await client.connect()

        print(f"Connected to {device_address}")

        await client.pair()

        print("Paired")

        # await display_services(client)

        await select_user(client, int(user_pin))

        await read_user_data(client)

        print("Reading scale data")

        try:
            await asyncio.gather(
                collect_body_composition_measurement(client, scale_response),
                collect_weight(client, scale_response)
            )
        except Exception as exception:
            raise exception

        if scale_response.weight is None:
            print(f"Nothing to write")
            return

        try:
            persist_to_file(scale_response)
        except Exception as file_persist_exception:
            print("Unable to persist scale data to the file")
            print(file_persist_exception)

        try:
            persist_to_database(scale_response)
        except Exception as database_persist_exception:
            print("Unable to persist scale data to the database")
            print(database_persist_exception)

    except Exception as exception:
        print(exception)
    finally:
        await client.unpair()


def display_services(client):
    for service in client.services:
        print(f"Service: {service.uuid}")
        print(f"Description: {service.description}")
        for characteristic in service.characteristic:
            print(f"-- Characteristics for {characteristic.description}")
            print(f"-- UUID: {characteristic.uuid}")
            print(f"-- Properties: {characteristic.properties}")


asyncio.run(main(sys.argv[1], sys.argv[2]))
