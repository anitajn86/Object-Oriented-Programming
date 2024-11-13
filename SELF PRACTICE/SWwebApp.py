from abc import ABC, abstractmethod

class User:
    def __init__(self,username,password):
        self._username=username
        self._password=password
        self._admins=[]
        self._normals=[]

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @abstractmethod
    def login(self):
        pass

    def viewPages(self):
        return "The pages are available for viewing"

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
        else:
            raise ValueError("Invalid credentials")

    def viewPages(self):
        if self.login():
            print("This employee can view the webpages")
        else:
            super().viewPages()

    def editContent(self):
        allowed_employeeIDs=[1,2,3,4,5,20]
        if self._employeeID in allowed_employeeIDs:
            print("This employee can edit the content on our pages")
        else:
            return super().viewPages 


class NormalUser(User): #inheritance
    def __init__(self,username,password):
        super().__init__(username,password)

    def is_normal(self,normal):
        if isinstance(normal,NormalUser):
            self._normals.append(normal)
            print(f"{self._username} is an instance of the normal class hence added to the list of normals")
        else:
            print(f"{self._username} is not an instance of the class")    

    def login(self,username,password): #polymorphism and abstraction
        if self._username==username and self._password==password:
            print(f"{self._username} has logged in.")
        else:
            print(f"Invalid username and or password")

    def viewPages(self):
        if self.login():
            print("This user is viewing or can view the pages of the app")
        else:
            super().viewPages()
            
class GuestUser:
    def __init__(self,email,username): #these are the guest user's google credentials
        self._email=email
        self._username=username

    def viewPages
        

# class Operations:
#     def __init__(self, guest,admin):
#         if not isinstance(guest,GuestUser) and not isinstance(admin,AdminUser):
#             raise ValueError("These are not instances of their respective classes")
#         self._guest=guest
#         self._admin=admin
