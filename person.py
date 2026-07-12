from abc import ABC, abstractmethod
from log_database import persons

class person(ABC):
    def __init__(self,person_id,name,age,gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self._mobile = None
    
    @abstractmethod
    def login(self):
        if self.person_id in persons:
            self.display()

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def display(self):
        pass