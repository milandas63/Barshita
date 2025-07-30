import mysql.connector as my

conn = my.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'barshita'
)

curr = conn.cursor()
curr.execute("SELECT * FROM contact")

for row in curr:
    print()
    for col in row:
        print(col, end=' | ')
