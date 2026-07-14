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
            print("option's available : ")
            print("1. view user details")
            print("2. add marks")
            print("3. update marks")
            print("4. take attendance")
            print("5. search student")
            print("6. To go back")
            teacher_choice = input("enter your choice : ")
            if teacher_choice == "1":
                self.display()
            elif teacher_choice == "2":
                self.add_marks()
            elif teacher_choice == "3":
                self.update_marks()
            elif teacher_choice == "4":
                pass
            elif teacher_choice == "5":
                self.search_student()
            elif teacher_choice == "6":
                flag = False
            else:
                print("enter valid input")
    
    def search_student(self):
        from log_database import students
        no = input("enter student roll number : ")
        for i in students:
            if i.roll_no == no:
                return i
        else:
            print("student not found")

    def add_marks(self):
        student_object = self.search_student()
        marks = input("enter new marks")
        student_object.marks = {self.subject:marks}


    def update_marks(self):
        student_object = self.search_student()
        if self.subject in student_object.marks.keys():
            marks = print("enter updated marks")
            student_object.marks = self.subject,marks
        else:
            print("student marks is not added, please add first")
    
    

    def take_attendance(self):
        pass

