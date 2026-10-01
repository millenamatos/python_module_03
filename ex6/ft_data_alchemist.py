import random


def main() -> None:
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")

    capitalize_players: list[str] = [
        player.capitalize() for player in players
    ]
    print(f"New list with all names capitalized: {capitalize_players}")

    only_capitalized: list[str] = [
        player for player in players if player.istitle()
    ]
    print(f"New list of capitalized names only: {only_capitalized}")

    score_dict: dict[str, int] = {
        player: random.randint(0, 1000)
        for player in capitalize_players
    }
    print(f"Score dict: {score_dict}")

    score_average: float = round(
        sum(score_dict.values()) / len(capitalize_players), 2
    )
    print(f"Score average: {score_average}")

    high_scores: dict[str, int] = {
        player: score
        for player, score in score_dict.items()
        if score > score_average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
