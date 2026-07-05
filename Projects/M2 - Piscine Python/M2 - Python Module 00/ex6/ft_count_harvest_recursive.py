def ft_count_harvest_recursive():
    """Count days until harvest using recursion."""
    days = int(input("Days until harvest: "))

    def count_days(current: int, total: int) -> None:
        """Helper function to recursively count days."""
        if current > total:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count_days(current + 1, total)

    count_days(1, days)
