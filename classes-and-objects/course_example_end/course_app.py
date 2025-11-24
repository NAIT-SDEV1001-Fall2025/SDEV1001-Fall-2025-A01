from data.course_data import student_data, assignment_data, submission_data

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
        


if __name__ == "__main__":
    # Create course
    course = Course("Dans Basketball Mastery Course")

    # Add students to course
    add_students(course)

    # Add assignments to course
    add_assignments(course)

    # Add submissions to the course
    add_submissions(course)

    # display course information
    print(course)

    # display course average
    print(F"Course average: {course.get_course_average()}")
