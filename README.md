# Student Task & Study Planner

## 1. Project Overview

Student Task & Study Planner is a console-based application created using the Python language that assists students in managing their tasks.

The application enables the creation of tasks based on subject, priority, and deadlines. Tasks can be updated, searched, filtered, deleted, and marked as completed. It also supports deadline tracking, task analysis, and productivity reports.

Information about the tasks is stored in a local JSON file so that data may be reloaded in case the application is launched again.

The project has a modular design with separate modules being dedicated to the following tasks: task management, deadline management, progress tracking, task analysis, reports, validation, storage, and console interface.

---

## 2. Features

### Task Management

- Add a new task
- View all tasks
- Search tasks by title
- Update existing tasks
- Delete tasks
- Automatically assign task IDs
- Renumber task IDs after deletion

### Progress Management

- Mark a task as completed
- View all pending tasks
- Filter tasks by status
- Filter tasks by priority
- Calculate completion progress

### Deadline Management

- View overdue tasks
- View upcoming tasks within the next 7 days
- Count overdue tasks
- Count upcoming tasks

### Analytics

The application provides:

- Total number of tasks
- Number of completed tasks
- Number of pending tasks
- Completion rate
- Subject-wise workload
- Priority distribution
- Completion statistics by subject

### Productivity Report

The productivity report combines task and deadline information to provide:

- Task summary
- Completion rate
- Deadline summary
- Overdue task count
- Upcoming task count
- Subject workload
- Priority distribution
- Completion by subject
- Overall productivity classification

The productivity level is classified as:

- Excellent
- Good
- Average
- Needs Improvement

### Input Validation

The application validates:

- Empty task titles
- Empty subjects
- Task IDs
- Integer input
- Priority values
- Deadline format

### Persistent Storage

Tasks are stored locally in:

`data/tasks.json`

The application loads saved tasks when it starts and saves changes whenever task data is modified.

---

## 3. Technologies and Tools Used

### Programming Language

- Python 3

### Python Standard Library

The project uses standard Python modules including:

- `json` - for storing and loading task data
- `datetime` - for validating and processing deadlines
- `timedelta` - for calculating upcoming deadlines
- `pathlib` - for handling the persistent storage file path

No external Python packages are required.

### Development Tools

- Visual Studio Code
- Command Prompt / PowerShell / Terminal
- Git
- GitHub

---

## 4. Project Structure

```text
Student_Task_Planner/
│
├── main.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── task_manager.py
│   ├── deadline_manager.py
│   ├── progress_manager.py
│   ├── analytics.py
│   ├── reports.py
│   ├── storage.py
│   ├── validators.py
│   └── utils.py
│
├── data/
│   └── tasks.json
│
└── docs/
    └── statement.md
```

### Module Description

#### `main.py`

The main entry point of the application.

It:

- Displays the main menu
- Accepts user input
- Validates input where required
- Connects the different managers
- Executes the selected operation
- Loads and saves task data

#### `src/task_manager.py`

Handles the core task management functionality.

It contains:

- `Task`
- `TaskManager`

The module manages:

- Adding tasks
- Viewing tasks
- Updating tasks
- Deleting tasks
- Searching tasks
- Filtering tasks

#### `src/deadline_manager.py`

Handles deadline-related operations.

It provides functionality for:

- Finding overdue tasks
- Finding upcoming tasks
- Counting overdue tasks
- Counting upcoming tasks

#### `src/progress_manager.py`

Handles task completion and progress-related functionality.

It provides:

- Marking tasks as completed
- Viewing pending tasks
- Calculating progress information

#### `src/analytics.py`

Calculates statistics from the stored tasks.

It provides:

- Basic task statistics
- Subject workload
- Priority distribution
- Completion statistics by subject

#### `src/reports.py`

Generates the overall student productivity report by combining information from the analytics and deadline managers.

#### `src/storage.py`

Handles persistent storage using JSON.

It provides:

- `load_tasks()`
- `save_tasks()`

Task data is stored in `data/tasks.json`.

#### `src/validators.py`

Contains functions used to validate user input.

It validates:

- Priority
- Deadline
- Empty input
- Task IDs
- Integer values

#### `src/utils.py`

Contains reusable command-line interface functions, including the formatted main menu.

#### `data/tasks.json`

Stores the task data locally in JSON format.

#### `docs/statement.md`

Contains the project problem statement, scope, target users, and high-level features.

---

## 5. Requirements

The project requires:

- Python 3.x
- A terminal or command-line environment

No external Python packages are required.

The included `requirements.txt` file documents that the project uses only Python standard-library modules.

---

## 6. Installation

### Step 1: Install Python

Install Python 3.x on your system.

Verify the installation using:

```bash
python --version
```

If the `python` command is not available on your system, try:

```bash
python3 --version
```

