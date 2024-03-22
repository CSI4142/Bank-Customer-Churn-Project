from params import params

class CustomerProfileDim:
    # SQL scripts related to customer profile dimension
    table_name = "customer_profile_dim"

    # SQL command to create customer profile dimension table
    create_table = f"""CREATE TABLE {table_name} (
    customer_id SERIAL PRIMARY KEY,
    surname VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age SMALLINT NOT NULL,
    estimated_salary FLOAT NOT NULL);"""
    
    # SQL command to drop customer profile dimension table
    drop_table = f"""DROP TABLE IF EXISTS {table_name};"""

    # SQL command to add data from CSV
    add_data = f"""COPY {table_name}(customer_id, surname, gender, age, estimated_salary)
    FROM '{f'{params.tmp_dir + params.customer_profile_dim_csv}'}'
    DELIMITER ','
    CSV HEADER;"""