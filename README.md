# To-Do List Application

A simple, lightweight command-line To-Do List application written in Python. It lets users add tasks, view pending tasks, remove tasks once completed, and tracks overall progress with a live text-based progress bar.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Session](#example-session)
- [How Progress Is Calculated](#how-progress-is-calculated)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features

- **Add tasks**: create new tasks with a short description.
- **View tasks**: display all pending tasks in a numbered list.
- **Remove completed tasks**: remove a task by its number once it is done.
- **Progress bar**: shows the percentage of completed tasks after every action.
- **Input validation**: handles empty tasks, invalid menu choices, and non-numeric input without crashing.

## Requirements

- Python 3.6 or higher
- No external libraries required

## Installation

1. Clone the repository or download the project files:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Confirm Python is installed:

   ```bash
   python --version
   ```

## Usage

Run the program from the terminal:

```bash
python toDo.py
```

Use the on-screen menu:

| Option | Action                    |
|--------|---------------------------|
| 1      | Add a new task            |
| 2      | View pending tasks        |
| 3      | Remove a completed task   |
| 4      | Exit the application      |

## Example Session

```text
===== TO-DO LIST =====
1. Add task
2. View tasks
3. Remove completed task
4. Exit
Choose an option (1-4): 1
Enter task: Finish assignment
Added: 'Finish assignment'

Progress: [------------------------------] 0% (0/1 completed)

Choose an option (1-4): 3
Enter the number of the completed task: 1
Completed and removed: 'Finish assignment'

Progress: [##############################] 100% (1/1 completed)
```

## How Progress Is Calculated

Completed tasks are removed from the list, so the program keeps two counters:

- **Total**: the number of tasks added during the session.
- **Completed**: the number of tasks removed as completed.

```text
Progress (%) = (Completed / Total) x 100
```

## Project Structure

```text
.
├── ToDo.py    # Main application
└── README.md      # Project documentation
```

## Future Improvements

- Save and load tasks from a file (JSON) so data persists between sessions.
- Add due dates and priority levels.
- Add an option to edit existing tasks.
- Build a graphical interface (Tkinter) or a web version.

## License

This project is intended for educational purposes. You are free to use and modify it.