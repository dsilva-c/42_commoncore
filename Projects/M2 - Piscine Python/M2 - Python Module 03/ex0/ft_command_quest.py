import sys


def ft_command_quest() -> None:
    """Display command-line arguments."""
    args = sys.argv
    program = args[0]
    user_args = args[1:]
    print("=== Command Quest ===")
    print(f"Program name: {program}")
    if not user_args:
        print("No arguments provided!")
        print(f"Total arguments: {len(args)}")
        return
    print(f"Arguments received: {len(user_args)}")
    for i, arg in enumerate(user_args, start=1):
        print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    ft_command_quest()
