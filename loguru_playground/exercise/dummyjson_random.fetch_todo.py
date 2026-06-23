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

def main():
    todo = load_data(id=random_id())
    print(todo)

if __name__ == "__main__":
    main()
