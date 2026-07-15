from person import person
from college_file import sports, cultural

class student(person,sports,cultural):
    def __init__(self,person_id,name,mobile,age,gender,roll_no,course,semester,attendance,password,fees_paid):
        super().__init__(person_id,name,mobile,age,gender,password)
        self.roll_no = roll_no
        self.course = course
        self.semester = semester
        self.__marks = {}
        self.attendance = attendance
        self.password = password
        self.fees_paid = fees_paid
    
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
            self.clear_display()
            print("Enter choice")
            print("1. view profile")
            print("2. view result")
            print("3. calculate_percentage")
            print("4. pay_fee ")
            print("5. perform dance")
            print("6. play sports")
            print("7. logout")
            
            student_choice = input("enter your choice : ")
            if student_choice == "1":
                self.display()
                self.hold_screen()
            elif student_choice == "2":
                self.clear_display()
                self.view_result()
                self.hold_screen()
            elif student_choice == "3":
                self.clear_display()
                self.calculate_percentage()
                self.hold_screen()
            elif student_choice == "4":
                self.clear_display()
                self.pay_fee()
                self.hold_screen()
            elif student_choice == "5":
                self.clear_display()
                self.perform_dance()
                self.hold_screen()
            elif student_choice == "6":
                self.clear_display()
                self.play_sport()
                self.hold_screen()
            elif student_choice == "7":
                self.logout()
                break
            else:
                print("invalid choice, Please retry....")
                self.hold_screen()


    def view_result(self):
        print(f" {self.name}'s result :")
        for subject , mark in self.marks.items():
            print(f"subject = {subject}   marks = {mark}")

    def calculate_percentage(self):
        subject_count ,subject_total_marks = 0,0
        for mark in self.marks.values():
            subject_total_marks += int(mark)
            subject_count +=1
        print("percentage is : ",subject_total_marks/subject_count)


    def pay_fee(self):
        from college_file import college
        self.college = college(self.fees_paid)
        self.fees_paid =self.college.pay_fee()


