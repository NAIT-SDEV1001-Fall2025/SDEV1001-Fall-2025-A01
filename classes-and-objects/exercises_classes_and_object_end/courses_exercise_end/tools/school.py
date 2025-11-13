from tools.course import Course

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        for idx, course in enumerate(self.courses):
            print(f"{idx}. {course}")

    def __str__(self):
        return self.name