from students import add_student, view_students, search_student
from attendance import mark_attendance, view_attendance
from reports import attendance_report

def print_menu():
    print("\n===== Student Attendance Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Mark Attendance")
    print("5. View Attendance")
    print("6. Attendance Report")
    print("7. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            mark_attendance()
        elif choice == "5":
            view_attendance()
        elif choice == "6":
            attendance_report()
        elif choice == "7":
            print("Thank you for using the Student Attendance Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
