import sqlite3

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('contact_book.db')
cursor = conn.cursor()

# Create the table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        CellNumber TEXT,
        Email TEXT
    )
''')

# Insert 5 rows of data
contacts_data = [
    ('John Doe', '123-456-7890', 'john@example.com'),
    ('Jane Doe', '987-654-3210', 'jane@example.com'),
    ('Alice Smith', '555-123-4567', 'alice@example.com'),
    ('Bob Johnson', '777-888-9999', 'bob@example.com'),
    ('Charlie Brown', '111-222-3333', 'charlie@example.com')
]

cursor.executemany('''
    INSERT INTO contacts (Name, CellNumber, Email) VALUES (?, ?, ?)
''', contacts_data)

# Commit changes and close connection
conn.commit()

# Fetch all data and display them
cursor.execute('SELECT * FROM contacts')
all_contacts = cursor.fetchall()

print("\nID\tName\t\tCell#\t\t\tE-mail")
print("-" * 40)
for contact in all_contacts:
    contact_id, name, cell_number, email = contact
    print(f"{contact_id}\t{name}\t{cell_number}\t{email}")

# Close the connection
conn.close()
