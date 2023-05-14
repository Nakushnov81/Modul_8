import sqlite3
# from datetime import datetime
conn = sqlite3.connect('Varsity.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Student (id INT PRIMARY KEY, name TEXT, surname TEXT, age int, city TEXT)''')

cur.execute('CREATE TABLE IF NOT EXISTS Course (id INT PRIMARY KEY, name TEXT, time_start TIMESTAMP, time_end TIMESTAMP)')

cur.execute('CREATE TABLE IF NOT EXISTS Student_courses (student_id INT, FOREIGN KEY(student_id) REFERENCES Student(id), course_id INT, FOREIGN KEY(course_id) REFERENCES Course(id))')

stud = [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manchester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')
]

courses = [(1, 'python', '21.07.21', '21.08.21'),
    (2, 'java', '13.07.21', '16.08.21')]

Student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

# cur.executemany("""INSERT INTO Student VALUES(?,?,?,?,?)""", stud)

# cur.executemany("""INSERT INTO Course VALUES(?,?,?,?)""", courses)
# conn.commit()
# cur.executemany('''INSERT INTO Course VALUES(?,?)''', Student_courses)
# cur.execute("DROP TABLE Student_courses")
conn.commit()

# cur.execute("""SELECT * FROM Course""")

# print(cur.fetchall())

cur.execute("""SELECT * FROM Student_courses""")

print(cur.fetchall())

conn.close()

