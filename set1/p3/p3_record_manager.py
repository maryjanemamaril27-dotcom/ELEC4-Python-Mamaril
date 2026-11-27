# ==========================================
# Name: Mary Jane DG. Mamaril
# Section: IV-BSIT
# Activity Code: P3
# Date: November 18, 2026
# ==========================================


print("================================")
print("Student: Mary Jane DG. Mamaril")
print("Section: IV-BSIT C")
print("================================")


students = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    for student in students:
        if student.lower() == name.lower():
            print("Student already exists.")
            return

    students.append(name)
    print("Student added successfully.")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed successfully.")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    found_students = []

    for student in students:
        if keyword in student.lower():
            found_students.append(student)

    if found_students:
        print("\nSearch Results:")
        for student in found_students:
            print(student)
    else:
        print("No matching student found.")


def display_students():
    if len(students) == 0:
        print("No students recorded.")
        return

    print("\n===== STUDENT LIST =====")

    sorted_students = sorted(students)

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    print(f"\nTotal Students: {len(students)}")


while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")


"""
LIST VS SET

A list stores items in order and allows duplicates.
A set stores unique items and automatically removes duplicates.
In this program, a list is used because we want to display
students alphabetically and maintain manageable records.
Duplicate checking is done manually before adding a new student.
"""
