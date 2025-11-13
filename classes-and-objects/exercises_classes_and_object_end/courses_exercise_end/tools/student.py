from .submission import Submission

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.submissions = []

    def __str__(self):
        return f"{self.name}"
    
    def add_submission(self, submission):
        self.submissions.append(submission)

    def get_average(self):
        total = 0
        for submission in self.submissions:
            total += submission.grade
        return total / len(self.submissions)