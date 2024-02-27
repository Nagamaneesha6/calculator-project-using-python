import tkinter as tk

class TodoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(root, width=50)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.tasks_listbox.bind("<ButtonRelease-1>", self.load_task)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=2, column=1, padx=10, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            selection = self.tasks_listbox.curselection()
            task_index = selection[0]
            del self.tasks[task_index]
            self.tasks_listbox.delete(task_index)
        except IndexError:
            pass

    def load_task(self, event=None):
        try:
            selection = self.tasks_listbox.curselection()
            task_index = selection[0]
            task = self.tasks_listbox.get(task_index)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, task)
        except IndexError:
            pass

    def edit_task(self):
        try:
            selection = self.tasks_listbox.curselection()
            task_index = selection[0]
            new_task = self.task_entry.get()
            self.tasks[task_index] = new_task
            self.tasks_listbox.delete(task_index)
            self.tasks_listbox.insert(task_index, new_task)
            self.task_entry.delete(0, tk.END)
        except IndexError:
            pass

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()
