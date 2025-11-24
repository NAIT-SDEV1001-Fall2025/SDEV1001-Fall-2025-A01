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
