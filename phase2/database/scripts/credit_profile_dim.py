from params import params

class CreditProfileDim:
    # SQL scripts related to customer profile dimension
    table_name = "credit_profile_dim"

    # SQL command to create customer profile dimension table
    create_table = f"""CREATE TABLE {table_name} (
    credit_profile_key SERIAL PRIMARY KEY,
    credit_card_ownership SMALLINT NOT NULL,
    credit_score FLOAT NOT NULL,
    credit_card_type VARCHAR(10) NOT NULL,);"""
    
    # SQL command to drop customer profile dimension table
    drop_table = f"""DROP TABLE IF EXISTS {table_name};"""

    # SQL command to add data from CSV
    add_data = f"""COPY {table_name}(credit_profile_key, credit_card_ownership, credit_score, credit_card_type)
    FROM '{f'{params.tmp_dir + params.credit_profile_dim_csv}'}'
    DELIMITER ','
    CSV HEADER;"""