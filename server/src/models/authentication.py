from pydantic import BaseModel


class UserSignUp(BaseModel):
    username: str
    password: str
    password_again: str


class UserLogin(BaseModel):
    username: str
    password: str