import json


def print_students(data):
    for student in data["students"]:
        print("Student: " + student["name"])


def print_course_info(data):
    print("Course: " + data["course_name"])
    print("Professor: " + data["professor"])


def print_student(data, student_id):
    for student in data["students"]:
        if student.name is student_id:
            print("ID: " + student_id)
            print("Name: " + student.name)
            print("Passing: " + student.Passing)


def main():
    json_file = 'somedata.json'

    with open(json_file) as json_file:
        data = json.load(json_file)

    print_course_info(data["course_info"])
    print_students(data)

main()


####################################################################################

# Sample Output

# Professor: John Martin
# Course: Math 1B
# Student: Jim Smith
# Student: Mat Lee
# Student: Gwen O'Rorke
# Student: Justin Martin
# Student: Steven Heidel
# Student: Paulina Marcos
# Student: Lydia Kajeckas
# Student: Emmy O'Brien
# Student: Donna Pershing

####################################################################################
