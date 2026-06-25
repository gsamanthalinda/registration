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

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL
                           )''')
        connection.execute(''' CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           department TEXT NOT NULL,
                           employee_id INTEGER NOT NULL
                           )''')
        connection.execute(''' CREATE TABLE IF NOT EXISTS courses(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           description TEXT NOT NULL,
                           credits INTEGER NOT NULL,
                           teacher_id INTEGER NOT NULL,
                           course_code TEXT NOT NULL
                           )''')



def add_student(name, age, email, country, id_number): 
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (name,age,email,country,id_number) VALUES(?,?,?,?,?)',
            (name, age, email, country, id_number)
        )

def get_students():
    with get_connection() as connection:
        
        rows = connection.execute('SELECT * FROM students').fetchall()
        return list(map(dict, rows))

def get_student(student_id): 
    with get_connection() as connection:
        row = connection.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
        return dict(row) if row else None

def update_student(student_id, name, age, email, country, id_number): 
    with get_connection() as connection:
        connection.execute('UPDATE students SET name = ?, age = ?, email = ?, country = ?, id_number = ? WHERE id = ?',
                           (name, age, email, country, id_number, student_id))

def delete_student(student_id): 
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id = ?', (student_id,))




def add_teacher(name, age, email, department, employee_id): 
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers(name,age,email,department,employee_id) VALUES(?,?,?,?,?)',
            (name, age, email, department, employee_id)
        )

def get_teachers():
    with get_connection() as connection:
        rows = connection.execute('SELECT * FROM teachers').fetchall()
        return list(map(dict, rows))

def get_teacher(teacher_id): 
    with get_connection() as connection:
        row = connection.execute('SELECT * FROM teachers WHERE id = ?', (teacher_id,)).fetchone()
        return dict(row) if row else None

def update_teacher(teacher_id, name, age, email, department, employee_id): 
    with get_connection() as connection:
        connection.execute('UPDATE teachers SET name = ?, age = ?, email = ?, department = ?, employee_id = ? WHERE id = ?',
                           (name, age, email, department, employee_id, teacher_id))

def delete_teacher(teacher_id): 
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id=?', (teacher_id,))



def add_course(title, description, credits, teacher_id, course_code):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses(title,description,credits,teacher_id,course_code) VALUES(?,?,?,?,?)',
            (title, description, credits, teacher_id, course_code)
        )

def get_courses():
    with get_connection() as connection:
        rows = connection.execute('SELECT * FROM courses').fetchall()
        return list(map(dict, rows))

def get_course(course_id): 
    with get_connection() as connection:
        row = connection.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
        return dict(row) if row else None

def update_course(course_id, title, description, credits, teacher_id, course_code): 
    with get_connection() as connection:
        connection.execute('UPDATE courses SET title = ?, description = ?, credits = ?, teacher_id = ?, course_code = ? WHERE id = ?',
                           (title, description, credits, teacher_id, course_code, course_id))

def delete_course(course_id): 
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id=?', (course_id,))
