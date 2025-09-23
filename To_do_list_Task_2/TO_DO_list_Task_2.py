"""
Console-based To-Do List Application
A complete, feature-rich CLI to-do manager that stores tasks in a JSON-formatted
text file (tasks.txt). 
"""
import json
import datetime
import os


class TodoApp:
    """Core To-Do application logic"""
    def __init__(self, filename: str = "tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    # ----------------- Persistence -----------------
    def load_tasks(self):
        """Load tasks from disk"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    content = file.read().strip()
                    self.tasks = json.loads(content) if content else []
            except (json.JSONDecodeError, OSError):
                print("Warning: Corrupted tasks file. Starting fresh.")
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to disk"""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=2)
        except OSError as e:
            print(f"Error saving tasks: {e}")

    # ----------------- CRUD -----------------
    def add_task(self, description: str, priority: str = "medium", category: str = "general", due_date: str = None):
        if not description.strip():
            print("Task description cannot be empty!")
            return False
        task = {
            "id": len(self.tasks) + 1,
            "description": description.strip(),
            "completed": False,
            "priority": priority,
            "category": category,
            "created_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date,
            "completion_date": None,
            "notes": ""
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f" Task added! (ID: {task['id']})")
        return True

    def remove_task(self, task_id: int):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"🗑️ Removed task {task_id}")
                return True
        print(" Task not found")
        return False

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task already completed")
                    return False
                task["completed"] = True
                task["completion_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print("Task completed")
                return True
        print("Task not found")
        return False

    def uncomplete_task(self, task_id: int):
        for task in self.tasks:
            if task["id"] == task_id:
                if not task["completed"]:
                    print("Task already incomplete")
                    return False
                task["completed"] = False
                task["completion_date"] = None
                self.save_tasks()
                print("Task marked incomplete")
                return True
        print(" Task not found")
        return False

    def edit_task(self, task_id: int, field: str, new_value: str):
        for task in self.tasks:
            if task["id"] == task_id:
                if field in {"description", "priority", "category", "due_date", "notes"}:
                    task[field] = new_value
                    self.save_tasks()
                    print("Task updated")
                    return True
                print("Invalid field")
                return False
        print("Task not found")
        return False

    # ----------------- Views -----------------
    def view_tasks(self, filter_by: str = "all", sort_by: str = "id"):
        if not self.tasks:
            print("No tasks found!")
            return
        # filtering
        filtered = []
        for t in self.tasks:
            if filter_by == "all":
                filtered.append(t)
            elif filter_by == "completed" and t["completed"]:
                filtered.append(t)
            elif filter_by == "incomplete" and not t["completed"]:
                filtered.append(t)
            elif filter_by == "overdue":
                if t["due_date"] and not t["completed"] and datetime.datetime.strptime(t["due_date"], "%Y-%m-%d").date() < datetime.date.today():
                    filtered.append(t)
            elif filter_by.startswith("priority:"):
                if t["priority"] == filter_by.split(":")[1]:
                    filtered.append(t)
            elif filter_by.startswith("category:"):
                if t["category"] == filter_by.split(":")[1]:
                    filtered.append(t)
        # sorting
        if sort_by == "priority":
            order = {"high": 1, "medium": 2, "low": 3}
            filtered.sort(key=lambda x: order.get(x["priority"], 4))
        elif sort_by == "due_date":
            filtered.sort(key=lambda x: x["due_date"] or "9999-12-31")
        else:
            filtered.sort(key=lambda x: x[sort_by])
        # display
        print(f"Tasks ({filter_by}, sorted by {sort_by}):" + "="*80)

        symbols = {"high": "🔴", "medium": "🟡", "low": "🟢"}
        for t in filtered:
            status = "✅" if t["completed"] else "⏳"
            pri = symbols.get(t["priority"], "⚪")
            print(f"{status} [{t['id']}] {pri} {t['description']}")
            print(f"    Category: {t['category'].title()} | Priority: {t['priority'].title()}")
            print(f"    Created: {t['created_date']}")
            if t["due_date"]:
                overdue = "  OVERDUE" if not t["completed"] and datetime.datetime.strptime(t["due_date"], "%Y-%m-%d").date() < datetime.date.today() else ""
                print(f"    Due: {t['due_date']}{overdue}")
            if t["completed"] and t["completion_date"]:
                print(f"    Completed: {t['completion_date']}")
            if t["notes"]:
                print(f"    Notes: {t['notes']}")
            print("-"*80)

    def search_tasks(self, query: str):
        query = query.lower().strip()
        matches = [t for t in self.tasks if query in t["description"].lower() or query in t["notes"].lower() or query in t["category"].lower()]
        if not matches:
            print("No tasks found")
            return
        print(f" Search results for '{query}':")
        for t in matches:
            print(f"[{t['id']}] {t['description']}")

# --------------- CLI Helpers ---------------

def display_menu():
    print("" + "="*60)
    print(" TO-DO LIST APPLICATION")
    print("="*60)
    print("1.  Add Task")
    print("2.  View Tasks")
    print("3.  Complete Task")
    print("4.  Uncomplete Task")
    print("5.  Remove Task")
    print("6.  Edit Task")
    print("7.  Search Tasks")
    print("8. Help")
    print("0.  Exit")

def display_help():
    print("HELP: Enter the number corresponding to the action. Fields: description, priority, category, due_date, notes. Date format YYYY-MM-DD.")


def get_valid_priority():
    while True:
        p = input("Priority (high/medium/low) [medium]: ").strip().lower()
        if not p:
            return "medium"
        if p in {"high", "medium", "low"}:
            return p
        print("Invalid priority!")


def get_valid_date():
    while True:
        d = input("Due date YYYY-MM-DD [skip]: ").strip()
        if not d:
            return None
        try:
            datetime.datetime.strptime(d, "%Y-%m-%d")
            return d
        except ValueError:
            print("Invalid date format!")


def get_task_id():
    while True:
        try:
            return int(input("Task ID: "))
        except ValueError:
            print("Enter a valid number")

# --------------- Main Loop ---------------
def main():
    app = TodoApp()
    print(" Welcome! Tasks auto-save to 'tasks.txt'.")
    while True:
        display_menu()
        choice = input("Choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            desc = input("Description: ")
            pr = get_valid_priority()
            cat = input("Category [general]: ") or "general"
            due = get_valid_date()
            app.add_task(desc, pr, cat, due)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            app.view_tasks(filter_by="incomplete")
            app.complete_task(get_task_id())
        elif choice == "4":
            app.view_tasks(filter_by="completed")
            app.uncomplete_task(get_task_id())
        elif choice == "5":
            app.view_tasks()
            app.remove_task(get_task_id())
        elif choice == "6":
            app.view_tasks()
            tid = get_task_id()
            field = input("Field to edit: ")
            val = input("New value: ")
            app.edit_task(tid, field, val)
        elif choice == "7":
            app.search_tasks(input("Search query: "))
        elif choice == "8":
            display_help()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted. Bye!")





