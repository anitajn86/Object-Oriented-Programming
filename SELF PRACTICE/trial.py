class Person:
    def __init__(self,name,age,gender):
        self._name = name
        self._age = age
        self._gender = gender

class Employee(Person):
    def __init__(self,name,age,gender,employee_id,department):
        super().__init__(name,age,gender)
        self._employee_id = employee_id
        self._department = department

    def assign_task(self,task):
        self.task=task
        return f"{self._name} has been assigned to {self.task}"
    def display_info(self):
        return f"name: {self._name}, age: {self._age}, gender:{self._gender}, employee_id: {self._employee_id}, department: {self._department}"
emp1=Employee('Anita',5,"Female",54,"student")
print(emp1.assign_task("dataScience"))
print(emp1.display_info())



    
        