import heapq
from copy import deepcopy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

MOVES = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}


class Puzzle:
    def __init__(self, board, parent=None, move="", moved_tile=None, depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.moved_tile = moved_tile
        self.depth = depth
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def display(self):
        for row in self.board:
            print(row)
        print()

    def is_goal(self):
        return self.board == GOAL_STATE

    def get_successors(self):
        successors = []
        x, y = self.blank_pos

        for move, (dx, dy) in MOVES.items():
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = deepcopy(self.board)

                moved_tile = new_board[nx][ny]  # Tile being moved

                # Swap
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

                child = Puzzle(
                    new_board,
                    self,
                    move,
                    moved_tile,
                    self.depth + 1
                )
                successors.append(child)

        return successors

    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def cost(self):
        return self.depth + self.heuristic()

    def __lt__(self, other):
        return self.cost() < other.cost()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))


def a_star(start):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return current

        closed_set.add(current)

        for neighbor in current.get_successors():
            if neighbor in closed_set:
                continue
            heapq.heappush(open_list, neighbor)

    return None


# ✅ FORMATTED OUTPUT FUNCTION
def print_solution(goal):
    path = []
    current = goal

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    print("\n=== Solution Steps ===\n")

    for i, step in enumerate(path):
        if i == 0:
            print(f"Initial State:")
        else:
            print(f"Move {i}: Move tile {step.moved_tile} {step.move.lower()}")

        step.display()


# 🔹 Given Initial State
initial_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

start = Puzzle(initial_board)
solution = a_star(start)

if solution:
    print_solution(solution)
else:
    print("No solution found.")