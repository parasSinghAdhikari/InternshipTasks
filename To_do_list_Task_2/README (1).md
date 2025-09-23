# Console-based To-Do List Application

This is a feature-rich console (CLI) To-Do List application written in Python. It allows you to manage tasks locally using a JSON-formatted text file for persistence.

## Features

- **Add Tasks**: Create tasks with description, priority (high/medium/low), category, due date, and optional notes.
- **View Tasks**: Display all tasks with filtering (all, completed, incomplete, overdue, by priority, by category) and sorting (ID, priority, due date, created date).
- **Complete/Uncomplete**: Mark tasks as done or undo completion.
- **Edit Tasks**: Modify task fields: description, priority, category, due date, and notes.
- **Remove Tasks**: Delete tasks permanently by ID.
- **Search Tasks**: Search tasks by keywords in description, notes, or category.
- **Statistics**: View summary of total, completed, incomplete, overdue tasks, priority and category breakdown.
- **Export**: Export tasks to `.txt` or `.csv` files.
- **Persistence**: Tasks are stored in `tasks.txt` in JSON format and auto-saved on every change.
- **Help Menu**: In-app guidance for commands and field formats.

## Prerequisites

- Python 3.7 or higher

## Installation

1. Clone or download this repository.
2. Ensure `TO_DO_list_Task_2.py` is in the project directory.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the application:

   ```bash
   python TO_DO_list_Task_2.py
   ```

3. Follow on-screen menu prompts:
   - Enter the number corresponding to the desired action (e.g., 1 to add a task).
   - Input task details when prompted.
   - Use 0 to exit the application.

4. All tasks are saved in `tasks.txt` automatically.

## File Structure

```├── TO_DO_list_Task_2.py   # Main application script
   ├── tasks.txt             # Stores tasks in JSON format (created on first run)
   └── README.md             # This documentation file
```

## Task Fields

- **id**: Unique integer identifier
- **description**: Task description (string)
- **completed**: Boolean status
- **priority**: `high`, `medium`, or `low`
- **category**: Custom category (e.g., work, personal)
- **created_date**: Timestamp when task was created
- **due_date**: Optional due date (`YYYY-MM-DD`)
- **completion_date**: Timestamp when task was completed
- **notes**: Additional notes (string)

## Examples

- Add a new task:
  ```
  Enter choice: 1
  Description: Finish project report
  Priority (high/medium/low): high
  Category [general]: work
  Due date YYYY-MM-DD [optional]: 2025-10-01
  ```

- View all tasks:
  ```
  Enter choice: 2
  ```

- Export tasks to CSV:
  ```
  Enter choice: 9
  Format txt/csv [txt]: csv
  ```

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

## License

This project is released under the MIT License.