import psycopg2
try:
    conn=4

    print("db connected successfully")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.commit()
    print(students)
except Exception as err:
    print("Not connected", err)   