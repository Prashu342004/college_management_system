from person import person


class student(person):
    def __init__(self,person_id,name,mobile,age,gender,roll_no,course,semester,attendance,password):
        super().__init__(person_id,name,mobile,age,gender,password)
        self.roll_no = roll_no
        self.course = course
        self.semester = semester
        self.__marks = {}
        self.attendance = attendance
        self.password = password
    
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,all_marks):
        for subject,marks in all_marks.items():
            self.__marks[subject] = marks

    @classmethod
    def login(cls):
        from log_database import students
        username , password = super().login()
        for i in students:
            if i.person_id == username and i.password == password:
                i.dashboard()
                break
        else:
            print("No user found")
    

    def display(self):
        super().display()
        print(f"{self.name}'s roll number   : {self.roll_no}")
        print(f"{self.name}'s course        : {self.course}")
        print(f"{self.name}'s marks        : {self.marks}")
    
    def dashboard(self):
        flag = True
        while flag:
            print("Enter choice")
            print("1. view profile")
            print("2. view result")
            print("3. calculate_percentage")
            print("4. pay_fee ")
            print("5. back")
            
            student_choice = int(input("enter your choice : "))
            if student_choice == 1:
                self.display()
            elif student_choice == 2:
                pass
            elif student_choice == 3:
                pass
            elif student_choice == 4:
                pass
            elif student_choice == 5:
                self.logout()
                break
            else:
                print("invalid choice, Please retry....")


    def view_result(self):
        pass
    def calculate_percentage(self):
        pass
    def pay_fee(self):
        pass

