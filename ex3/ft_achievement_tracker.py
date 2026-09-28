import random

def gen_player_achievements() -> set[str]:
    achievements: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Master Explorer",
    "World Savior",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "Untouchable",
    "Collector Supreme",
    "Unstoppable",
    "Hidden Path Finder",
    "Sharp Mind"
    ]
    quantity: int = random.randint(5, 8)
    selected: list[str] = random.sample(achievements, quantity)
    return set(selected)


def main() -> None:
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements: set[str] = set.union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements: set[str] = set.intersection(alice, bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}")

    only_alice: set[str] = alice - set.union(bob, charlie, dylan)
    print(f"\nOnly Alice has: {only_alice}")

    only_bob: set[str] = bob - set.union(alice, charlie, dylan)
    print(f"Only Bob has: {only_bob}")

    only_charlie: set[str] = charlie - set.union(alice, bob, dylan)
    print(f"Only Charlie has: {only_charlie}")

    only_dylan: set[str] = dylan - set.union(alice, charlie, bob)
    print(f"Only Dylan has: {only_dylan}")

    missing_alice: set[str] = all_achievements - alice
    print(f"\nAlice is missing: {missing_alice}")

    missing_bob: set[str] = all_achievements - bob
    print(f"Bob is missing: {missing_bob}")

    missing_charlie: set[str] = all_achievements - charlie
    print(f"Charlie is missing: {missing_charlie}")

    missing_dylan: set[str] = all_achievements - dylan
    print(f"Dylan is missing: {missing_dylan}")

if __name__ == "__main__":
    main()
