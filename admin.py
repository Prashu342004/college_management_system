from person import person
from student import student
from teacher import teacher
from custom_exceptions import InvalidAgeError,DuplicateRollNumberError,DuplicatePersonIdError

class admin(person):
    def __init__(self, person_id,password):
        self.person_id = person_id
        self.password = password

    def add_student(self):
        from log_database import students
        while True:
            try:
                person_id = str(input("enter person's id : "))
                for i in students:
                    if person_id == i.person_id:
                        raise DuplicatePersonIdError(person_id)
                else:
                    break
            except DuplicatePersonIdError as e:
                print(f"error is : {e}")
                continue

        while True:
            name = input("enter person's name : ").strip()
            if name != "":
                break
            else:
                continue

        while True:
            try:
                age = int(input("enter person's age : "))
                if age <18 or age >90:
                    raise InvalidAgeError
            except ValueError:
                print("please enter numeric value")   
            except InvalidAgeError as e:
                print(f"error is : {e}")
                continue
            else:
                break
            

        while True:
            try:
                mobile = student.num_validity(int(input("Enter mobile number : ")))
                break
            except Exception:
                print("number not valid ")
        
        gender = input("enter person's gender : ")
        while True:
            try:
                roll_no = input("enter person's roll no : ")
                for i in students:
                    if i.roll_no == roll_no:
                        raise DuplicateRollNumberError(roll_no)
                else:
                    break
            except DuplicateRollNumberError as e:
                print(f"error is : {e}")

        course = input("enter person's course : ")
        semester = input("enter person's semester : ")
        attendance = input("enter person's attendance : ")
        password = input("Enter student password : ")
        while True:
            try:
                fees_paid = int(input("enter the fees paid by the student : "))
                break
            except ValueError:
                print("enter numeric value")

        obj_name = person_id

        obj_name = student(person_id,name,mobile,age,gender,roll_no,course,semester,attendance,password,fees_paid)

        students.append(obj_name)


    def delete_student(self):
        from log_database import students
        flag = True
        count = 0
        while flag:
            count +=1 
            try:
                self.view_student()
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
            if count >2:
                flag = False

        

    def add_teacher(self):
        from log_database import teachers
        while True:
            try:
                person_id = str(input("enter person's id : "))
                for i in teachers:
                    if person_id == i.person_id:
                        raise DuplicatePersonIdError(person_id)
                else:
                    break
            except DuplicatePersonIdError as e:
                print(f"error is : {e}")
        while True:
            name = input("enter person's name : ").strip()
            if name != "":
                break
            else:
                continue

        try:
            mobile = teacher.num_validity(int(input("Enter mobile number : ")))
        except Exception:
            print("number not valid ")

        while True:
            try:
                age = int(input("enter person's age : "))
                if age <18 or age >90:
                    raise InvalidAgeError
                else:
                    break
            except InvalidAgeError as e:
                print(f"error is : {e}")
                continue
            
        
        gender = input("enter person's gender : ")
        employee_id = input("enter person's employee id : ")
        subject = input("enter person's subject : ")
        while True:
            try:
                salary = int(input("Enter teacher's salary : "))
                break
            except Exception as e:
                print(f"error is : {e}")
        password = input("Enter the password of teacher : ")
        obj_name = person_id
        obj_name = teacher(person_id,name,mobile,age,gender,employee_id,subject,password)
        obj_name.salary = salary
        teachers.append(obj_name)

    def delete_teacher(self):
        from log_database import teachers
        flag = True
        count = 0
        while flag:
            count += 1 
            try:
                self.view_teacher()
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
            if count >2:
                flag = False
    

    # ----------------------------------used class method here --------------------------------

    @classmethod  
    def login(cls):
        from log_database import admin_user
        while True:
            cls.clear_display()
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


    def display(self):
    
        while True:
            self.clear_display()
            try:
                print("""
              welcome admin:

              choose option :

              1. Add student
              2. Delete student
              3. Add teacher
              4. Delete teacher
              5. view student 
              6. view teacher
              7. logout
              """)
                choice = input(" :  ")
                if choice == "1":
                    self.clear_display()
                    self.add_student()
                    self.hold_screen()
                    continue
                elif choice == "2":
                    self.delete_student()
                    self.hold_screen()
                    continue
                elif choice == "3":
                    self.add_teacher()
                    continue
                elif choice == "4":
                    self.delete_teacher()
                    self.hold_screen()
                    continue
                elif choice == "5":
                    self.clear_display()
                    self.view_student()
                    self.hold_screen()
                elif choice == "6":
                    self.clear_display()
                    self.view_teacher()
                    self.hold_screen()
                elif choice == "7":
                    self.logout()
                    break
                else:
                    print("please enter correct choice")
                
            except ValueError:
                print("enter numeric value ")
            
        
