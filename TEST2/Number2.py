# a) Function to add a student to the student list
def add_student(student_list, student_id, name, age, course):
    # Check if student ID is unique
    for student in student_list:
        if student['id'] == student_id:
            print("Error: Student ID already exists.")
            return
    # Add new student to the list
    student_list.append({'id': student_id, 'name': name, 'age': age, 'course': course})

# b) Functions to find and remove a student by ID
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            return student
    print("Error: Student not found.")
    return None

def remove_student_by_id(student_list, student_id):
    for i, student in enumerate(student_list):
        if student['id'] == student_id:
            del student_list[i]
            print("Student removed successfully.")
            return
    print("Error: Student not found.")

# c) Base class Person with subclasses Student and Instructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")

class Instructor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# d) Sorting function for students
def sort_students(student_list, key_function):
    return sorted(student_list, key=key_function)

# Demonstrating functionality
# Creating a sample student list
students = []
add_student(students, 1, "Anita", 21, "Math")
add_student(students, 2, "Ruth", 22, "Physics")
add_student(students, 3, "Jonah", 20, "Biology")

# Finding and removing a student
print(find_student_by_id(students, 2))  # Should print Bob's details
remove_student_by_id(students, 2)       # Should remove Bob
print(find_student_by_id(students, 2))   # Should print error message

# Creating instances of Student and Instructor
Angel = Student("Angel", 31, "Math")
James = Instructor("James", 40, "Physics")

# Demonstrating polymorphism
Angel.study()
James.teach()

# Sorting students by age and name
sorted_by_age = sort_students(students, lambda x: x['age'])
sorted_by_name = sort_students(students, lambda x: x['name'])

print("Sorted by age:", sorted_by_age)
print("Sorted by name:", sorted_by_name)
