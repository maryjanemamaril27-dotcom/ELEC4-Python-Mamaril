# ==========================================
# Name: Mary Jane DG. Mamaril
# Section: IV-BSIT
# Activity Code: P4
# Date: November 18, 2026
# ==========================================

print("================================")
print("Student: Mary Jane DG. Mamaril")
print("Section: IV-BSIT C")
print("================================")


while True:

    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = num1 / num2

        elif choice == "2":

            filename = input("Enter filename: ")

            with open(filename, "r") as file:
                content = file.read()

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            raise KeyError("Invalid menu selection")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except FileNotFoundError:
        print("Error: File not found.")

    except KeyError:
        print("Error: Invalid menu choice.")

    else:

        if choice == "1":
            print("Result =", result)

        elif choice == "2":
            print("\n===== FILE CONTENT =====")
            print(content)

    finally:
        print("Operation completed.")
