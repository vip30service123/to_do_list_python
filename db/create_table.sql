-- Create USER table
CREATE TABLE "USER" (
    USERNAME VARCHAR(255) PRIMARY KEY,
    PASSWORD VARCHAR(255),
    CREATED_TIME TIMESTAMP
);

-- Create TODO_LIST table          !!!! Must contain content_id
CREATE TABLE TODO_LIST (
    CONTENT_ID SERIAL PRIMARY KEY,
    USERNAME VARCHAR(255) NOT NULL,
    CONTENT TEXT,
    CREATED_TIME TIMESTAMP,
    FOREIGN KEY (USERNAME) REFERENCES "USER"(USERNAME)
);