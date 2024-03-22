import sys
# from phase2.database.scripts.banking_profile_dim import create_banking_profile_dim_table, drop_banking_profile_dim_table, add_banking_profile_dim_data

# sys.path.append('./scripts')

from scripts.banking_profile_dim import create_banking_profile_dim_table, drop_banking_profile_dim_table, add_banking_profile_dim_data

def create_tables(conn):
    """ Create a table in the PostgreSQL database """
    print("Creating tables")
    commands = [
        create_banking_profile_dim_table
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
        drop_banking_profile_dim_table
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
    commands = [
        add_banking_profile_dim_data
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