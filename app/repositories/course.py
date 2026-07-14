from ..database import get_connection
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

