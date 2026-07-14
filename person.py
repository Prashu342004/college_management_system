from abc import ABC, abstractmethod

class person(ABC):
    def __init__(self,person_id,name,mobile,age,gender,password):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.password = password
    
    @staticmethod
    def num_validity(mobile):
        if len(str(mobile)) != 10:
            raise ValueError("mobile number not valid")
        return mobile
            
    @classmethod   
    @abstractmethod
    def login(cls):
        print("Please enter login details")
        username = str(input("enter username :  "))
        password = str(input("Enter password :  "))
        return username, password
    
    def logout(self):
        pass
    
    @abstractmethod
    def display(self):
        
        print("personal details :")
        print(f"{self.name}'s personal id   : {self.person_id}")
        print(f"{self.name}'s name          : {self.name}")
        print(f"{self.name}'s mobile number : {self.mobile}")
        print(f"{self.name}'s age           : {self.age}")
        print(f"{self.name}'s gender        : {self.gender}")