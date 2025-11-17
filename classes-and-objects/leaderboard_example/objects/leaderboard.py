import csv
from objects.player import Player

class Leaderboard:
    def __init__(self):
        self.players = []

    def load_players_from_csv(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                player =  Player(row["username"], int(row["score"]), int(row["time"]), row["rank"])
                self.players.append(player)

    def print_leaderboard(self):
        print("###############################################################################")

        for player in self.players:
            print(player)

        print("###############################################################################")

    def sort_by_high_score(self):
        self.players.sort(key=lambda player: player.score, reverse=True)

    def sort_by_name(self):
        self.players.sort(key=lambda player: player.name)

    def sort_by_time(self):
        self.players.sort(key=lambda player: player.time)

    def sort_by_rank(self):
        self.players.sort(key=lambda player: player.rank)