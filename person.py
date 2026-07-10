from abc import ABC, abstractmethod


class person(ABC):
    def __init__(self,person_id,name,age,gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self._mobile = None
    

    def login(self):
        pass
    def logout(self):
        pass

    @abstractmethod
    def display():
        pass