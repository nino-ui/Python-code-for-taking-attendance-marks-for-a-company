import sqlite3
from datetime import datetime

# connect to the database
conn = sqlite3.connect('company.db')
c = conn.cursor()

# create table to store attendance marks if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (employee_id INTEGER, date TEXT, status TEXT)''')

# get current date
date = datetime.now().strftime('%Y-%m-%d')

# display list of employees
print("Employee List:")
c.execute("SELECT id, name FROM employees")
for row in c.fetchall():
    print(row[0], "-", row[1])

# prompt user for employee ID and attendance status
employee_id = int(input("Enter employee ID: "))
status = input("Enter attendance status (P/A/L): ").upper()

# check if employee exists
c.execute("SELECT COUNT(*) FROM employees WHERE id = ?", (employee_id,))
if c.fetchone()[0] == 0:
    print("Employee not found.")
else:
    # record attendance mark
    c.execute("INSERT INTO attendance VALUES (?, ?, ?)", (employee_id, date, status))
    conn.commit()
    print("Attendance marked for employee ID", employee_id)

# close the database connection
conn.close()
