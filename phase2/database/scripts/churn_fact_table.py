from params import params

class ChurnFactTable:
    # SQL scripts related to churn fact table
    table_name = "churn_fact_table"

    # SQL command to create churn fact table
    create_table = f"""CREATE TABLE {table_name} (
            customer_key INTEGER NOT NULL,
            bank_profile_key INTEGER NOT NULL,
            credit_profile_key INTEGER NOT NULL,
            location_key INTEGER NOT NULL,
            churn SMALLINT NOT NULL,
            PRIMARY KEY (customer_key, bank_profile_key, credit_profile_key, location_key),
            FOREIGN KEY (customer_key) 
            REFERENCES customer_profile_dim (customer_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (bank_profile_key) 
            REFERENCES banking_profile_dim (bank_profile_key)
            ON UPDATE CASCADE ON DELETE NO ACTION,
            FOREIGN KEY (credit_profile_key) 
            REFERENCES credit_profile_dim (credit_profile_key)
            ON UPDATE CASCADE ON DELETE NO ACTION,
            FOREIGN KEY (location_key) 
            REFERENCES location_dim (location_key) 
            ON UPDATE CASCADE ON DELETE NO ACTION);"""
    
    # SQL command to drop churn fact table
    drop_table = f"DROP TABLE IF EXISTS {table_name};"

    # SQL command to add data from CSV
    add_data = f"""COPY {table_name}(customer_key, bank_profile_key, credit_profile_key, location_key, churn)
    FROM '{f'{params.tmp_dir + params.churn_fact_table_csv}'}'
    DELIMITER ','
    CSV HEADER;"""