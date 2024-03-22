from dotenv import dotenv_values
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from params import params
from commands import Commands

def connect():
    config = dotenv_values(".env")
    """ Connect to the PostgreSQL server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def connectDB():
    config = dotenv_values(".env")
    """ Connect to the PostgreSQL database server """
    # add database name to the config
    config['database'] = params.db_name
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
            # drop database
            Commands.drop_database(conn)
            # drop tables
            Commands.drop_tables(conn)
            return conn
        # if running for the first time
        if params.fresh_start:
            # drop database if it already exists
            Commands.drop_database(conn)
            # create database
            Commands.create_database(conn)
            # use database
            conn = connectDB()
            # drop tables if they already exist
            Commands.drop_tables(conn)
            # create tables
            Commands.create_tables(conn)
            # add data
            Commands.add_data(conn)
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