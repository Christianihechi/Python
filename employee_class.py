class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def employee_info(self):
        print("--- Employee Information ---\n")
        print(f"Name: {self.name.title()}")
        print(f"Current Position: {self.position.title()}")
        print(f"Salary: {self.salary}")

    def salary_raise(self, new_salary):
        self.salary += new_salary

    def update_position(self, new_position):
        self.position = new_position
