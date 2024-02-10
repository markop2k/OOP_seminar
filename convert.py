import sqlite3

fd = open('tablice.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')
conn = sqlite3.connect("faks.db")
cursor = conn.cursor()
for command in sqlCommands:
    conn.execute(command)
    conn.commit()