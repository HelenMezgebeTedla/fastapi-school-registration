from database import get_db_connection

def add_teacher(name, email, course, teacher_id):
    with get_db_connection() as connection:
        connection.execute('INSERT INTO teachers (name, email, course, teacher_id) VALUES (?,?,?,?)',
                           (name, email, course, teacher_id))

def get_teachers():
    with get_db_connection() as connection:
        return [dict(row) for row in connection.execute('SELECT * FROM teachers').fetchall()]

def get_teacher(teacher_id):
    with get_db_connection() as connection:
        row = connection.execute('SELECT * FROM teachers WHERE id = ?', (teacher_id,)).fetchone()
        return dict(row) if row else None

def update_teacher(id, name, email, course, teacher_id):
    with get_db_connection() as connection:
        connection.execute('UPDATE teachers SET name = ?, email = ?, course = ?, teacher_id = ? WHERE ID = ?',
                           (name, email, course, teacher_id, id))
        return {"id": id, "name": name, "email": email, "course": course, "teacher_id": teacher_id}

def delete_teacher(id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id = ?', (id,))
