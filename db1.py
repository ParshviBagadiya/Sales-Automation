import sqlite3

conn = sqlite3.connect("email_analytics.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in DB:", tables)
conn.close()
