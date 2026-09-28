from database import STUDENTS_FILE, read_lines, append_line
from validators import valid_student_id, valid_name, valid_roll_number

def add_student():
    student_id = input("Enter student ID: ").strip()
    if not valid_student_id(student_id):
        print("Student ID cannot be empty.")
        return

    for line in read_lines(STUDENTS_FILE):
        if line.split("|")[0] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()
    department = input("Enter department: ").strip()

    if not valid_name(name) or not valid_roll_number(roll_number):
        print("Name and roll number cannot be empty.")
        return

    append_line(STUDENTS_FILE, f"{student_id}|{name}|{roll_number}|{department}")
    print("Student added successfully.")

def view_students():
    students = read_lines(STUDENTS_FILE)
    if not students:
        print("No students found.")
        return
    print("\n----- Student List -----")
    for line in students:
        student_id, name, roll_number, department = line.split("|")
        print(f"ID: {student_id} | Name: {name} | Roll No: {roll_number} | Department: {department}")

def search_student():
    keyword = input("Enter student ID, name, or roll number: ").strip().lower()
    if not keyword:
        print("Search value cannot be empty.")
        return

    found = False
    for line in read_lines(STUDENTS_FILE):
        student_id, name, roll_number, department = line.split("|")
        if keyword in student_id.lower() or keyword in name.lower() or keyword in roll_number.lower():
            print(f"ID: {student_id} | Name: {name} | Roll No: {roll_number} | Department: {department}")
            found = True
    if not found:
        print("No matching student found.")
