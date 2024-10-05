class MemberException(Exception):
    pass

class StudentManagement:
    def __init__(self):
        # List to store the student objects
        self.students = []

    def addStudent(self, student):
        try:
            # Check if the student is already in the system based on registrationNumber
            if any(stu.registrationNumber == student.registrationNumber for stu in self.students):
                raise MemberException(f"Student with registration number {student.registrationNumber} is already in the system.")
            # Add student if not present
            self.students.append(student)
            print(f"Student {student.name} has been added to the student management system.")
        except MemberException as error:
            print(f"Error: {error}")

    def updateStudent(self, registrationNumber, name=None, course=None):
        try:
            # Find student by registrationNumber
            student = next((stu for stu in self.students if stu.registrationNumber == registrationNumber), None)
            if student is None:
                raise MemberException(f"Student with registration number {registrationNumber} not found.")
            
            # Update student details if provided
            if name:
                student.name = name
            if course:
                student.course = course
            
            print(f"Student {registrationNumber} has been updated.")
        except MemberException as error:
            print(f"Error: {error}")

    def deleteStudent(self, registrationNumber):
        try:
            # Find student by registrationNumber
            student = next((stu for stu in self.students if stu.registrationNumber == registrationNumber), None)
            if student is None:
                raise MemberException(f"Student with registration number {registrationNumber} not found.")
            
            # Remove student from the list
            self.students.remove(student)
            print(f"Student {registrationNumber} has been removed from the system.")
        except MemberException as error:
            print(f"Error: {error}")

class Student:
    def __init__(self, name, course, registrationNumber):
        self.name = name
        self.course = course
        self.registrationNumber = registrationNumber
        print(f"{self.name} ({self.registrationNumber}) is enrolled in {self.course}.")

# Create the management system
management = StudentManagement()

# Create student instances
student1 = Student("Alice", "Computer Science", "CS001")
student2 = Student("Bob", "Mathematics", "MATH002")

# Add students to the management system
management.addStudent(student1)
management.addStudent(student2)

# Try to add the same student again (will raise an exception)
management.addStudent(student1)

# Update a student
management.updateStudent("CS001", name="Alice Smith")

# Delete a student
management.deleteStudent("MATH002")
