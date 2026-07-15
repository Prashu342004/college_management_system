

class InvalidAgeError(Exception):
    pass

class InvalidMarksError(Exception):  # have to use it in teacher class where i will add marks to the student
    pass

class StudentNotFoundError(Exception):  # have to use it in search in teacher class 
    pass

class DuplicateRollNumberError(Exception):
    def __init__(self,roll_no):
        self.roll_no = roll_no
        message = f"roll number : {roll_no} ---  already exist"
        super().__init__(f"{message}")

class DuplicatePersonIdError(Exception):
    def __init__(self,person_id):
        self.roll_no = person_id
        message = f"person id : {person_id} ---  already exist"
        super().__init__(f"{message}")
        