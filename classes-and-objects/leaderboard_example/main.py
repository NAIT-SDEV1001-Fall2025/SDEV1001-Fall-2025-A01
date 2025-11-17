from pathlib import Path
from objects.leaderboard import Leaderboard


def main():
    directory = Path(__file__).parent
    file_path = directory / "data" / "game_data.csv"

    leaderboard = Leaderboard()
    leaderboard.load_players_from_csv(file_path)
    leaderboard.sort_by_high_score()
    leaderboard.print_leaderboard()

if __name__ == "__main__":
    main()