import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"


@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def init_db():
    from .models.student import create_table as student_create_table
    from .models.teacher import create_table as teacher_create_table
    from .models.course import create_table as course_create_table
    student_create_table()
    teacher_create_table()
    course_create_table()













