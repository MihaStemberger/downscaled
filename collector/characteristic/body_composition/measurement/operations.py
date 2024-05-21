import asyncio

from bleak import BleakClient, BleakGATTCharacteristic, BleakError

from model.scale_response import ScaleResponse

# Body Composition Measurement
UUID = '00002a9c-0000-1000-8000-00805f9b34fb'


async def notify(client: BleakClient, scale_response: ScaleResponse, timeout: int):
    async def callback(sender: BleakGATTCharacteristic, data: bytearray):
        scale_response.body_fat_percentage = int.from_bytes(data[2:4], byteorder='little', signed=False) * 0.1
        scale_response.basal_metabolism = int.from_bytes(data[4:6], byteorder='little', signed=False)
        scale_response.muscle_percentage = int.from_bytes(data[6:8], byteorder='little', signed=False) * 0.01
        scale_response.soft_lean_mass = int.from_bytes(data[8:10], byteorder='little', signed=False) * 0.005
        scale_response.body_water_mass = int.from_bytes(data[10:12], byteorder='little', signed=False) * 0.005
        scale_response.impedance = int.from_bytes(data[10:12], byteorder='little', signed=False)
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
