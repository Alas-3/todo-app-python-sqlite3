import sqlite3

# Function to create the to-do app database if it doesn't exist
def create_todo_app_database():
    conn = sqlite3.connect('todo_app.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 due_date TEXT,
                 priority INTEGER NOT NULL
                 )''')

    conn.commit()
    conn.close()

# Function to add a new task
def add_task(name, due_date, priority):
    conn = sqlite3.connect('todo_app.db')
    c = conn.cursor()

    c.execute("INSERT INTO tasks (name, due_date, priority) VALUES (?, ?, ?)", (name, due_date, priority))
    conn.commit()
    conn.close()

# Function to view all tasks
def view_tasks():
    conn = sqlite3.connect('todo_app.db')
    c = conn.cursor()

    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    conn.close()
    return tasks

# Function to delete a task by ID
def delete_task(task_id):
    conn = sqlite3.connect('todo_app.db')
    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
