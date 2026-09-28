from datetime import date
from database import STUDENTS_FILE, ATTENDANCE_FILE, read_lines, append_line
from validators import valid_attendance_status

def student_exists(student_id):
    return any(line.split("|")[0] == student_id for line in read_lines(STUDENTS_FILE))

def mark_attendance():
    student_id = input("Enter student ID: ").strip()
    if not student_exists(student_id):
        print("Student ID not found. Add the student first.")
        return

    attendance_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not attendance_date:
        attendance_date = str(date.today())

    status = input("Enter attendance status (Present/Absent): ").strip().title()
    if not valid_attendance_status(status):
        print("Invalid status. Use Present or Absent.")
        return

    for line in read_lines(ATTENDANCE_FILE):
        old_id, old_date, _ = line.split("|")
        if old_id == student_id and old_date == attendance_date:
            print("Attendance for this student and date is already recorded.")
            return

    append_line(ATTENDANCE_FILE, f"{student_id}|{attendance_date}|{status}")
    print("Attendance marked successfully.")

def view_attendance():
    records = read_lines(ATTENDANCE_FILE)
    if not records:
        print("No attendance records found.")
        return
    print("\n----- Attendance Records -----")
    for line in records:
        student_id, attendance_date, status = line.split("|")
        print(f"Student ID: {student_id} | Date: {attendance_date} | Status: {status}")
