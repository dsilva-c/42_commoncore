import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompt until a valid 3D coordinate tuple is provided."""
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = [part.strip() for part in raw.split(",")]
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords: list[float] = []
        for part in parts:
            try:
                coords.append(float(part))
            except ValueError as exc:
                print(f"Error on parameter '{part}': {exc}")
                break
        if len(coords) == 3:
            return (coords[0], coords[1], coords[2])


def ft_coordinate_system() -> None:
    """Demonstrate 3D coordinates and distance calculations."""
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    center_dist = math.sqrt(first[0] ** 2 + first[1] ** 2 + first[2] ** 2)
    print(f"Distance to center: {round(center_dist, 4)}")

    print("Get a second set of coordinates")
    second = get_player_pos()

    dx = second[0] - first[0]
    dy = second[1] - first[1]
    dz = second[2] - first[2]
    dist = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    ft_coordinate_system()
