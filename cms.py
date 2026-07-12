import admin

def role_selection():
    while True:
        print("Select Role")
        print()
        print("1. student")
        print("2. teacher")
        print("3. Admin ")
        print("4. Principal")
        print("5. Back")
        
        role_choice = int(input("Enter your choice"))

        if role_choice == 1:
            pass
        elif role_choice == 2:
            pass
        elif role_choice == 3:
            a = admin.admin("a101","shubh",22,"male")
            a.login()
        elif role_choice == 4:
            pass
        elif role_choice == 5:
            break
        else:
            print("incorrect choice")


while True:
    print("""
        
        Main Dashboard : College Management System

        choose your option :

        1. login
        2. exit
        """)
    while True:
        try:
            choice = int(input("         : "))
        except ValueError:
            print("enter numeric value")
        except Exception:
            print("something went wrong")
        else:
            if choice == 1:
                role_selection()
            else:
                break
        
    