### Step 2: Get the Project

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd Student_Task_Planner
```

Alternatively, the project can be downloaded and opened directly in a terminal.

---

## 7. Running the Project

Open a terminal in the project root and run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

The application will display the Student Task & Study Planner menu.

The project is designed to run from the command line without requiring a graphical interface.

---

## 8. Using the Application

After starting the program, the main menu provides the following options:

```text
[1]  Add Task
[2]  View Tasks
[3]  Search Tasks
[4]  Update Task
[5]  Delete Task
[6]  Mark Task Complete
[7]  View Pending Tasks
[8]  Filter Tasks
[9]  View Overdue Tasks
[10] View Upcoming Tasks
[11] Analytics
[12] Productivity Report
[13] Exit
```

### Adding a Task

Select:

```text
1
```

Enter:

- Task title
- Subject
- Priority
- Deadline

The deadline must use:

```text
YYYY-MM-DD
```

Valid priorities are:

```text
High
Medium
Low
```

The task is then saved to `data/tasks.json`.

### Viewing Tasks

Select:

```text
2
```

The application displays all stored tasks.

### Searching Tasks

Select:

```text
3
```

Enter a keyword to search task titles.

### Updating a Task

Select:

```text
4
```

Enter the task ID and provide the updated task information.

### Deleting a Task

Select:

```text
5
```

Enter the task ID to delete the task.

### Completing a Task

Select:

```text
6
```

Enter the task ID to mark the task as completed.

### Viewing Pending Tasks

Select:

```text
7
```

The application displays tasks that are still pending.

### Filtering Tasks

Select:

```text
8
```

Tasks can be filtered by:

- Status
- Priority

### Viewing Overdue Tasks

Select:

```text
9
```

The application displays pending tasks whose deadlines have already passed.

### Viewing Upcoming Tasks

Select:

```text
10
```

The application displays pending tasks with deadlines within the next 7 days.

### Viewing Analytics

Select:

```text
11
```

The analytics section provides:

- Basic statistics
- Subject-wise workload
- Priority distribution
- Completion by subject

### Viewing the Productivity Report

Select:

```text
12
```

The application generates a combined productivity report containing task, deadline, workload, priority, and completion information.

### Exiting

Select:

```text
13
```

to exit the application.

---

## 9. Data Storage

The application uses a local JSON file:

```text
data/tasks.json
```

The file stores information such as:

- Task ID
- Task title
- Subject
- Priority
- Deadline
- Completion status

When the application starts, previously saved tasks are loaded from the JSON file.

When task information is modified, the updated data is saved back to the JSON file.

No external database is required.

The storage path is handled using Python's `pathlib` module so that the application can locate the data file relative to the project structure.

---

## 10. Testing Instructions

The application can be tested directly from the command line.

Start the application using:

```bash
python main.py
```

The following functionality can be tested.

### Task Operations

- Add a task
- View tasks
- Search for a task
- Update a task
- Delete a task
- Mark a task as completed

### Filtering

- Filter by status
- Filter by priority

### Deadline Features

- Add a task with a past deadline and check overdue tasks
- Add a task with a deadline within the next 7 days and check upcoming tasks

### Analytics

Check:

- Basic statistics
- Subject workload
- Priority distribution
- Completion by subject

### Productivity Report

Verify that the report displays:

- Task totals
- Completion rate
- Deadline counts
- Subject workload
- Priority distribution
- Completion by subject
- Overall productivity

### Validation

Test invalid inputs such as:

- Empty task title
- Empty subject
- Invalid priority
- Invalid date format
- Non-numeric task ID
- Task ID that does not exist
- Invalid menu option

### Persistence

1. Add one or more tasks.
2. Exit the application.
3. Start the application again.
4. Verify that the previously saved tasks are loaded.

---

## 11. Error Handling and Validation

The application includes input validation to prevent common invalid inputs.

Examples include:

- Empty task information
- Invalid priority values
- Incorrect deadline format
- Non-numeric task IDs
- Task IDs that do not exist
- Invalid menu choices

The validation functions are implemented separately in `src/validators.py`.

---

## 12. Design Approach

The project uses a modular approach.

Each major responsibility is separated into its own Python module.

The general application flow is:

```text
                         USER
                           |
                           v
                        main.py
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       Task Management  Progress      Deadlines
       task_manager.py  progress_     deadline_manager.py
                         manager.py
             |             |             |
             +-------------+-------------+
                           |
                           v
                       Analytics
                     analytics.py
                           |
                           v
                       Reporting
                      reports.py

                   Persistent Storage
                           |
                           v
                       storage.py
                           |
                           v
                    data/tasks.json
```

This separation makes the project easier to understand, maintain, and extend.

---

## 13. Object-Oriented Programming

The project uses object-oriented programming through classes such as:

- `Task`
- `TaskManager`
- `DeadlineManager`
- `ProgressManager`
- `AnalyticsManager`
- `ReportManager`

The `Task` class represents an individual student task, while the manager classes handle specific categories of operations.

---

## 14. Future Enhancements

Possible future improvements include:

- Graphical user interface
- More advanced task sorting
- Recurring tasks
- Study-time tracking
- Reminder notifications
- Exporting reports to PDF or CSV
- More detailed productivity analytics
- Database-based storage
- User accounts and multiple student profiles

---

## 15. Project Status

The current version is a command-line based Student Task & Study Planner with:

- Modular Python architecture
- Object-oriented programming
- JSON-based persistent storage
- Input validation
- Task management
- Progress tracking
- Deadline tracking
- Analytics
- Productivity reporting
- Organized source, data, and documentation folders

---

## 16. Author

Neha Jaiswal
Registration Number: 26BAI10087
