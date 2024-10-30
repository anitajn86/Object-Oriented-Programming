class Voter:
    def __init__(self,voter_id:str, name:str, age:int, gender:bool, location:str, VotingStatus:bool):
        self.__voter_id = voter_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__location = location
        self.__VotingStatus = VotingStatus

    def getID(self):
        return self.__voter_id
    def setID(self, voter_id:str):
        self.__voter_id = voter_id
    
    def getname(self):
        return self.__name
    def setname(self, name:str):
        self.__name = name
    
    def getage(self):
        return self.__age
    def setage(self, age:int):
        self.__age = age  
    
    def getGender(self):
        return self.__gender
    def setGender(self, gender:bool):
        self.__gender = gender  
    
    def getLocation(self):
        return self.__location
    def setLocation(self, location:str):
        self.__location =location  
    
    def get_VotingStatus(self):
        return self.__VotingStatus
    def set_VotingStatus(self,VotingStatus):
        self.__VotingStatus =VotingStatus
    
    def register_voter(self):
        print(f"The Voter {self.__name}, ID {self.__voter_id} is now registered to vote")  

    def vote(self):
        if self.__VotingStatus:
            print("This voter has not yet voted")
        else:
            print("This voter has voted")

V1=Voter("u001","Anita",27,1,"Entebbe",False)
print(V1.getLocation())
V1.setLocation("Mukono")
print(V1.setLocation())
print(V1.get_VotingStatus())

