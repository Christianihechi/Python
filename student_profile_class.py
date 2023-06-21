class Student:
    """Student's information and grade calculator"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0

        total = sum(self.grades)
        average = total / len(self.grades)
        return average

    def display_info(self):
        print("--- Student Information ---")
        print(f"Name: {self.name.title()}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average()}")
