class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []
    
    def add_student(self, student):
        self.students.append(student)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
    
    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    
    def list_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")

    def list_assignments(self):
        for assignment in self.assignments:
            print(assignment)
    
    def get_assignment(self, assignment_id):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                return assignment
        return None
    
    def get_course_average(self):
        total = 0
        number_of_submissions = 0
        for student in self.students:
            for submission in student.submissions:
                total += submission.grade
                number_of_submissions += 1
        return total / number_of_submissions
    
    def get_assignment_average(self, assignment_id):
        total = 0
        number_of_submissions = 0
        for student in self.students:
            for submission in student.submissions:
                if submission.assignment.id == assignment_id:
                    total += submission.grade
                    number_of_submissions += 1

        return total / number_of_submissions
    
    def __str__(self):
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"