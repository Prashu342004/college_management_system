from person import person
from student import student

class teacher(person):
    def __init__(self,person_id,name,mobile,age,gender,employee_id,subject,password):
        super().__init__(person_id,name,mobile,age,gender,password)
        self.employee_id = employee_id
        self.subject = subject
        self.__salary = None
        self.password = password

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,salary):
        if int(salary) > 0:
            self.__salary = salary

    @classmethod
    def login(cls):
        from log_database import teachers
        username , password = super().login()
        for i in teachers:
            if i.person_id == username and i.password == password:
                i.dashboard()
                break
        else:
            print("No user found")

    def display(self):
        super().display()
        print(f"{self.name}'s employee id   : {self.employee_id}")
        print(f"{self.name}'s subject       : {self.subject}")
        print(f"{self.name}'s salary        : {self.salary}")
    
    def dashboard(self):
        flag = True
        while flag:
            self.clear_display()
            print("option's available : ")
            print("1. view user details")
            print("2. add marks")
            print("3. update marks")
            # print("4. take attendance")
            print("5. search student")
            print("6. view students")
            print("7. logout")
            teacher_choice = input("enter your choice : ")
            if teacher_choice == "1":
                self.display()
                self.hold_screen()
            elif teacher_choice == "2":
                self.add_marks()
                self.hold_screen()
            elif teacher_choice == "3":
                self.update_marks()
                self.hold_screen()
            elif teacher_choice == "4":
                pass                            # Here code is not completed
            elif teacher_choice == "5":
                obj = self.search_student()
                print(obj.display())
                self.hold_screen()
            elif teacher_choice == "6":
                self.clear_display()
                self.view_student()
            elif teacher_choice == "7":
                self.logout()
                flag = False
            else:
                print("enter valid input")
    
    def search_student(self):
        from log_database import students
        self.clear_display()
        no = input("enter student roll number : ")
        for i in students:
            if i.roll_no == no:
                return i
        else:
            print("student not found")
            return 0

    def add_marks(self):
        from custom_exceptions import InvalidMarksError
        self.clear_display()
        student_object = self.search_student()
        while True:
            try:
                marks = input("enter new marks")
                if marks < 1:
                    raise InvalidMarksError
                else:
                    break
            except InvalidMarksError as e:
                print(f"error occur is : {e}")
        student_object.marks = {self.subject:marks}


    def update_marks(self):
        from custom_exceptions import InvalidMarksError
        self.clear_display()
        student_object = self.search_student()
        if self.subject in student_object.marks.keys():
            while True:
                try:
                    marks = int(input("enter updated marks"))
                    if marks < 1:
                        raise InvalidMarksError
                    else:
                        break
                except InvalidMarksError as e:
                    print(f"error occur is : {e}")
            student_object.marks = {self.subject:marks}
        else:
            print("cannot update marks which does not exist")
    
    

    def take_attendance(self):
        pass

