from database import get_db_connection

def add_course(name, code, credits):
    with get_db_connection() as connection:
        connection.execute('INSERT INTO courses (name, code, credits) VALUES (?, ?, ?)', (name, code, credits))

def get_courses():
    with get_db_connection() as connection:
        rows = connection.execute('SELECT * FROM courses').fetchall()
        return [dict(row) for row in rows]

def get_course(course_id):
    with get_db_connection() as connection:
        row = connection.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
        return dict(row) if row else None

def update_course(course_id, name, code, credits):
    with get_db_connection() as connection:
        connection.execute('UPDATE courses SET name = ?, code = ?, credits = ? WHERE id = ?', (name, code, credits, course_id))
        return {"id": course_id, "name": name, "code": code, "credits": credits}

def delete_course(course_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id = ?', (course_id,))
