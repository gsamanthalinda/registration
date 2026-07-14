from ..database import get_connection 
def create_table():
    with get_connection() as connection:
        connection.execute(''' CREATE TABLE IF NOT EXISTS courses(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           description TEXT NOT NULL,
                           credits INTEGER NOT NULL,
                           teacher_id INTEGER NOT NULL,
                           course_code TEXT NOT NULL
                           )''')