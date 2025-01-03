from psycopg2 import Error
from datetime import datetime
from typing import List, Dict, Any, Optional

def create_todo(
    connection: Any,
    username: str,
    content: str
) -> List[Dict[str, Any]]:
    """
    Create a new todo item in the TODO_LIST table.
    
    Args:
        connection: PostgreSQL connection object
        user_id (int): ID of the user creating the todo
        content (str): Content of the todo item
        
    Returns:
        bool: True if creation successful, False otherwise
    """
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO TODO_LIST (USERNAME, CONTENT, CREATED_TIME)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (username, content, datetime.now()))
        cursor.close()
        return read_todos(connection, username)
    
    except (Exception, Error) as error:
        print(f"Error while creating todo: {error}")
        return []

def read_todos(
    connection: Any,
    username: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Read todo items from the TODO_LIST table.
    
    Args:
        connection: PostgreSQL connection object
        user_id (int, optional): Filter todos by user ID
        
    Returns:
        List[Dict]: List of dictionaries containing todo information
    """
    try:
        cursor = connection.cursor()
        if username:
            select_query = """
                SELECT * FROM TODO_LIST WHERE USERNAME = %s
            """
            cursor.execute(select_query, (username,))
        else:
            select_query = "SELECT * FROM TODO_LIST"
            cursor.execute(select_query)
            
        todos = cursor.fetchall()
        
        # Convert to list of dictionaries
        todo_list = []
        for todo in todos:
            todo_dict = {
                'user_id': todo[0],
                'content': todo[1],
                'created_time': todo[2]
            }
            todo_list.append(todo_dict)
        
        cursor.close()
        return todo_list
    
    except (Exception, Error) as error:
        print(f"Error while reading todos: {error}")
        return []

def update_todo(
    connection: Any,
    username: str,
    current_content: str,
    new_content: str
) -> List[Dict[str, Any]]:
    """
    Update a todo item in the TODO_LIST table.
    
    Args:
        connection: PostgreSQL connection object
        user_id (int): ID of the user whose todo is being updated
        new_content (str): New content for the todo item
        
    Returns:
        List[Dict]: Updated list of todos for the user
    """
    try:
        cursor = connection.cursor()
        update_query = """
            UPDATE TODO_LIST
            SET CONTENT = %s
            WHERE USERNAME = %s AND CONTENT = %s
        """
        cursor.execute(update_query, (new_content, username, current_content))
        cursor.close()
        
        # Return updated list of todos
        return read_todos(connection, username)
    
    except (Exception, Error) as error:
        print(f"Error while updating todo: {error}")
        return []

def delete_todo(
    connection: Any,
    username: str,
    content: str
) -> List[Dict[str, Any]]:
    """
    Delete a todo item from the TODO_LIST table.
    
    Args:
        connection: PostgreSQL connection object
        user_id (int): ID of the user whose todo is being deleted
        
    Returns:
        List[Dict]: Updated list of todos (excluding deleted item)
    """
    try:
        cursor = connection.cursor()
        delete_query = """
            DELETE FROM TODO_LIST
            WHERE USERNAME = %s AND CONTENT = %s
        """
        cursor.execute(delete_query, (username, content))
        cursor.close()
        
        # Return updated list of todos
        return read_todos(connection, username)
    
    except (Exception, Error) as error:
        print(f"Error while deleting todo: {error}")
        return []