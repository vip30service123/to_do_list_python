from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from datetime import datetime

from conn.connection import connect_database
from conn.todo_list import (
    create_todo,
    read_todos,
    update_todo,
    delete_todo
)
from models.todo_list import (
    TodoCreate,
    TodoDelete,
    TodoUpdate
)


# Initialize router
router = APIRouter(
    prefix="/todo",
    tags=["todo_list"]
)


# Database connection dependency
async def get_db():
    # This should be replaced with your actual database connection logic
    connection = connect_database(
        "localhost",
        "todo_list",
        "postgres",
        "123456",
        table_name="\"USER\""
    ) 

    try:
        yield connection
    finally:
        if connection:
            connection.close()


@router.post("/create", response_model=List[Dict[str, Any]])
async def create_todo_item(todo: TodoCreate, db: Any = Depends(get_db)):
    """
    Create a new todo item
    """
    try:
        result = create_todo(
            connection=db,
            username=todo.username,
            content=todo.content
        )
        if not result:
            raise HTTPException(status_code=400, detail="Failed to create todo item")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/read", response_model=List[Dict[str, Any]])
async def read_todo_items(username: Optional[str] = None, db: Any = Depends(get_db)):
    """
    Read todo items, optionally filtered by username
    """
    try:
        todos = read_todos(
            connection=db,
            username=username
        )
        return todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update", response_model=List[Dict[str, Any]])
async def update_todo_item(todo: TodoUpdate, db: Any = Depends(get_db)):
    """
    Update an existing todo item
    """
    try:
        updated_todos = update_todo(
            connection=db,
            username=todo.username,
            current_content=todo.current_content,
            new_content=todo.new_content
        )
        if not updated_todos:
            raise HTTPException(status_code=404, detail="Todo item not found")
        return updated_todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete", response_model=List[Dict[str, Any]])
async def delete_todo_item(todo: TodoDelete, db: Any = Depends(get_db)):
    """
    Delete a todo item
    """
    try:
        remaining_todos = delete_todo(
            connection=db,
            username=todo.username,
            content=todo.content
        )
        return remaining_todos
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))