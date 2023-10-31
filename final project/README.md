# TODO APPLICATION
#### Video Demo:  https://youtu.be/Cij6uceOPwY
#### Description:
## Overview

The To-Do List Application is a command-line tool designed to help you manage your tasks effectively. It provides a simple interface for adding, updating, and deleting tasks, making it a valuable asset for staying organized in your daily life or small projects.

## Project Files

- **project.py**: This file serves as the core of the application. It encompasses the main functionality, handling user interactions through a user-friendly menu, task management, and file I/O for saving and loading tasks.

- **test_project.py**: To ensure the reliability and integrity of the application, this file contains unit tests for critical functions in `project.py`. These tests confirm that the application performs as expected and that new changes won't disrupt its functionality.

## Getting Started
**Explore the Features:**
- Add tasks by selecting option 2 and entering your task.
- Update tasks by choosing option 3 and following the prompts.
- Delete tasks by selecting option 4 and specifying the task to remove.
- Save and load your task list automatically.

## Design Choices

- **Command-Line Interface**: The To-Do List Application employs a command-line interface to provide a lightweight, easily accessible solution. This design choice ensures quick task management without the need for a graphical user interface.

- **Storage in a Text File**: To guarantee the persistence of tasks, the application stores them in a text file (`tasks.txt`). This approach allows users to continue their task list even after restarting the program.

- **Pytest for Testing**: We have chosen the `pytest` library for testing the application's functions. This decision offers a robust framework for verifying the code's correctness and maintaining its integrity.

- **User-Friendly Menu**: The menu presents a list of numbered options, simplifying the user experience by making it intuitive to choose actions.

- **Task Indexing**: Tasks are indexed starting from 1 for a user-friendly approach to task management.


