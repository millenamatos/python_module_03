import math

def get_player_pos():
    while True:
            coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
            coordinates = coordinates.split(",")
            if len(coordinates) != 3:
                print("Invalid syntax")
                continue
            count = 0
            try:
                for element in coordinates:
                    coordinates[count] = float(element)
                    count += 1
            except ValueError as error:
                print(f"Error on parameter '{element}': {error}")
                continue
            coordinates = tuple(coordinates)
            return coordinates
        
if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")
    distance_center = math.sqrt((0 - first_pos[0])**2 + (0 - first_pos[1])**2 + (0 - first_pos[2])**2)
    print(f"Distance to center: {round(distance_center, 4)}")
    print("\nGet a second set of coordinates")
    second_pos = get_player_pos()
    distance_between = math.sqrt((second_pos[0] - first_pos[0])**2 + (second_pos[1] - first_pos[1])**2 + (second_pos[2] - first_pos[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance_between, 4)}")
