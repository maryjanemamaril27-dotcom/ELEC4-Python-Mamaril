# ==========================================
# Name: YOUR NAME
# Section: IV-BSIT
# Activity Code: P2
# File: p2_main.py
# ==========================================

import student_utils
from datetime import datetime

grades = []

while True:
    try:
        count = int(input("How many grades do you want to enter? "))

        if count > 0:
            break

        print("Please enter a positive number.")

    except ValueError:
        print("Invalid input. Enter a whole number.")

for i in range(count):
    while True:
        try:
            grade = float(input(f"Enter grade #{i+1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")

average = student_utils.calculate_average(grades)
highest = student_utils.get_highest_grade(grades)
lowest = student_utils.get_lowest_grade(grades)
passed = student_utils.is_passed(grades)

print("\n===== STUDENT GRADE REPORT =====")
print("Date Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Grades:", grades)
print(f"Average: {average:.2f}")
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)

if passed:
    print("Status: PASSED")
else:
    print("Status: FAILED")
