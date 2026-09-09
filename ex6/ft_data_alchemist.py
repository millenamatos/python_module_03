import random

players = ["Alice", "bob", "Charlie", 
        "dylan", "Emma", "Gregory", 
        "john", "kevin", "Liam"]

print("=== Game Data Alchemist ===")
print(f"Initial list of players: {players}")
capitalize_players = [player.capitalize() for player in players]
print(f"New list with all names capitalized: {capitalize_players}")
only_capitalized = [player for player in players if player.istitle()]
print(f"New list of capitalized names only: {only_capitalized}")
score_dict = {player : random.randint(0, 1000) for player in capitalize_players}
print(f"Score dict: {score_dict}")
score_average = round(sum(score_dict.values()) / len(capitalize_players), 2)
print(f"Score average: {score_average}")
high_scores = {player : score for player, score in score_dict.items() if score > score_average}
print(f"High scores: {high_scores}")