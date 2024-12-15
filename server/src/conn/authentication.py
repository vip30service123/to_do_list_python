from psycopg2 import Error
from datetime import datetime
from typing import List, Dict, Optional, Any

def create_user(
    connection: Any,
    username: str,
    password: str
) -> bool:
    """
    Create a new user in the USER table.
    
    Args:
        connection: PostgreSQL connection object
        username (str): Username for the new user
        password (str): Password for the new user
        
    Returns:
        bool: True if user creation successful, False otherwise
    """
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO "USER" (USERNAME, PASSWORD, CREATED_TIME)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (username, password, datetime.now()))
        cursor.close()
        return True
    except (Exception, Error) as error:
        print(f"Error while creating user: {error}")
        return False

def read_users(connection: Any) -> List[Dict[str, Any]]:
    """
    Read all users from the USER table.
    
    Args:
        connection: PostgreSQL connection object
        
    Returns:
        List[Dict]: List of dictionaries containing user information
    """
    try:
        cursor = connection.cursor()
        select_query = 'SELECT * FROM "USER"'
        cursor.execute(select_query)
        users = cursor.fetchall()
        
        # Convert to list of dictionaries
        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'password': user[2],
                'created_time': user[3]
            }
            user_list.append(user_dict)
        
        cursor.close()
        return user_list
    except (Exception, Error) as error:
        print(f"Error while reading users: {error}")
        return []