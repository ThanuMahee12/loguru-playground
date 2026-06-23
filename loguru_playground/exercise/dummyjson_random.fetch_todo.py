import urllib.request
import json
import random
import sqlite3
from loguru_playground.config.env import DB_PATH

DB_PATH.mkdir(parents=True, exist_ok=True)
DB_FILE = DB_PATH / "dummyjson.db"



def load_random_todo_data(id: int | None = None) -> dict:
    if id is None:
        id = random.randint(1, 200)
    req = urllib.request.Request(
        f"https://dummyjson.com/todos/{id}",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())
    
def load_random_user_data(id: int | None = None) -> dict:
    if id is None:
        id = random.randint(1, 200)
    req = urllib.request.Request(
        f"https://dummyjson.com/users/{id}",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def init_db(conn:sqlite3.Connection):
    conn.execute(
         """
 CREATE TABLE IF NOT EXISTS user (
       id          INTEGER PRIMARY KEY,
      first_name        TEXT,
      last_name   TEXT,
      age     TEXT
      )
"""
     )
       
    conn.execute(
         """
 CREATE TABLE IF NOT EXISTS todos (
       id          INTEGER PRIMARY KEY,
      todo        TEXT,
      completed   INTEGER,
      user_id     INTEGER
      )
"""
     )