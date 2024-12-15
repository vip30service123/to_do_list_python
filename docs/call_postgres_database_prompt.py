Act as a Python Developer. You are given a list of tasks. You must write python code based on the tasks.

Notes:
- The database framework that I use is Postgres so the syntax when call table must be Postgres.
- Use psycopg2 to call Postgres database.
- The description for the table in task is only reference, DO NOT CREATE A NEW TABLE.
- You must create files as in the task.

### Tasks
- Create a python file, called "connection.py".
- In "connection.py":
	+ Create an function that connect to the postgres database.
	+ The input attributes should contain all the configuration for the database.
	+ The input attributes for this object should contain table name.
	+ The output must be a postgres object.
- Create a python file, called "authentication.py".
- In "authentication.py"
 	+ Create 2 functions for creating and reading table "USER".
	+ The input of 2 functions must contain the return object from "connection.py".
	+ The description for table USER is as follow:
		CREATE TABLE "USER" (
    			ID SERIAL PRIMARY KEY,
    			USERNAME VARCHAR(255),
    			PASSWORD VARCHAR(255),
    			CREATED_TIME TIMESTAMP
		);
	+ The function create return True if the input is inserted successfully, return False otherwise.
	+ The function read must return a list of all user.
- Create a python file, called "todo_list.py"
- In "todo_list.py"
	+ Create 4 functions for creating, reading, updating, and deleting table "TODO_LIST".
	+ The input of 4 functions must contain the return object from "connection.py"
	+ The description for table TODO_LIST is as follow:
		CREATE TABLE TODO_LIST (
    			USER_ID INTEGER NOT NULL UNIQUE,
    			CONTENT TEXT,
    			CREATED_TIME TIMESTAMP,
    			FOREIGN KEY (USER_ID) REFERENCES "USER"(ID)
		);
	+ The function create return True if the input is inserted successfully, return False otherwise.
	+ The functions read, update, and delete return list of todo_list.
