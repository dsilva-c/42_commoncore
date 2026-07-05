import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Generate an endless stream of random game events."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "move", "grab", "use", "climb", "eat", "sleep", "swim"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Consume and yield events in random order until the list is empty."""
    while events:
        idx = random.randrange(len(events))
        yield events.pop(idx)


def ft_data_stream() -> None:
    """Demonstrate generator-based data streaming."""
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    list_gen = gen_event()
    event_list = [next(list_gen) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
