from params import params

class BankingProfileDim:
    # SQL scripts related to banking profile dimension
    table_name = "banking_profile_dim"

    # SQL command to create banking profile dimension table
    create_table = f"""CREATE TABLE {table_name} (
        Bank_Profile_Key SERIAL PRIMARY KEY,
        Tenure SMALLINT NOT NULL,
        Active_Member SMALLINT NOT NULL,
        Products_Number SMALLINT NOT NULL,
        Balance FLOAT NOT NULL,
        Complain SMALLINT NOT NULL
    );"""

    # SQL command to drop banking profile dimension table
    drop_table = f"""DROP TABLE IF EXISTS {table_name};"""

    # SQL command to add data from CSV
    add_data = f"""COPY {table_name}(Bank_Profile_Key, Tenure, Active_Member, Products_Number, Balance, Complain)
    FROM '{f'{params.tmp_dir + params.banking_profile_dim_csv}'}'
    DELIMITER ','
    CSV HEADER;"""