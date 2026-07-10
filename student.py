from person import person




class student(person):
    def __init__(self,roll_no,course,semester,attendance):
        super().__init__()
        self.roll_no = roll_no
        self.course = course
        self.semester = semester
        self._marks = None
        self.attendance = attendance

    def login(self):
        pass
    def logout(self):
        pass
    def display(self):
        pass
    def view_result(self):
        pass
    def calculate_percentage(self):
        pass
    def pay_fee(self):
        pass
   