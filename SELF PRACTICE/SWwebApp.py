from abc import ABC, abstractmethod

class User:
    def __init__(self,username,password):
        self._username=username
        self._password=password
        self._admins=[]
        self._guests=[]

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @abstractmethod
    def login(self):
        pass

class AdminUser(User):
    def __init__(self,username,password,employeeID):
        super().__init__(username,password)
        self._employeeID=employeeID

    def is_employee(self,admin):
        if isinstance(admin,AdminUser):
            self._admins.append(admin)
            print(f"{self._username} is an instance of the admin class hence added to the list of admins")
        else:
            print(f"{self._username} is not an instance of the class")

    def login(self,username,password,employeeID): #polymorphism and abstraction 
        if self.is_employee():
            self._username==username
            self._password==password
            self._employeeID==employeeID
            print(f"{self._username} with {self._employeeID} is logged in")

class GuestUser(User): #inheritance
    def __init__(self,username,password):
        super().__init__(username,password)

    # def is_guest(self,guest):
    #     if isinstance(guest,GuestUser):
    #         self._guests.append(guest)
    #         print(f"{self._username} is an instance of the guest class hence added to the list of guests")
    #     else:
    #         print(f"{self._username} is not an instance of the class")    

    def login(self,username,password): #polymorphism and abstraction
        if self._username==username and self._password==password:
            print(f"{self._username} has logged in.")
        else:
            print(f"Invalid username and or password")