from scripts.banking_profile_dim import BankingProfileDim
from scripts.location_dim import LocationDim
from scripts.customer_profile_dim import CustomerProfileDim
from scripts.churn_fact_table import ChurnFactTable
from params import params
from utils import copy_dim_files_to_tmp

class Commands:
    def create_database(conn):
        """ Create a database in the PostgreSQL database """
        print("Creating database")
        # create a cursor
        cur = conn.cursor()
        # create database
        cur.execute(f"CREATE DATABASE {params.db_name};")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Database created successfully')

    def drop_database(conn):
        """ Drop a database in the PostgreSQL database """
        print("Dropping database")
        # create a cursor
        cur = conn.cursor()
        # drop database
        cur.execute(f"DROP DATABASE IF EXISTS {params.db_name};")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Database dropped successfully')

    def use_database(conn):
        """ Use a database in the PostgreSQL database """
        print("Using database")
        # create a cursor
        cur = conn.cursor()
        # use database
        cur.execute(f"USE {params.db_name};")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print(f'Database {params.db_name} in use')

    def create_tables(conn):
        """ Create a table in the PostgreSQL database """
        print("Creating tables")
        commands = [
            BankingProfileDim.create_table,
            LocationDim.create_table,
            CustomerProfileDim.create_table,
            ChurnFactTable.create_table
        ]
        # create a cursor
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Tables created successfully')

    def drop_tables(conn):
        """ Drop a table in the PostgreSQL database """
        print("Dropping tables")
        commands = [
            ChurnFactTable.drop_table,
            BankingProfileDim.drop_table,
            LocationDim.drop_table,
            CustomerProfileDim.drop_table
        ]
        # create a cursor
        cur = conn.cursor()
        # drop table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Tables dropped successfully')

    def add_data(conn):
        """ Add data to the PostgreSQL database """
        print("Adding data")
        # before we can add data, we need to copy the dimension 
        # files to the temporary directory for them to be accessible
        copy_dim_files_to_tmp()
        commands = [
            BankingProfileDim.add_data,
            LocationDim.add_data,
            CustomerProfileDim.add_data,
            ChurnFactTable.add_data
        ]
        # create a cursor
        cur = conn.cursor()
        # add data one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Data added successfully')