# Task Management System

This is a simple task management system written in Python. It allows users to create tasks and assign them to other users. Each task has a title, description, assigned user, date assigned, due date, and status. The system also allows new users to register.

## How to use

1. Clone the repository or download the code.
2. Open a terminal window and navigate to the folder where the code is located.
3. Run the command `python task_manager.py` to start the program.
4. If you are an existing user, enter your username and password to log in. If you are a new user, you will need to register first.
5. Once you are logged in, you will see a menu with several options:
   - Register a new user
   - Add a task
   - View all tasks
   - View your tasks
   - View the total number of tasks and users
   - Exit
6. To register a new user, select option "r" from the menu and enter the new user's information as prompted.
7. To add a task, select option "a" from the menu and enter the task information as prompted.
8. To view all tasks, select option "va" from the menu.
9. To view your tasks, select option "vm" from the menu.
10. To view the total number of tasks and users, select option "s" from the menu.
11. To exit the program, select option "e" from the menu.

## Files

The code uses two text files to store user and task data: `user.txt` and `tasks.txt`. These files should be in the same directory as the `task_manager.py` file. The `user.txt` file contains one line for each user, with the username and password separated by a comma and a space. The `tasks.txt` file contains one line for each task, with the assigned user, title, description, date assigned, due date, and status separated by a comma and a space. The status is either "Yes" or "No", indicating whether the task is complete.

## Requirements

The code requires Python 3 to be installed on your computer.