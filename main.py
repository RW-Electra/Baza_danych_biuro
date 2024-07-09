import pyodbc

server = '192.168.1.187\\SQL'
database = 'Test'
username = 'sa'
password = '1234'

connection_string = (f"DRIVER={{SQL Server Native Client 11.0}};"
                     f"SERVER={server};"
                     f"DATABASE={database};"
                     f"UID={username};"
                     f"PWD={password}")

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()
select_string = "SELECT * FROM Dane_testowe"
insert_string = "INSERT Dane_testowe (ID,data,Desctriptio) VALUES ('3','23.4','VPN')"

connection.autocommit = True
cursor.execute(insert_string)
connection.autocommit = False

cursor.execute(select_string)
print(cursor.fetchall())

cursor.close()
connection.close()