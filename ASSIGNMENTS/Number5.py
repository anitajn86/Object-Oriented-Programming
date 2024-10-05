class MemberException(Exception):
    pass

class StudentManagement:
    def __init__(self):
        self.students=[]


class Student:
    def __init__(self,name,course,registrationNumber):
        self.name=name
        self.course=course
        self.registrationNumber=registrationNumber
        print(f"{self.name},{self.registrationNumber} does {self.course}")

    def addStudent(self,student):
        try:
            student in self.students
            self.student=self.student.append(student)
            print(f"Student {student} has been added to student management")
        except MemberException as error:
            print(f"Student is already in system \n {error}")

    # def deleteStudent(self,student):
    #     try:
    #         student in self.student
    #         self.student=self.student.pop(student)



    
