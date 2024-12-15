from fastapi import APIRouter, HTTPException, status
from typing import Optional
from psycopg2 import Error
from datetime import datetime

# Import the provided functions
from conn.connection import connect_database
from conn.authentication import create_user, read_users
from models.authentication import (
    UserLogin,
    UserSignUp
)


router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignUp):
    connection = connect_database(
        "localhost",
        "todo_list",
        "postgres",
        "123456",
        table_name="\"USER\""
    )

    # Validate passwords match
    if user.password != user.password_again:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )
    
    # Check if username already exists
    existing_users = read_users(connection)  # Note: connection should be passed from your main app
    if any(existing_user['username'] == user.username for existing_user in existing_users):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists"
        )
    
    # Create new user
    success = create_user(
        connection=connection,  # Note: connection should be passed from your main app
        username=user.username,
        password=user.password  # In production, this should be hashed
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user"
        )
    
    return {"message": "User created successfully"}

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: UserLogin):
    connection = connect_database(
        "localhost",
        "todo_list",
        "postgres",
        "123456",
        table_name="\"USER\""
    )

    # Get all users
    existing_users = read_users(connection)  # Note: connection should be passed from your main app
    
    # Check if user exists and password matches
    user_found = False
    password_correct = False
    
    for existing_user in existing_users:
        if existing_user['username'] == user.username:
            user_found = True
            if existing_user['password'] == user.password:  # In production, use proper password comparison
                password_correct = True
            break
    
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    
    return {"message": "Login successful"}