from fastapi import FastAPI

from authentication import authentication
from todo_list import todo_list


app = FastAPI()


app.include_router(authentication.router)
app.include_router(todo_list.router)