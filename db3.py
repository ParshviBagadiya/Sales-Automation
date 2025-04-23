import sqlite3

# Connect to SQLite DB (creates the file if it doesn't exist)
conn = sqlite3.connect("email_analytics.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the analytics table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS analytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id TEXT NOT NULL,
        event TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("✅ Database and 'analytics' table created successfully.")
