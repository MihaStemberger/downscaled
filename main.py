import asyncio
import csv
from pathlib import Path

from bleak import BleakClient, BleakGATTCharacteristic

WEIGHT_UUID = "00002a9d-0000-1000-8000-00805f9b34fb"
BODY_COMP_MEASUREMENT = '00002a9c-0000-1000-8000-00805f9b34fb'

# -- Characteristics for User Control Point
# -- UUID: 00002a9f-0000-1000-8000-00805f9b34fb
UCP_UUID = '00002a9f-0000-1000-8000-00805f9b34fb'


class CSVInput:
    def __init__(self):
        self._weight = None
        self._bmi = None
        self._height = None
        self._year = None
        self._month = None
        self._day = None
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._body_fat_percentage = None
        self._basal_metabolism = None
        self._muscle_percentage = None
        self._soft_lean_mass = None
        self._body_water_mass = None
        self._impedance = None

    @property
    def weight(self):
        return self._weight

    @property
    def bmi(self):
        return self._bmi

    @property
    def height(self):
        return self._height

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    @property
    def body_fat_percentage(self):
        return self._body_fat_percentage

    @property
    def basal_metabolism(self):
        return self._basal_metabolism

    @property
    def muscle_percentage(self):
        return self._muscle_percentage

    @property
    def soft_lean_mass(self):
        return self._soft_lean_mass

    @property
    def body_water_mass(self):
        return self._body_water_mass

    @property
    def impedance(self):
        return self._impedance

    @weight.setter
    def weight(self, value):
        # You can add validation logic here if needed
        self._weight = value

    @bmi.setter
    def bmi(self, value):
        # You can add validation logic here if needed
        self._bmi = value

    @height.setter
    def height(self, value):
        # You can add validation logic here if needed
        self._height = value

    @year.setter
    def year(self, value):
        # You can add validation logic here if needed
        self._year = value

    @month.setter
    def month(self, value):
        # You can add validation logic here if needed
        self._month = value

    @day.setter
    def day(self, value):
        # You can add validation logic here if needed
        self._day = value

    @hours.setter
    def hours(self, value):
        # You can add validation logic here if needed
        self._hours = value

    @minutes.setter
    def minutes(self, value):
        # You can add validation logic here if needed
        self._minutes = value

    @seconds.setter
    def seconds(self, value):
        # You can add validation logic here if needed
        self._seconds = value

    @body_fat_percentage.setter
    def body_fat_percentage(self, value):
        # You can add validation logic here if needed
        self._body_fat_percentage = value

    @basal_metabolism.setter
    def basal_metabolism(self, value):
        # You can add validation logic here if needed
        self._basal_metabolism = value

    @muscle_percentage.setter
    def muscle_percentage(self, value):
        # You can add validation logic here if needed
        self._muscle_percentage = value

    @soft_lean_mass.setter
    def soft_lean_mass(self, value):
        # You can add validation logic here if needed
        self._soft_lean_mass = value

    @body_water_mass.setter
    def body_water_mass(self, value):
        # You can add validation logic here if needed
        self._body_water_mass = value

    @impedance.setter
    def impedance(self, value):
        # You can add validation logic here if needed
        self._impedance = value


def callback(sender: BleakGATTCharacteristic, data: bytearray):
    print(f"{sender}: {data}")


async def readUserData(client):
    USER_INDEX = '00002a9a-0000-1000-8000-00805f9b34fb'
    GENDER = '00002a8c-0000-1000-8000-00805f9b34fb'
    DB_INCREMENT = '00002a99-0000-1000-8000-00805f9b34fb'
    BIRTH = '00002a85-0000-1000-8000-00805f9b34fb'
    ui = await client.read_gatt_char(USER_INDEX)
    g = await client.read_gatt_char(GENDER)
    inc = await client.read_gatt_char(DB_INCREMENT)
    bir = await client.read_gatt_char(BIRTH)

    userindex = int.from_bytes(ui)

    print(f"User data is {ui}, {g}, {inc}, {bir}")


