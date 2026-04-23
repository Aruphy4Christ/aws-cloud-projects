import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='webuser',
    password='Password123!',
    database='rufusdb'
)

cursor = conn.cursor()
cursor.execute("INSERT INTO visitors (name) VALUES ('Rufus')")
conn.commit()

cursor.execute("SELECT * FROM visitors")
for row in cursor.fetchall():
    print(row)

conn.close()
print("Database connected successfully!")
