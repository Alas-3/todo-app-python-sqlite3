import tkinter as tk
from tkinter import messagebox
from crud_operations import *
from crud_operations import delete_task


# Function to handle the add task button
def add_task_handler(task_entry, priority_var):
    task_name = task_entry.get()

    if not task_name:
        messagebox.showerror("Error", "Task name is required.")
        return

    priority = priority_var.get() + 1
    add_task(task_name, priority)
    refresh_tasks()

# Function to refresh and display tasks
# Function to refresh and display tasks
def refresh_tasks():
    task_list.delete(0, tk.END)
    tasks = view_tasks()
    if tasks:
        for task in tasks:
            task_list.insert(tk.END, f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}")
            print(f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}")  # Print task to IDLE shell
    else:
        task_list.insert(tk.END, "No tasks found.")


# Function to handle the delete task button
def delete_task_handler():
    selected_task_index = task_list.curselection()
    
    if selected_task_index:
        try:
            selected_task_text = task_list.get(selected_task_index)
            task_id = selected_task_text.split(':')[1].split(',')[0].strip()
            task_id = int(task_id)
            
            delete_task(task_id)
            refresh_tasks()  # Refresh the task list after deletion
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete task: {e}")
    else:
        messagebox.showerror("Error", "Please select a task to delete.")



# Function to show the to-do app interface
def show_todo_app():
    root = tk.Tk()
    root.title("To-Do List App")

    tk.Label(root, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
    task_entry = tk.Entry(root)  
    task_entry.grid(row=0, column=1, padx=5, pady=5)

    priority_var = tk.IntVar()
    tk.Label(root, text="Priority:").grid(row=0, column=2, padx=5, pady=5)
    low_priority = tk.Radiobutton(root, text="Low", variable=priority_var, value=0)
    low_priority.grid(row=0, column=3, padx=5, pady=5)
    high_priority = tk.Radiobutton(root, text="High", variable=priority_var, value=1)
    high_priority.grid(row=0, column=4, padx=5, pady=5)
    priority_var.set(0)

    add_task_button = tk.Button(root, text="Add Task", command=lambda: add_task_handler(task_entry, priority_var))
    add_task_button.grid(row=0, column=5, padx=5, pady=5)

    delete_task_button = tk.Button(root, text="Delete Task", command=delete_task_handler)
    delete_task_button.grid(row=1, column=0, padx=5, pady=5)

    global task_list  
    task_list_label = tk.Label(root, text="Current To-Do Tasks:")
    task_list_label.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

    task_list = tk.Listbox(root, height=10, width=80, selectmode=tk.SINGLE)
    task_list.grid(row=3, columnspan=6, padx=5, pady=5)

    refresh_tasks()

    root.mainloop()

if __name__ == "__main__":
    create_todo_app_database()
    show_todo_app()
