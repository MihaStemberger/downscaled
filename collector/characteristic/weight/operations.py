import asyncio

from bleak import BleakClient, BleakGATTCharacteristic, BleakError

from model.scale_response import ScaleResponse

# Weight characteristics
UUID = "00002a9d-0000-1000-8000-00805f9b34fb"


async def notify(client: BleakClient, scale_response: ScaleResponse, timeout: int):
    async def callback(sender: BleakGATTCharacteristic, data: bytearray):
        scale_response.weight = int.from_bytes(data[1:3], byteorder='little', signed=False) * 0.005
        scale_response.bmi = int.from_bytes(data[11:13], byteorder='little', signed=False) * 0.1
        scale_response.height = int.from_bytes(data[13:15], byteorder='little', signed=False) * 0.1
        scale_response.year = int.from_bytes(data[3:5], byteorder='little', signed=False)
        scale_response.month = int.from_bytes(data[5:6], byteorder='little', signed=False)
        scale_response.day = int.from_bytes(data[6:7], byteorder='little', signed=False)
        scale_response.hours = int.from_bytes(data[7:8], byteorder='little', signed=False)
        scale_response.minutes = int.from_bytes(data[8:9], byteorder='little', signed=False)
        scale_response.seconds = int.from_bytes(data[9:10], byteorder='little', signed=False)
        data_received_event.set()

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
