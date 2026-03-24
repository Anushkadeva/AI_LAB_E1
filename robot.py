import random

# Constants
GRID_SIZE = 4

# Initialize grid with random dirty (1) or clean (0)
def create_room():
    return [[random.choice([0, 1]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Display the grid
def display_room(room):
    for row in room:
        print(" ".join(["D" if cell == 1 else "C" for cell in row]))
    print()

# Robot cleaning function
def clean_room(room):
    cleaned_positions = []
    total_dirty = 0
    cleaned_count = 0

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if room[i][j] == 1:  # Dirty cell
                total_dirty += 1
                room[i][j] = 0   # Clean it
                cleaned_positions.append((i, j))
                cleaned_count += 1

    # Calculate performance
    performance = (cleaned_count / total_dirty * 100) if total_dirty > 0 else 100

    return cleaned_positions, performance

# Main program
room = create_room()

print("Room state BEFORE cleaning:")
display_room(room)

cleaned_positions, performance = clean_room(room)

print("Room state AFTER cleaning:")
display_room(room)

print("Locations cleaned by the robot:")
for pos in cleaned_positions:
    print(pos)

print(f"\nPerformance: {performance:.2f}%")