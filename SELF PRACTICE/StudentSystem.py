class MemberException(Exception):
    pass

class Student:
    def __init__(self, name, course, registrationNumber):
        self.name = name
        self.course = course
        self.registrationNumber = registrationNumber
        print(f"{self.name} ({self.registrationNumber}) is enrolled in {self.course}.")

class StudentManagement:
    def __init__(self):
        self.students=[]

    def viableStudent(self,student):
        if student in self.students:
            return
        else:
            raise MemberException(f"Student {student} is already in the system.")
        
    def addStudent(self,student):
        try:
            self.viableStudent(student)
            self.students.append(student)
            print(f" {student} has been added to the system")
        except MemberException as error:
            print(f"The student is already in the system. \n {error}")




management=StudentManagement()
s1=Student("Anita","BSDS","DS001")
s2 = Student("Alice", "Computer Science", "CS001")
s3 = Student("Bob", "Mathematics", "MATH002")

management.addStudent(s1)
# management.addStudent(s2)