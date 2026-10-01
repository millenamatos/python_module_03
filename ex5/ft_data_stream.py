import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ["bob", "alice", "charlie", "dylan"]
    actions: list[str] = ["run", "eat", "sleep", "grab", "move",
                          "swim", "climb", "release", "use"]

    while True:
        player: str = random.choice(players)
        action: str = random.choice(actions)
        yield (player, action)


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while event_list:
        index: int = random.randint(0, len(event_list) - 1)
        event: tuple[str, str] = event_list.pop(index)
        yield event


def main() -> None:
    event_generator = gen_event()

    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(event_generator)
        player, action = event
        print(f"Event {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = []

    for _ in range(10):
        event_list.append(next(event_generator))

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
