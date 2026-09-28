from database import STUDENTS_FILE, ATTENDANCE_FILE, read_lines

def attendance_report():
    students = read_lines(STUDENTS_FILE)
    records = read_lines(ATTENDANCE_FILE)

    if not students:
        print("No students found.")
        return

    print("\n===== Attendance Report =====")
    print(f"Total Students: {len(students)}")
    print(f"Total Attendance Records: {len(records)}")

    present = sum(1 for line in records if line.split("|")[2] == "Present")
    absent = sum(1 for line in records if line.split("|")[2] == "Absent")
    print(f"Present Records: {present}")
    print(f"Absent Records: {absent}")

    print("\n----- Student-wise Attendance -----")
    for student in students:
        student_id, name, roll_number, department = student.split("|")
        student_records = [r for r in records if r.split("|")[0] == student_id]
        present_count = sum(1 for r in student_records if r.split("|")[2] == "Present")
        total = len(student_records)
        if total:
            percentage = (present_count / total) * 100
            print(f"{student_id} | {name} | Present: {present_count}/{total} | Attendance: {percentage:.1f}%")
        else:
            print(f"{student_id} | {name} | No attendance recorded")
