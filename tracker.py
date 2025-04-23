from flask import Flask, send_file, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Logs an event (open/click) into the SQLite database
def log_event(lead_id, event_type):
    conn = sqlite3.connect("email_analytics.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id TEXT,
            event TEXT,
            timestamp TEXT
        )
    ''')
    cursor.execute("INSERT INTO analytics (lead_id, event, timestamp) VALUES (?, ?, ?)",
                   (lead_id, event_type, datetime.now()))
    conn.commit()
    conn.close()

# Optional: homepage to confirm the server is running
@app.route("/")
def home():
    return "✅ Flask Email Tracker is Running!"



# Tracking pixel endpoint
@app.route("/track/open/<lead_id>")
def track_open(lead_id):
    log_event(lead_id, "open")
    return send_file("pixel.png", mimetype="image/png")

# Click tracking endpoint
@app.route("/track/click/<lead_id>")
def track_click(lead_id):
    log_event(lead_id, "click")
    return redirect("https://www.example.com")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
