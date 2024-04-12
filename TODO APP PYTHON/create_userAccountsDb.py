import sqlite3

# Function to create the user accounts database if it doesn't exist
def create_user_accounts_database():
    conn = sqlite3.connect('user_accounts.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 username TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL
                 )''')

    conn.commit()
    conn.close()

# Function to create a new user
def create_user(username, password):
    conn = sqlite3.connect('user_accounts.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # User with this username already exists
        conn.close()
        return False

# Function to authenticate a user
def authenticate_user(username, password):
    conn = sqlite3.connect('user_accounts.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    return user
