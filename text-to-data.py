import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('prompts.db')
c = conn.cursor()

# Create a table to store the data
c.execute('''CREATE TABLE IF NOT EXISTS prompts (
                id INTEGER PRIMARY KEY,
                prompt TEXT
             )''')

# Read data from the text file and insert into the database
with open('text.txt', 'r') as file:
    line = file.readline().strip()
    prompts = line.split('||')
    for prompt in prompts:
        c.execute('INSERT INTO prompts (prompt) VALUES (?)', (prompt.strip(),))

# Commit changes and close the connection
conn.commit()
conn.close()
