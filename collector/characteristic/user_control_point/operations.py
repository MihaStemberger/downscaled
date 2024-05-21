import asyncio

from bleak import BleakGATTCharacteristic, BleakClient, BleakError

#  User Control Point characteristic
UUID = '00002a9f-0000-1000-8000-00805f9b34fb'


async def select_user_on_scale(client: BleakClient, pin, timeout: int):
    async def callback(sender: BleakGATTCharacteristic, data: bytearray):
        data_received_event.set()

    as_bytes = pin.to_bytes(2, byteorder='little')
    await client.write_gatt_char(UUID, int(2).to_bytes(1) + int(1).to_bytes(1) + as_bytes, response=True)

    data_received_event = asyncio.Event()

    try:
        await client.start_notify(UUID, callback)
        try:
            # Wait for either the data received event or the timeout
            await asyncio.wait_for(data_received_event.wait(), timeout)
            if data_received_event.is_set():
                print(f"Data received from {UUID}")
            else:
                print(f"Timeout waiting for data from {UUID}")
                raise asyncio.TimeoutError(f"Timeout waiting for data from {UUID}")

        except asyncio.TimeoutError as timeout_exception:
            print(f"Timeout waiting for data from {UUID}")
            raise timeout_exception
    except BleakError as e:
        print(f"Failed to start notify for {UUID}: {e}")
        raise e
    finally:
        await client.stop_notify(UUID)
