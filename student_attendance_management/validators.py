def valid_attendance_status(status):
    return status in {"Present", "Absent"}

def valid_student_id(student_id):
    return student_id.strip() != ""

def valid_name(name):
    return name.strip() != ""

def valid_roll_number(roll_number):
    return roll_number.strip() != ""
