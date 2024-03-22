from params import params

# SQL scripts related to banking profile dimension
banking_profile_dim_table_name = "banking_profile_dim"

# SQL command to create banking profile dimension table
create_banking_profile_dim_table = f"""CREATE TABLE {banking_profile_dim_table_name} (
    Bank_Profile_Key SERIAL PRIMARY KEY,
    Tenure SMALLINT NOT NULL,
    Active_Member SMALLINT NOT NULL,
    Products_Number SMALLINT NOT NULL,
    Balance FLOAT NOT NULL,
    Complain SMALLINT NOT NULL
);"""

# SQL command to drop banking profile dimension table
drop_banking_profile_dim_table = f"""DROP TABLE IF EXISTS {banking_profile_dim_table_name};"""

# SQL command to add data from CSV
add_banking_profile_dim_data = f"""COPY {banking_profile_dim_table_name}(Tenure, Active_Member, Products_Number, Balance, Complain)
FROM '{f'{params.csv_dir + params.banking_profile_dim_csv}'}'
DELIMITER ','
CSV HEADER;"""