from employee_class import Employee


def main():
    employee = None  # Initialize the employee variable outside the loop
    while True:
        print()
        print("Hi, What would you like to do?\n")
        print(" 1. Enter employee's Information")
        print(" 2. Update employee's Salary")
        print(" 3. Update employee's position")
        print(" 4. View employee's Information")
        print()
        prompt = input("Please type 1, 2, 3 or 4 according to your choice: ")

        if prompt == '1':
            name = input("Enter your employee's full name: ")
            position = input("Enter employee's position: ")
            salary = int(input("Enter salary of employee: "))

            employee = Employee(name, position, salary)

        elif prompt == '2':
            if employee is None:
                print("Employee information not entered yet. Please enter employee information first.")
                continue

            new_salary = int(input("Please enter the new salary for the employee: "))
            employee.salary_raise(new_salary)

        elif prompt == '3':
            if employee is None:
                print("Employee information not entered yet. Please enter employee information first.")
                continue

            new_position = input("Please enter the new position for the employee: ")
            employee.update_position(new_position)

        elif prompt == '4':
            if employee is None:
                print("Employee information not entered yet. Please enter employee information first.")
                continue
            employee.employee_info()

        else:
            print("No Employee data currently saved, please select the right option.")


if __name__ == '__main__':
    main()
