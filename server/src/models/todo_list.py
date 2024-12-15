from pydantic import BaseModel


class TodoCreate(BaseModel):
    username: str
    content: str


class TodoUpdate(BaseModel):
    username: str
    current_content: str
    new_content: str


class TodoDelete(BaseModel):
    username: str
    content: str