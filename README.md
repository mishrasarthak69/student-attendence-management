
# Student Attendance Management System

A simple terminal-based Python project for storing student details, marking attendance, viewing attendance records, searching students, and generating attendance reports.

## Features

- Add Student
- View Students
- Search Student by ID, name, or roll number
- Mark Present/Absent attendance
- View attendance records
- Generate student-wise attendance percentages
- Prevent duplicate student IDs
- Prevent duplicate attendance for the same student and date
- Store data locally in `.txt` files

## Technologies

- Python 3
- Python standard library
- Local text-file storage
- Command-line interface

No external packages, databases, or internet connection are required.

## Project Structure

```text
student_attendance_management/
├── data/
│   ├── students.txt
│   └── attendance.txt
├── attendance.py
├── database.py
├── main.py
├── reports.py
├── students.py
├── validators.py
├── requirements.txt
├── statement.md
├── README.md
└── .gitignore
```

## File Description

| File | Purpose |
|---|---|
| `main.py` | Main terminal menu and program entry point |
| `students.py` | Student add, view and search operations |
| `attendance.py` | Attendance marking and viewing |
| `database.py` | Local text-file storage |
| `reports.py` | Attendance statistics and reports |
| `validators.py` | Basic input validation |
| `data/students.txt` | Student records |
| `data/attendance.txt` | Attendance records |

## Requirements

- Python 3.x
- VS Code or any terminal
- No external dependencies

## How to Run

Open the project folder in VS Code and open a terminal.

Check Python:

```bash
python --version
```

Run the project:

```bash
python main.py
```

## Main Menu

```text
===== Student Attendance Management System =====
1. Add Student
2. View Students
3. Search Student
4. Mark Attendance
5. View Attendance
6. Attendance Report
7. Exit
```

## Data Format

Student records:

```text
student_id|name|roll_number|department
```

Attendance records:

```text
student_id|date|status
```

Example:

```text
ST101|Aarav Sharma|01|CSE
ST101|2026-09-27|Present
```

## Testing

Test the application by:

1. Adding a valid student.
2. Trying a duplicate student ID.
3. Viewing students.
4. Searching for a student.
5. Marking Present attendance.
6. Marking Absent attendance.
7. Trying an unknown student ID.
8. Trying duplicate attendance for the same date.
9. Viewing attendance.
10. Generating the attendance report.
11. Exiting the program.

## Limitations

This is a simple academic command-line project. It does not include authentication, a web/mobile interface, cloud storage, biometric attendance, external databases, or notifications.

## Future Enhancements

- Student/faculty login
- Subject-wise attendance
- Monthly reports
- Attendance percentage warnings
- SQLite database
- GUI or web interface
- CSV export
- Notifications

## Author

**Divyansh Chandra**

Python Essentials — VITyarthi Project

## Run Command

```bash
python main.py
```
