from params import params

class LocationDim:
    # SQL scripts related to location dimension
    table_name = "location_dim"

    # SQL command to create location dimension table
    create_table = f"""CREATE TABLE {table_name} (
        Location_key SERIAL PRIMARY KEY,
        Country VARCHAR(20) NOT NULL
    );"""

    # SQL command to drop location dimension table
    drop_table = f"""DROP TABLE IF EXISTS {table_name};"""

    # SQL command to add data from CSV
    add_data = f"""COPY {table_name}(Location_key, Country)
    FROM '{f'{params.tmp_dir + params.location_dim_csv}'}'
    DELIMITER ','
    CSV HEADER;"""