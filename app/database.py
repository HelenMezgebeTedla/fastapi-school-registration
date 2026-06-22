from contextlib import contextmanager
import sqlite3

sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()

def create_table():
    with get_db_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                country TEXT NOT NULL,
                id_number INTEGER NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL,
                id_number INTEGER NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                code TEXT NOT NULL,
                credits INTEGER NOT NULL,
                department TEXT NOT NULL,
                max_capacity INTEGER NOT NULL
            )
        """)
        connection.commit()

def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute(
            "INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)",
            (name, age, email, country, id_number),
        )
        connection.commit()

def get_students():
    with get_db_connection() as connection:
        rows = connection.execute("SELECT * FROM students").fetchall()
        return [dict(row) for row in rows]

def add_teacher(name, email, department, salary, id_number):
    with get_db_connection() as connection:
        connection.execute(
            "INSERT INTO teachers (name, email, department, salary, id_number) VALUES (?, ?, ?, ?, ?)",
            (name, email, department, salary, id_number),
        )
        connection.commit()

def get_teachers():
    with get_db_connection() as connection:
        rows = connection.execute("SELECT * FROM teachers").fetchall()
        return [dict(row) for row in rows]

def add_course(title, code, credits, department, max_capacity):
    with get_db_connection() as connection:
        connection.execute(
            "INSERT INTO courses (title, code, credits, department, max_capacity) VALUES (?, ?, ?, ?, ?)",
            (title, code, credits, department, max_capacity),
        )
        connection.commit()

def get_courses():
    with get_db_connection() as connection:
        rows = connection.execute("SELECT * FROM courses").fetchall()
        return [dict(row) for row in rows]
    

def update_student(student_id, name, age, email, country, id_number):
    with get_db_connection() as connection:
        cursor = connection.execute(
            "UPDATE students SET name=?, age=?, email=?, country=?, id_number=? WHERE id=?",
            (name, age, email, country, id_number, student_id)
        )
        connection.commit()
        return cursor.rowcount > 0

def delete_student(student_id):
    with get_db_connection() as connection:
        cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()
        return cursor.rowcount > 0

def update_teacher(teacher_id, name, email, department, salary, id_number):
    with get_db_connection() as connection:
        cursor = connection.execute(
            "UPDATE teachers SET name=?, email=?, department=?, salary=?, id_number=? WHERE id=?",
            (name, email, department, salary, id_number, teacher_id)
        )
        connection.commit()
        return cursor.rowcount > 0

def delete_teacher(teacher_id):
    with get_db_connection() as connection:
        cursor = connection.execute("DELETE FROM teachers WHERE id = ?", (teacher_id,))
        connection.commit()
        return cursor.rowcount > 0

def update_course(course_id, title, code, credits, department, max_capacity):
    with get_db_connection() as connection:
        cursor = connection.execute(
            "UPDATE courses SET title=?, code=?, credits=?, department=?, max_capacity=? WHERE id=?",
            (title, code, credits, department, max_capacity, course_id)
        )
        connection.commit()
        return cursor.rowcount > 0

def delete_course(course_id):
    with get_db_connection() as connection:
        cursor = connection.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        connection.commit()
        return cursor.rowcount > 0















# from contextlib import contextmanager
# import sqlite3

# sqlite_file_name = "school.db"


# @contextmanager
# def get_db_connection():
#     connection = sqlite3.connect(sqlite_file_name)
#     connection.row_factory = sqlite3.Row
#     try:
#         yield connection
#     finally:
#         connection.close()


# def create_table():
#     with get_db_connection() as connection:
#         connection.execute(
#             """
#             CREATE TABLE IF NOT EXISTS students (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 age INTEGER NOT NULL,
#                 email TEXT NOT NULL,
#                 country TEXT NOT NULL,
#                 id_number INTEGER NOT NULL
#             )
#         """
#         )


# def add_student(name, age, email, country, id_number):
#     with get_db_connection() as connection:
#         connection.execute(
#             """
#             INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)
#         """,
#             (name, age, email, country, id_number),
#         )
#         connection.commit()


# def get_students():
#     with get_db_connection() as connection:
#         rows = connection.execute("SELECT * FROM students").fetchall()
#         return [dict(row) for row in rows]










# # import _sqlite3
# # from contextlib import contextmanager

# # sqlite_file_name= "school.db"

# # @contextmanager
# # def get_db_connection():
# #     Connection= sqlite3.connect(sqlite_file_name)
# #     Connection.row_factory = sqlite3.Row
# #     try:
# #         yield Connection
# #     finally:
# #         Connection.close()

    
# # def create_table():
# #     with get_db_connection() as connection:
# #         connection.execute(
# #             '''
# #             CREATE TABLE IF NOT EXISTS students (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 name TEXT NOT NULL,
# #                 age INTEGER NOT NULL,
# #                 email TEXT NOT NULL,
# #                 country TEXT NOT NULL,
# #                 id_number INTEGER NOT NULL
# #             )
# #         '''
# #         )

# # def add_student(name, age, email, country, id_number):
# #     with get_db_connection() as connection:
# #         connection.execute(
# #             """
# #             INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)
# #         """,
# #             (name, age, email, country, id_number),
# #         )
# #         connection.commit()


# # def get_students():
# #     with get_db_connection() as connection:
# #         return  connection.execute(execute("SELECT * FROM students").fetchall()
# #         )