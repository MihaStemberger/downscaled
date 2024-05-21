import psycopg2

from model.scale_response import ScaleResponse


def persist_to_database(scale_response: ScaleResponse):
    # Database connection parameters
    conn_params = {
        'dbname': 'hakunamatata',
        'user': 'postgres',
        'password': 'mysecretpassword',
        'host': 'localhost',
        'port': '5432'
    }

    # Create a connection to the PostgreSQL database
    connection = psycopg2.connect(**conn_params)

    query = """
    INSERT INTO scale_data (
        weight, bmi, height, body_fat_percentage, 
        basal_metabolism, muscle_percentage, soft_lean_mass, 
        body_water_mass, impedance
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        scale_response.weight,
        scale_response.bmi,
        scale_response.height,
        scale_response.body_fat_percentage,
        scale_response.basal_metabolism,
        scale_response.muscle_percentage,
        scale_response.soft_lean_mass,
        scale_response.body_water_mass,
        scale_response.impedance
    )

    with connection.cursor() as cursor:
        cursor.execute(query, values)
        connection.commit()

    # Close the database connection
    connection.close()
