# 🕒 Time Tracker App

This is a Python app for tracking time spent on different projects. It provides a graphical user interface (GUI) built with Tkinter and stores project data in an SQLite database.

## Features
- ✅ **Project Selection:** Choose a project from the list of available projects.
- ⏱️ **Start and Stop Timer:** Track time spent on each project by starting and stopping timers.
- **Elapsed Time Display:** View the elapsed time for each project in the format HH:MM:SS.
- **Add New Projects:** Easily add new projects directly from the app.
- **Reset for a New Week:** Start a new week and reset project times to zero, preserving historic data.
- **Display Database Data:** View project data in a tabular format.

## How to Use
1. Run `main.py` to start the app.
2. Select a project from the dropdown list.
3. Click the "Start" button to initiate the timer.
4. Click the "Stop" button to pause the timer.
5. The elapsed time for the selected project is displayed on the screen.
6. To add a new project, click the "Add Project" button, enter the project name, and click "Add."
7. To start a new week and reset project times, click the "Start New Week" button.
8. To view all project data in a table, click the "Display Database" button.

## Dependencies
The Time Tracker App relies on the following dependencies:
- 🐍 **Python 3.x:** The core programming language used.
- **Tkinter:** The standard Python interface to the Tk GUI toolkit, used for building the graphical user interface.
- **SQLite3:** A built-in Python library for interacting with SQLite databases, used for data storage.
- **Datetime Module:** Used for handling date and time operations.
- 📊 **Matplotlib:** A library for creating data visualizations, used for creating project time histograms.
- 🐼 **Pandas:** A library for data manipulation and analysis, used for displaying project data in tables.

## Installation
1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required dependencies if not already installed (Tkinter, SQLite3, Matplotlib, and Pandas).

## License
This project is licensed under the MIT License.

**Author:** Giovanni De Franceschi
