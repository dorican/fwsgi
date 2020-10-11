import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()
with open('create_db.sql', 'r') as student:
    student_text = student.read()
cur.executescript(student_text)
cur.close()
con.close()

