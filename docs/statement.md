# Student Task & Study Planner

## 1. Problem Statement

Most times, a student will have various academic-related tasks, assignments, projects, and learning activities with various priorities and deadlines. It becomes hard for students to manage such academic activities using manual means since it might not be easy to know which task is pending, overdue, or the academic progress in general.

The Student Task & Study Planner is a command-line application created using Python programming language that makes it easier for students to manage academic tasks. Users of the program are able to add various tasks with subject, priority and deadline, check progress, find overdue or future tasks, and see various statistics and productivity.

Tasks are locally saved in a JSON file so that tasks are saved even after the application is stopped.

---

## 2. Scope of the Project

The project focuses on managing academic tasks through a command-line interface.

The system covers:

- Creating and storing academic tasks
- Viewing existing tasks
- Searching tasks by title
- Updating task information
- Deleting tasks
- Marking tasks as completed
- Viewing pending tasks
- Filtering tasks by status or priority
- Identifying overdue tasks
- Identifying upcoming tasks within the next 7 days
- Calculating task and completion statistics
- Analyzing subject-wise workload
- Analyzing priority distribution
- Generating a student productivity report
- Persisting task information using a JSON file
- Validating common user inputs

The current project is designed for local, single-user command-line use. It does not include a graphical user interface, online synchronization, user accounts, or an external database.

---

## 3. Target Users

The primary target users are:

- College students
- School students
- Students managing multiple subjects and academic deadlines

The application is especially useful for students who want a lightweight command-line tool for organizing assignments, study tasks, and other academic work.

---

## 4. High-Level Features

### Task Management

Users can:

- Add tasks
- View tasks
- Search tasks
- Update tasks
- Delete tasks

### Task Progress Tracking

Users can:

- Mark tasks as completed
- View pending tasks
- Filter tasks by completion status
- Track overall completion progress

### Priority Management

Each task can be assigned one of three priorities:

- High
- Medium
- Low

Users can also filter tasks based on priority.

### Deadline Management

The system can:

- Identify overdue pending tasks
- Identify upcoming pending tasks within the next 7 days
- Count overdue tasks
- Count upcoming tasks

### Analytics

The application provides:

- Total task count
- Completed task count
- Pending task count
- Completion rate
- Subject-wise workload
- Priority distribution
- Completion by subject

### Productivity Reporting

The application generates a productivity report containing task statistics, deadline information, subject workload, priority distribution, completion information, and an overall productivity classification.

### Persistent Storage

Task information is stored locally in `tasks.json` using Python's JSON functionality.

### Input Validation

The system validates important inputs such as:

- Empty task titles
- Empty subjects
- Invalid priorities
- Invalid deadlines
- Invalid task IDs
- Non-numeric task IDs

## 5. Non-Functional Requirements

### 5.1 Usability

* There should be an easy-to-understand command-line user interface.
* There should be menu items that accurately describe the available actions.
* The users should be able to manage their tasks without having any technical background knowledge.
* Clear messages should be provided for successful actions and invalid inputs.

### 5.2 Reliability

* The task information should stay accessible even after closing and reopening the program.
* The program should not crash in case of an invalid user input.
* The task data should be saved every time when the task information is added, changed or deleted.
* The system should properly determine the pending, completed, overdue and future tasks.

### 5.3 Performance

* Functions such as add, display, search, update, and delete tasks must be performed without any perceivable lag time in terms of a regular student load.
* Efficient creation of analytics and productivity reports based on the stored task data must be performed by the system.
* The application must consume only the required resources for its operation.

### 5.4 Maintainability

* The software must have a modular design where different duties will be segregated into separate Python modules.
* Task management, deadline management, tracking, analysis, reporting, storage, and validation must stay separately managed.
* There must be reuse of functions and classes in order to facilitate any further changes in the future.
* It should enable easy addition of new features without making major changes to unrelated modules.

### 5.5 Error Handling

* Tasks having null titles or subjects should be declined.
* Invalid priority levels should be declined.
* Deadline dates that do not match the proper format should be declined.
* Invalid or non-numeric task numbers should be processed without terminating the program.
* Incorrect menu choices should generate the proper error message and allow the user to use the program.