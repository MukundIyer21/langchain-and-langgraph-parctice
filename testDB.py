import sqlite3


conn = sqlite3.connect('school.db')


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no INTEGER UNIQUE NOT NULL,
    science INTEGER,
    maths INTEGER,
    english INTEGER,
    history INTEGER
)
''')

students_data = [
    ('Alice', 101, 85, 90, 88, 92),
    ('Bob', 102, 78, 82, 80, 76),
    ('Charlie', 103, 92, 88, 95, 90),
    ('Diana', 104, 70, 75, 68, 72)
]

cursor.executemany('''
INSERT INTO students (name, roll_no, science, maths, english, history)
VALUES (?, ?, ?, ?, ?, ?)
''', students_data)


conn.commit()
conn.close()

print("Database 'school.db' created with 'students' table successfully!")
