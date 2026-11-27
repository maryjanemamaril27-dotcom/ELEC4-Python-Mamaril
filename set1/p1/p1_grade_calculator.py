# Name: Mary Jane DG. Mamaril
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 18 2026

grades = []

print("================================")
print("Student: Mary Jane DG. Mamaril")
print("Section: IV-BSIT C")
print("================================")


def input_grades():
    global grades
    grades = []

    while True:
        try:
            count = int(input("How many grades would you like to enter? "))

            if count <= 0:
                print("Please enter a positive number.")
                continue

            break

        except ValueError:
            print("Invalid input. Enter a number only.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade #{i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid grade. Please enter a number.")


def calculate_average(student_grades):
    return sum(student_grades) / len(student_grades)


def get_highest_grade(student_grades):
    return max(student_grades)


def get_lowest_grade(student_grades):
    return min(student_grades)


def determine_status(student_grades):
    average = calculate_average(student_grades)

    if average >= 75:
        return "PASS"
    else:
        return "FAIL"


def display_results():
    if len(grades) == 0:
        print("\nNo grades entered yet.\n")
        return

    print("\n===== STUDENT GRADE REPORT =====")
    print(f"Average Grade : {calculate_average(grades):.2f}")
    print(f"Highest Grade : {get_highest_grade(grades)}")
    print(f"Lowest Grade  : {get_lowest_grade(grades)}")
    print(f"Status        : {determine_status(grades)}")
    print("===============================\n")


def main():
    while True:
        print("===== MENU =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_grades()

        elif choice == "2":
            display_results()

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid menu choice.\n")


main()

"""
LOCAL VS GLOBAL VARIABLES

A local variable exists only inside the function where it is created.
It cannot be accessed outside that function. In this program,
variables such as average inside determine_status() are local variables.

A global variable can be accessed throughout the program.
The grades list is a global variable because it is declared outside
all functions and is used by multiple functions.
"""
