class Player:
    def __init__(self, name, score, time, rank):
        self.name = name
        self.score = score
        self.time = time
        self.rank = rank

    def __str__(self):
        return f"Username: {self.name} | Score: {self.score} | Time Played: {self.time} | Rank: {self.rank}"
    
    def __repr__(self):
        return f"Player({self.name}, {self.score}, {self.time}, {self.rank})"