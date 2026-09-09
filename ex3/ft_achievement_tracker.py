import random

def gen_player_achievements():
    achievements = [
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
    quantity = random.randint(5, 8)
    selected = random.sample(achievements, quantity)
    return set(selected)


if __name__ == "__main__":
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = set.union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements = set.intersection(alice, bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}")

    only_alice = alice - set.union(bob, charlie, dylan)
    print(f"\nOnly Alice has: {only_alice}")
    only_bob = bob - set.union(alice, charlie, dylan)
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie - set.union(alice, bob, dylan)
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = dylan - set.union(alice, charlie, bob)
    print(f"Only Dylan has: {only_dylan}")

    missing_alice = all_achievements - alice
    print(f"\nAlice is missing: {missing_alice}")
    missing_bob = all_achievements - bob
    print(f"Bob is missing: {missing_bob}")
    missing_charlie = all_achievements - charlie
    print(f"Charlie is missing: {missing_charlie}")
    missing_dylan = all_achievements - dylan
    print(f"Dylan is missing: {missing_dylan}")
