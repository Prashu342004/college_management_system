import admin
import student
from teacher import teacher
import log_database
run_once = True
a101 = admin.admin("a101","shubh")
log_database.admin_user.append(a101)
log_database.load_teachers()
log_database.load_students()

def role_selection():
    while True:
        print("Select Role")
        print()
        print("1. student")
        print("2. teacher")
        print("3. Admin ")
        print("4. Principal")
        print("5. Back")
        
        role_choice = int(input("Enter your choice : "))

        if role_choice == 1:
            student.student.login()
        elif role_choice == 2:
            teacher.login()
        elif role_choice == 3:
            admin.admin.login()
            break
        elif role_choice == 4:
            pass
        elif role_choice == 5:
            break
        else:
            print("incorrect choice")

def main_menu():
    flag_inner = True
    while flag_inner:
        try:
            print("""
        
        Main Dashboard : College Management System

        choose your option :

        1. login
        2. exit
        """)
            choice = int(input("         : "))
            if choice == 1:
                role_selection()
            else:
                flag_inner = False
        except ValueError:
            print("enter numeric value")
        except Exception as e:
            print("something went wrong")
            print(f"The exact error is: {e}")


if run_once == True:
    run_once = False
    main_menu()

log_database.save_students()
log_database.save_teachers()