import tkinter as tk
import time
import sqlite3
from datetime import datetime, timedelta

class TimeTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Tracker App")

        self.create_database()

        self.project_label = tk.Label(root, text="Select Project:")
        self.project_label.pack()

        self.project_listbox = tk.Listbox(root)
        self.project_listbox.pack()

        self.projects = self.load_projects()

        self.timer_running = False
        self.start_time = None

        self.timer_label = tk.Label(root, text="Timer: 00:00:00")
        self.timer_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)

        self.start_button.pack()
        self.stop_button.pack()

        self.update_project_listbox()

        self.project_listbox.bind("<<ListboxSelect>>", self.select_project)

    def create_database(self):
        self.conn = sqlite3.connect("projects.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                time_spent INTEGER,
                date TEXT
            )
        ''')

        self.conn.commit()
        self.conn.close()

    def load_projects(self):
        projects = []

        self.conn = sqlite3.connect("projects.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT name FROM projects")
        rows = self.cursor.fetchall()

        self.conn.close()

        for row in rows:
            projects.append(row[0])

        return projects

    def add_project(self, project_name, time_spent):
        self.conn = sqlite3.connect("projects.db")
        self.cursor = self.conn.cursor()

        current_date = datetime.now().strftime("%Y-%m-%d")

        self.cursor.execute("INSERT INTO projects (name, time_spent, date) VALUES (?, ?, ?)",
                            (project_name, time_spent, current_date))

        self.conn.commit()
        self.conn.close()

    def select_project(self, event):
        try:
            selected_project = self.project_listbox.get(self.project_listbox.curselection())
            self.project_var.set(selected_project)
        except:
            pass

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()

            self.project_listbox.config(state=tk.DISABLED)

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            elapsed_time = time.time() - self.start_time
            self.update_timer(elapsed_time)

            selected_project = self.project_var.get()
            self.update_project_time(selected_project, int(elapsed_time))

            self.project_listbox.config(state=tk.NORMAL)

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self, elapsed_time=None):
        if elapsed_time is None:
            elapsed_time = time.time() - self.start_time

        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.timer_label.config(text=f"Timer: {time_str}")

    def update_project_time(self, project_name, elapsed_time):
        self.conn = sqlite3.connect("projects.db")
        self.cursor = self.conn.cursor()

        current_date = datetime.now().strftime("%Y-%m-%d")

        self.cursor.execute("SELECT time_spent FROM projects WHERE name=? AND date=?",
                            (project_name, current_date))
        current_time = self.cursor.fetchone()

        if current_time:
            current_time = current_time[0] + elapsed_time
            self.cursor.execute("UPDATE projects SET time_spent=? WHERE name=? AND date=?",
                                (current_time, project_name, current_date))
        else:
            self.cursor.execute("INSERT INTO projects (name, time_spent, date) VALUES (?, ?, ?)",
                                (project_name, elapsed_time, current_date))

        self.conn.commit()
        self.conn.close()

    def update_project_listbox(self):
        self.projects = self.load_projects()
        self.project_listbox.delete(0, tk.END)
        for project in self.projects:
            self.project_listbox.insert(tk.END, project)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTrackerApp(root)
    root.mainloop()
