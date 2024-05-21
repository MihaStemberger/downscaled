import csv
from pathlib import Path

from model.scale_response import ScaleResponse


def persist_to_file(scale_response: ScaleResponse):
    csv_file_path = 'measurements.csv'

    if Path(csv_file_path).exists():
        print(f"The file '{csv_file_path}' exists.")
        with open(csv_file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write the data
            csv_writer.writerow([scale_response.weight,
                                 scale_response.bmi,
                                 scale_response.height,
                                 scale_response.year,
                                 scale_response.month,
                                 scale_response.day,
                                 scale_response.hours,
                                 scale_response.minutes,
                                 scale_response.seconds,
                                 scale_response.body_fat_percentage,
                                 scale_response.basal_metabolism,
                                 scale_response.muscle_percentage,
                                 scale_response.soft_lean_mass,
                                 scale_response.body_water_mass,
                                 scale_response.impedance
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
            csv_writer.writerow([scale_response.weight,
                                 scale_response.bmi,
                                 scale_response.height,
                                 scale_response.year,
                                 scale_response.month,
                                 scale_response.day,
                                 scale_response.hours,
                                 scale_response.minutes,
                                 scale_response.seconds,
                                 scale_response.body_fat_percentage,
                                 scale_response.basal_metabolism,
                                 scale_response.muscle_percentage,
                                 scale_response.soft_lean_mass,
                                 scale_response.body_water_mass,
                                 scale_response.impedance
                                 ])
