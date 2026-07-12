from person import person
from student import student
from teacher import teacher

class admin(person):
    def add_student(self):
        from log_database import students
        person_id = input("enter person's id : ")
        name = input("enter person's name : ")
        age = int(input("enter person's age : "))
        gender = input("enter person's gender : ")
        roll_no = input("enter person's roll no : ")
        course = input("enter person's course : ")
        semester = int(input("enter person's semester : "))
        attendance = int(input("enter person's attendance : "))

        obj_name = roll_no

        obj_name = student(person_id,name,age,gender,roll_no,course,semester,attendance)

        students.append({person_id:obj_name})
        print(students)
        self.display()


    def delete_student(self,person_id):
        from log_database import students
        while True:
            try:
                input("Enter student's person id  :  ")
                if person_id in students:
                    del student[person_id]
                    break
                else:
                    print("student not found")
                    continue
            except ValueError:
                print("enter numeric value")
            except Exception:
                print("something went wrong, try again...")

        self.display()
        

    def add_teacher(self):
        from log_database import teachers
        teacher_data = {}
        person_id = input("enter person's id : ")
        name = input("enter person's name : ")
        age = int(input("enter person's age : "))
        gender = input("enter person's gender : ")
        employee_id = input("enter person's employee id : ")
        subject = input("enter person's subject : ")
        obj_name = employee_id

        obj_name = teacher(obj_name,person_id,name,age,gender,employee_id,subject)
        teacher_data[person_id] = obj_name
        teachers.append(teacher_data)
        self.display()

    def delete_teacher(self,person_id):
        from log_database import teachers
        while True:
            try:
                input("Enter teacher's person id  :  ")
                if person_id in teachers:
                    del teacher[person_id]
                    break
                else:
                    print("teacher not found")
                    continue
            except ValueError:
                print("enter numeric value")
            except Exception:
                print("something went wrong, try again...")
        self.display()

    def login(self):
        from log_database import admin_user
        while True:
            username = input("enter username :  ")
            password = input("Enter password :  ")
            for i in admin_user:
                if (username,password) in i.items():
                    self.display()
            print("No user found")


    def logout(self):
        import cms
        cms.role_selection()

    def display(self):
        print("""
              welcome admin:

              choose option :

              1. Add student
              2. Delete student
              3. Add teacher
              4. Delete teacher
              5. logout
              """)
        while True:
            try:
                choice = int(input(" :  "))
                break
            except ValueError:
                print("enter numeric value ")
        
        if choice == 1:
            self.add_student()
        elif choice == 2:
            
            self.delete_student()
        elif choice == 3:
            self.add_teacher()
        elif choice == 4:
            self.delete_teacher()
        elif choice == 5:
            self.logout()
        else:
            print("please enter correct choice")
           


