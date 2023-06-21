from student_profile_class import Student

name = input("What is your name: ")
age = int(input("What is your age: "))

# Linking the variables to the class
student = Student(name, age)

num_grade = int(input("How many grades do you wish to add: "))
for i in range(num_grade):
    grade = float(input(f"Enter grade #{i+1}: "))
    student.add_grade(grade)

# Display student information
student.display_info()
