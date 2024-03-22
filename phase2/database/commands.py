from scripts.banking_profile_dim import BankingProfileDim
from scripts.location_dim import LocationDim
from scripts.customer_profile_dim import CustomerProfileDim
from utils import copy_dim_files_to_tmp

def create_tables(conn):
    """ Create a table in the PostgreSQL database """
    print("Creating tables")
    commands = [
        BankingProfileDim.create_table,
        LocationDim.create_table,
        CustomerProfileDim.create_table
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
        CustomerProfileDim.add_data
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