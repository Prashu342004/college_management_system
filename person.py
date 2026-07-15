from abc import ABC, abstractmethod
import os
from prettytable import PrettyTable
class person(ABC):
    def __init__(self,person_id,name,mobile,age,gender,password):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.password = password

    @staticmethod
    def clear_display():
        os.system("cls")

    @staticmethod
    def hold_screen():
        input(" press enter to continue.....  ")

    def view_student(self):
        from log_database import students
        if len(students) == 0:
            print("No data exist")
        else:
            table = PrettyTable(["person_id","name","mobile","age","gender","roll_no","course","semester","attendance","password","marks","fees_paid"])
            for s in students:
                table.add_row([s.person_id,s.name,s.mobile,s.age,s.gender,s.roll_no,s.course,s.semester,s.attendance,s.password,s.marks,s.fees_paid])
            print(table)

    def view_teacher(self):
        from log_database import teachers
        if len(teachers) == 0:
            print("No data exist")
        else:
            table = PrettyTable(["person_id","name","mobile","age","gender","employee_id","subject","password","salary"])
            for s in teachers:
                table.add_row([s.person_id,s.name,s.mobile,s.age,s.gender,s.employee_id,s.subject,s.password,s.salary])
            print(table)
    
    @staticmethod
    def num_validity(mobile):
        if len(str(mobile)) != 10:
            raise ValueError("mobile number not valid")
        return mobile
            
    @classmethod   
    @abstractmethod
    def login(cls):
        cls.clear_display()
        print("Please enter login details")
        username = str(input("enter username :  "))
        password = str(input("Enter password :  "))
        return username, password
    
    def logout(self):
        pass
    
    @abstractmethod
    def display(self):
        self.clear_display()
        print("personal details :")
        print(f"{self.name}'s personal id   : {self.person_id}")
        print(f"{self.name}'s name          : {self.name}")
        print(f"{self.name}'s mobile number : {self.mobile}")
        print(f"{self.name}'s age           : {self.age}")
        print(f"{self.name}'s gender        : {self.gender}")
    
    
    
    