from dotenv import dotenv_values
import psycopg2
from params import params
from commands import create_tables, drop_tables, add_data

def connect():
    config = dotenv_values(".env")
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def program():
    conn = connect()
    try:
        print('Connected to the PostgreSQL server.')
        # if only want to reset
        if params.reset:
            print('Dropping tables')
            # drop tables
            drop_tables(conn)
            return conn
        # if running for the first time
        if params.fresh_start:
            # drop tables if they already exist
            drop_tables(conn)
            # create tables
            create_tables(conn)
            # add data
            add_data(conn)
        else:
            print('Tables already created')

        # close the connection
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    

if __name__ == '__main__':
    program()