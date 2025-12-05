import sqlite3

conn = sqlite3.connect('shaft_data.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM shaft_calculations')

results = cursor.fetchall()


for row in results :
    print(f"قطر: {row[0]} , شکل : {row[1]} , چگالی: {row[2]}")
    
    
conn.close()

