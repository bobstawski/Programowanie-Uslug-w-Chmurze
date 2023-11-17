import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=polska-lab1.database.windows.net, 1433;'
    'DATABASE=PUWC;'
    'UID=sql;'
    'PWD=confidential;'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
)
cursor = conn.cursor()

cursor.execute('DROP TABLE ExampleTable')
conn.commit()

cursor.execute('''
    CREATE TABLE ExampleTable (
        ID INT IDENTITY(1,1) PRIMARY KEY,
        Name NVARCHAR(50),
        Age INT
    )
''')

cursor.execute("INSERT INTO ExampleTable (Name, Age) VALUES (?, ?)", 'Alice', 25)
cursor.execute("INSERT INTO ExampleTable (Name, Age) VALUES (?, ?)", 'Mariusz', 30)
cursor.execute("INSERT INTO ExampleTable (Name, Age) VALUES (?, ?)", 'Charlie', 28)

conn.commit()

cursor.execute('SELECT * FROM ExampleTable')

for row in cursor.fetchall():
    print(f'Dane z bazy w konsoli: {row}')

conn.close()