import sqlite3
import pandas as pd

conn = sqlite3.connect("email_analytics.db")
df = pd.read_sql_query("SELECT * FROM analytics", conn)
print(df)
