import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('stocks.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_number TEXT NOT NULL,
    name TEXT NOT NULL,
    open_price REAL NOT NULL,
    close_price REAL NOT NULL,
    high_price REAL NOT NULL,
    low_price REAL NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
)
''')

# Commit and close
conn.commit()
conn.close()
 
