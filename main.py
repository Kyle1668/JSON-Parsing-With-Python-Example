import json


def print_students(data):
    for student in data["students"]:
        print("Student: " + student["name"])


def print_course_info(course_data):
    print("Course: " + course_data["course_name"])
    print("Professor: " + course_data["professor"])


def main():
    with open('somedata.json') as json_file:
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
