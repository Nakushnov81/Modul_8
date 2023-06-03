import sqlite3
def create_db():
    conn = sqlite3.connect('Varsity.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Student (id INT PRIMARY KEY,
                name TEXT, surname TEXT, age int, city TEXT)''')

    cur.execute('CREATE TABLE IF NOT EXISTS Course (id INT PRIMARY KEY,'
                    ' name TEXT, time_start TIMESTAMP, time_end TIMESTAMP)')

    cur.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
                    student_id INT,
                    course_id INT,
                    FOREIGN KEY(student_id) REFERENCES Student(id),
                    FOREIGN KEY(course_id) REFERENCES Course(id)
                    )''')

    stud = [
            (1, 'Max', 'Brooks', 24, 'Spb'),
            (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manchester'),
            (4, 'Kate', 'Brooks', 34, 'Spb')
        ]

    courses = [(1, 'python', '21.07.21', '21.08.21'),
            (2, 'java', '13.07.21', '16.08.21')]

    Student_cour = [(1, 1), (2, 1), (3, 1), (4, 2)]

    try:
        cur.executemany("""INSERT INTO Student VALUES(?,?,?,?,?)""", stud)
        conn.commit()
    except sqlite3.Error:
        print('Ошибка внесения данных студента')
        pass

    try:
        cur.executemany("""INSERT INTO Course VALUES(?,?,?,?)""", courses)
        conn.commit()
    except sqlite3.Error:
        print('Ошибка внесения данных курса')
        pass

    try:
        cur.executemany('''INSERT INTO Student_courses VALUES(?,?)''', Student_cour)
        conn.commit()
    except sqlite3.Error:
        print('Ошибка внесения данных')
        pass

def get_old_students():
    conn = sqlite3.connect('Varsity.sqlite')
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM Student WHERE age > 30""")
        print(cur.fetchall())

    except sqlite3.Error:
        print('Ошибка запроса')
        pass
    conn.close()

def get_course():
    conn = sqlite3.connect('Varsity.sqlite')
    cur = conn.cursor()
    try:
        cur.execute("""SELECT python FROM Course""")
        print(cur.fetchall())
    except sqlite3.Error:
        print('Ошибка запроса')
        pass
    conn.close()

def get_data():
    conn = sqlite3.connect('Varsity.sqlite')
    cur = conn.cursor()
    try:
        cur.execute("""SELECT student.name, student.surname FROM Student JOIN Student_courses ON 
        Student_courses.course_id == 1
        """)
        print(cur.fetchall())
        conn.close()

    except sqlite3.Error:
        print('Ошибка запроса')
        pass


get_data()