async def main(address):
    print(f"Starting scale script")
    csv_file_path = 'measurements.csv'
    collector = CSVInput()

    def weight_characteristics_callback(sender: BleakGATTCharacteristic, data: bytearray):
        print(f"Handling weight characteristics response: {sender.uuid}")
        collector.weight = int.from_bytes(data[1:3], byteorder='little', signed=False) * 0.005
        collector.bmi = int.from_bytes(data[11:13], byteorder='little', signed=False) * 0.1
        collector.height = int.from_bytes(data[13:15], byteorder='little', signed=False) * 0.1
        collector.year = int.from_bytes(data[3:5], byteorder='little', signed=False)
        collector.month = int.from_bytes(data[5:6], byteorder='little', signed=False)
        collector.day = int.from_bytes(data[6:7], byteorder='little', signed=False)
        collector.hours = int.from_bytes(data[7:8], byteorder='little', signed=False)
        collector.minutes = int.from_bytes(data[8:9], byteorder='little', signed=False)
        collector.seconds = int.from_bytes(data[9:10], byteorder='little', signed=False)

    def body_composition_measurement(sender: BleakGATTCharacteristic, data: bytearray):
        print(f"Handling body composition measurement: {sender.uuid}")
        collector.body_fat_percentage = int.from_bytes(data[2:4], byteorder='little', signed=False) * 0.1
        collector.basal_metabolism = int.from_bytes(data[4:6], byteorder='little', signed=False)
        collector.muscle_percentage = int.from_bytes(data[6:8], byteorder='little', signed=False) * 0.01
        collector.soft_lean_mass = int.from_bytes(data[8:10], byteorder='little', signed=False) * 0.005
        collector.body_water_mass = int.from_bytes(data[10:12], byteorder='little', signed=False) * 0.005
        collector.impedance = int.from_bytes(data[10:12], byteorder='little', signed=False)

    client = BleakClient(address)
    try:
        if not client.is_connected:
            await client.connect()

        print(f"Connected to {address}")

        await client.pair()

        # for service in client.services:
        #     print(f"Service: {service.uuid}")
        #     print(f"Description: {service.description}")
        #     for characteristic in service.characteristics:
        #         print(f"-- Characteristics for {characteristic.description}")
        #         print(f"-- UUID: {characteristic.uuid}")
        #         print(f"-- Properties: {characteristic.properties}")

        int_parameter = int(PIN)
        asBytes = int_parameter.to_bytes(2, byteorder='little')
        await client.write_gatt_char(UCP_UUID, int(2).to_bytes(1) + int(1).to_bytes(1) + asBytes, response=True)
        await asyncio.sleep(5)
        await client.start_notify(UCP_UUID, callback)
        await asyncio.sleep(5)
        await client.start_notify(WEIGHT_UUID, weight_characteristics_callback)
        await client.start_notify(BODY_COMP_MEASUREMENT, body_composition_measurement)
        await asyncio.sleep(30)

        await readUserData(client)

        print(f"stop_notify all")
        await client.stop_notify(WEIGHT_UUID)
        await client.stop_notify(UCP_UUID)
    except Exception as e:
        print(e)
    finally:
        if collector.weight is None:
            print(f"Nothing to write")
            return
        if Path(csv_file_path).exists():
            print(f"The file '{csv_file_path}' exists.")
            with open(csv_file_path, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                # Write the data
                csv_writer.writerow([collector.weight,
                                     collector.bmi,
                                     collector.height,
                                     collector.year,
                                     collector.month,
                                     collector.day,
                                     collector.hours,
                                     collector.minutes,
                                     collector.seconds,
                                     collector.body_fat_percentage,
                                     collector.basal_metabolism,
                                     collector.muscle_percentage,
                                     collector.soft_lean_mass,
                                     collector.body_water_mass,
                                     collector.impedance
                                     ])
        else:
            print(f"The file '{csv_file_path}' does not exist.")
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                # Write the header
                csv_writer.writerow(['weight', 'bmi', 'height', 'year', 'month', 'day', 'hours', 'minutes', 'seconds',
                                     'body_fat_percentage', 'basal_metabolism', 'muscle_percentage', 'soft_lean_mass',
                                     'body_water_mass', 'impedance'])

                # Write the data
                csv_writer.writerow([collector.weight,
                                     collector.bmi,
                                     collector.height,
                                     collector.year,
                                     collector.month,
                                     collector.day,
                                     collector.hours,
                                     collector.minutes,
                                     collector.seconds,
                                     collector.body_fat_percentage,
                                     collector.basal_metabolism,
                                     collector.muscle_percentage,
                                     collector.soft_lean_mass,
                                     collector.body_water_mass,
                                     collector.impedance
                                     ])

        await client.unpair()




asyncio.run(main(ADDRESS))
