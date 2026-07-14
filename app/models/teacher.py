from ..database import get_connection
def create_table():
    with get_connection() as connection:
       connection.execute(''' CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           department TEXT NOT NULL,
                           employee_id INTEGER NOT NULL
                           )''')