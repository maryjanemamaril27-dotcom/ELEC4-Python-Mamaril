# ==========================================
# Name: Mary Jane DG. Mamaril
# Section: IV-BSIT
# Activity Code: P2
# File: student_utils.py
# ==========================================


print("================================")
print("Student: Mary Jane DG. Mamaril")
print("Section: IV-BSIT C")
print("================================")


def calculate_average(grades):
    return sum(grades) / len(grades)


def is_passed(grades):
    return calculate_average(grades) >= 75


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


if __name__ == "__main__":
    print("student_utils module loaded.")
