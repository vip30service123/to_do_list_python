import psycopg2
from psycopg2 import Error
from typing import Optional

def connect_database(
    host: str,
    database: str,
    user: str,
    password: str,
    port: str = "5432",
    table_name: str = None
) -> Optional[psycopg2.extensions.connection]:
    """
    Create a connection to PostgreSQL database.
    
    Args:
        host (str): Database host
        database (str): Database name
        user (str): Database user
        password (str): Database password
        port (str): Database port (default: 5432)
        table_name (str): Name of the table to be accessed
        
    Returns:
        psycopg2.extensions.connection: PostgreSQL connection object if successful, None otherwise
    """
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        connection.autocommit = True
        return connection
    except (Exception, Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return None