from ..database import get_connection
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