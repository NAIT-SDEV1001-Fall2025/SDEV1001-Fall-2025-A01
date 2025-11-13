from data.course_data import student_data, assignment_data, submission_data
from random import randint

from tools.school import School
from tools.course import Course
from tools.student import Student
from tools.assignment import Assignment
from tools.submission import Submission

def add_students(course):
    for student in student_data:
        student_instance = Student(student["id"], student["name"])
        course.add_student(student_instance)
    

def add_assignments(course):
    for assignment in assignment_data:
        assignment_instance = Assignment(assignment["id"], assignment["name"])
        course.add_assignment(assignment_instance)

def add_submissions(course):
    for submission in submission_data:
        student = course.get_student(submission["student_id"])
        assignment = course.get_assignment(submission["assignment_id"])
        submission = Submission(student, assignment, submission["grade"])
        student.add_submission(submission)

def load_data(school):
    course = Course("Dans Basketball Mastery Course")
    add_students(course)
    add_assignments(course)
    add_submissions(course)
    school.add_course(course)

def manage_course(course):
    option = input("""How do you want to manage the course? (choose number)
            1. Add Student
            2. Add Assignment
            3. Add Submission
            4. Get Course Average
            5. Get Assignment Average
            6. Get Student Average
        """)
    
    match option:
        case "1":
            new_id = randint(0, 1000)
            for student in course.students:
                if new_id == student.id:
                    new_id = randint(0, 1000)
            
            student_name = input("What is the student's name? ")
            course.add_student(Student(new_id, student_name))
        case "2":
            new_id = randint(0, 1000)
            for assignment in course.assignments:
                if new_id == assignment.id:
                    new_id = randint(0, 1000)
            
            assignment_name = input("What is the assignment's name? ")
            course.add_assignment(Assignment(new_id, assignment_name))
        case "3":
            try:
                course.list_students()
                student_id = int(input("Which student is this submission for? (Enter id) "))
                student = course.get_student(student_id)
                if student == None:
                    print("Student not found.")
                
                course.list_assignments()
                assignment_id = int(input("Which assignment is this submission for? (Enter id) "))
                assignment = course.get_assignment(assignment_id)
                if assignment == None:
                    print("Assignment not found.")

                if student != None and assignment != None:
                    grade = float(input("Enter Student Grade: "))
                    submission = Submission(student, assignment, grade)
                    student.add_submission(submission)
                
            except ValueError:
                print("Invalid Choice...")
        case "4":
            print(f"Course average: {course.get_course_average()}")
        case "5":
            try:
                course.list_assignments()
                assignment_id = int(input("Which assignment do you want the average of? (Enter id)"))
                print(f"Average: {course.get_assignment_average(assignment_id)}")
            except ValueError:
                print("Invalid Option")
        case "6":
            try:
                course.list_students()
                student_id = int(input("Which student do you want the average of? (Enter id)"))
                student = course.get_student(student_id)
                if student == None:
                    print("Student not found.")
                else:
                    print(f"Average: {student.get_average()}")
            except ValueError:
                print("Invalid Option")
        case _:
            print("Invalid option...")

def main():
    school_name = input("What is the school's name? ")
    school = School(school_name)
    load_data(school)

    while True:
        option = input(""" What do you want to do? (choose number)
            1. List courses
            2. Add course
            3. Manage course
            4. Quit
        """)

        match option:
            case "1":
                school.list_courses()
            case "2":
                course_name = input("What is the name of the course? ")
                course = Course(course_name)
                school.add_course(course)
            case "3":  
                try:
                    school.list_courses()
                    course_index = int(input("Which course would like to manage (by index)? "))
                    course = school.courses[course_index]
                    manage_course(course)
                except (ValueError, IndexError):
                    print("Invalid Course option.")
            case "4":
                break
        
if __name__ == "__main__":
    main()