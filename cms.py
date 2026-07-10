



print("""
      
      Main Dashboard : College Management System

      choose your option :

      1. Student
      2. Teacher
      3. Admin
      """)
while True:
    try:
        choice = int(input(": "))
        break
    except ValueError:
        print("enter numeric value")
    except Exception:
        print("something went wrong")
    