from person import person


class teacher(person):
    def __init__(self,employee_id,subject):
        super().__init__()
        self.employee_id = employee_id
        self.subject = subject
        self.__salary = None
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary > 0:
            self.__salary = salary

    def login(self):
        pass
    def logout(self):
        pass
    def display(self):
        pass
    def add_marks(self):
        pass
    def update_marks(self):
        pass
    def take_attendance(self):
        pass

