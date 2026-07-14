from person import person
from student import student
from teacher import teacher

class admin(person):
    def __init__(self, person_id,password):
        self.person_id = person_id
        self.password = password

    def add_student(self):
        from log_database import students
        person_id = str(input("enter person's id : "))
        name = input("enter person's name : ")
        age = int(input("enter person's age : "))
        gender = input("enter person's gender : ")
        roll_no = input("enter person's roll no : ")
        course = input("enter person's course : ")
        semester = int(input("enter person's semester : "))
        attendance = int(input("enter person's attendance : "))
        password = input("Enter student password : ")
        obj_name = person_id

        obj_name = student(person_id,name,age,gender,roll_no,course,semester,attendance,password)

        students.append(obj_name)
        print(obj_name)


    def delete_student(self):
        from log_database import students
        flag = True
        while flag:
            try:
                person_id = input("Enter student's person id  :  ")
                for i in students:
                    if person_id == i.person_id:
                        students.remove(i)
                        print("student deleted")
                        flag = False
                        break
                else:
                    print("student not found")
                    continue
            except Exception as e:
                print("something went wrong, try again...")
                print(f"The exact error is: {e}")

        

    def add_teacher(self):
        from log_database import teachers
        person_id = input("enter person's id : ")
        name = input("enter person's name : ")
        age = int(input("enter person's age : "))
        gender = input("enter person's gender : ")
        employee_id = input("enter person's employee id : ")
        subject = input("enter person's subject : ")
        salary = int(input("Enter teacher's salary : "))
        password = input("Enter the password of teacher : ")
        obj_name = employee_id
        obj_name = teacher(person_id,name,age,gender,employee_id,subject,password)
        obj_name.salary = salary
        teachers.append(obj_name)

    def delete_teacher(self):
        from log_database import teachers
        flag = True
        while flag:
            try:
                person_id = input("Enter teacher's person id  :  ")
                for i in teachers:
                    if person_id == i.person_id:
                        teachers.remove(i)
                        print("Teacher deleted")
                        flag = False
                        break
                else:
                    print("teacher not found")
                    continue
            except ValueError:
                print("enter numeric value")
            except Exception:
                print("something went wrong, try again...")
    

    # ----------------------------------used class method here --------------------------------

    @classmethod  
    def login(cls):
        from log_database import admin_user
        while True:
            print("Please enter login details")
            username = input("enter username :  ")
            password = input("Enter password :  ")
            for i in admin_user:
                if i.person_id == username and i.password == password:
                    i.display()
                    break
            else:
                print("No user found")
            break


    def logout(self):
        pass

    def display(self):
    
        while True:
            try:
                print("""
              welcome admin:

              choose option :

              1. Add student
              2. Delete student
              3. Add teacher
              4. Delete teacher
              5. logout
              """)
                choice = int(input(" :  "))
                if choice == 1:
                    self.add_student()
                    continue
                elif choice == 2:
                    self.delete_student()
                    continue
                elif choice == 3:
                    self.add_teacher()
                    continue
                elif choice == 4:
                    self.delete_teacher()
                    continue
                elif choice == 5:
                    self.logout()
                else:
                    print("please enter correct choice")
                break
            except ValueError:
                print("enter numeric value ")
        

