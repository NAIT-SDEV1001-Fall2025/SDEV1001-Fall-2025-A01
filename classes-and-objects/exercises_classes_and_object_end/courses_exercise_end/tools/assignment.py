class Assignment():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Assignment ID: {self.id}, Assignment Name: {self.name}"

    def __repr__(self):
        return str(self)