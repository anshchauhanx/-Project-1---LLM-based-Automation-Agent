import sqlite3
import os

# Ensure the "data" folder exists
os.makedirs("data", exist_ok=True)

# Connect to (or create) the SQLite database
db_path = "data/ticket-sales.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the "tickets" table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    type TEXT,
    units INTEGER,
    price REAL
);
""")

# Insert sample data
cursor.executemany("""
INSERT INTO tickets (type, units, price) VALUES (?, ?, ?);
""", [
    ('Gold', 10, 50.0),
    ('Silver', 20, 30.0),
    ('Gold', 5, 50.0),
    ('Bronze', 15, 20.0)
])

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"✅ Database created successfully at {db_path}")
