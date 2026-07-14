from abc import ABC, abstractmethod
from log_database import persons

class person(ABC):
    def __init__(self,person_id,name,age,gender,password):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self._mobile = None
        self.password = password
    
    @abstractmethod
    def login(self):
        if self.person_id in persons:
            self.display()


    @abstractmethod
    def display(self):
        pass