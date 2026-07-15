import admin 
from student import student 
from teacher import teacher
import time
students = []
teachers = []
admin_user = []
persons = []


def save_students():
    try:
        if students != []:
            print("Saving student data...")
            with open("student_data.txt","w") as file:
                for s in students:
                    line = f"{s.person_id},{s.name},{s.mobile},{s.age},{s.gender},{s.roll_no},{s.course},{s.semester},{s.attendance},{s.password},{s.marks},{s.fees_paid},\n"
                    file.write(line)
    except Exception as e:
        print(f"data not saved because of {e}")
    else:
        time.sleep(0.5)
        print("Data Saved ")


def load_students():
    try:
        print("Loading employee data...")
        time.sleep(0.5)
        with open("student_data.txt","r") as f:
            for i in f:
                data = []
                data = i.split(",")
                person_id = str(data[0])
                name = data[1]
                mobile = data[2]
                age = data[3]
                gender = data[4]
                roll_no = data[5]
                course = data[6]
                semester = data[7]
                attendance = data[8]
                password = str(data[9])
                marks = eval(data[10])
                fees_paid = int(data[11])
                obj_name = person_id
                obj_name = student(person_id,name,mobile,age,gender,roll_no,course,semester,attendance,password,fees_paid)
                obj_name.marks = marks
                students.append(obj_name)
    except FileNotFoundError:
        print("Data do not exist")
    except Exception as e:
        print(f"error occured because of {e}")
    else:
        print(" loaded sucessfully.")


def save_teachers():
    try:
        if teachers != []:
            print("Saving teacher data...")
            with open("teacher_data.txt","w") as file:
                for t in teachers:
                    line = f"{t.person_id},{t.name},{t.mobile},{t.age},{t.gender},{t.employee_id},{t.subject},{t.password},{t.salary},\n"
                    file.write(line)
    except Exception as e:
        print(f"data not saved : {e}")
    else:
        time.sleep(0.5)
        print("Data Saved Sucessfully")



        
def load_teachers():
    try:
        print("Loading teacher data...")
        time.sleep(0.5)
        with open("teacher_data.txt","r") as f:
            for i in f:
                data = []
                data = i.split(",")
                person_id = str(data[0])
                name = data[1]
                mobile = data[2]
                age = data[3]
                gender = data[4]
                employee_id = data[5]
                subject = data[6]
                password = str(data[7])
                salary = data[8]
                obj = person_id
                obj = teacher(person_id,name,mobile,age,gender,employee_id,subject,password)
                obj.salary = salary
                teachers.append(obj)
    except FileNotFoundError:
        print("Data do not exist")
    except Exception as e:
        print(f"error occured because of {e}")
    else:
        print(" loaded sucessfully.")