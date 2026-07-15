import admin
import student
from teacher import teacher
import log_database
import os

def clear_display():
        os.system("cls")
def hold_screen():
        input(" press enter to continue.....  ")

run_once = True
a101 = admin.admin("a101","shubh")
log_database.admin_user.append(a101)
clear_display()
log_database.load_teachers()
log_database.load_students()

def role_selection():
    while True:
        clear_display()
        print("Select Role")
        print()
        print("1. student")
        print("2. teacher")
        print("3. Admin ")
        # print("4. Principal")
        print("5. Back")
        
        role_choice = input("Enter your choice : ")

        if role_choice == "1":
            student.student.login()
            hold_screen()
            break
        elif role_choice == "2":
            teacher.login()
            hold_screen()
            break
        elif role_choice == "3":
            admin.admin.login()
            break
        elif role_choice == "4":
            pass
        elif role_choice == "5":
            break
        else:
            print("incorrect choice")

def main_menu():
    flag_inner = True
    while flag_inner:
        clear_display()
        try:
            print("""
        
        Main Dashboard : College Management System

        choose your option :

        1. login
        2. exit
        """)
            choice = input("         : ")
            if choice == "1":
                role_selection()
            elif choice == "2":
                flag_inner = False
            else:
                print("choose correct option")
        except Exception as e:
            print("something went wrong")
            print(f"The exact error is: {e}")
        hold_screen()


if run_once == True:
    run_once = False
    main_menu()

clear_display()
log_database.save_students()
log_database.save_teachers()