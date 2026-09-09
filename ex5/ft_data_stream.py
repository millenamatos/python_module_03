import random

def gen_event():
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)

players = ["bob", "alice", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move", "swim", "climb", "release", "use"]

def consume_event(event_list):
    while event_list:
        index = random.randint(0, len(event_list) - 1)
        event = event_list.pop(index)
        yield event

event_generator = gen_event()
print("=== Game Data Stream Processor ===")
for i in range(1000):
    event = next(event_generator)
    player, action = event
    print(f"Event {i}: Player {player} did action {action}")

event_generator = gen_event()
event_list = []
for i in range(10):
    event = next(event_generator)
    event_list.append(event)
print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")