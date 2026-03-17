from collections import deque

goal = [1,2,3,4,5,6,7,8,0]

moves = {
    0:[1,3],
    1:[0,2,4],
    2:[1,5],
    3:[0,4,6],
    4:[1,3,5,7],
    5:[2,4,8],
    6:[3,7],
    7:[4,6,8],
    8:[5,7]
}

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(start))
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal:
            return path + [state]
        
        zero = state.index(0)
        
        for move in moves[zero]:
            new_state = state.copy()
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append((new_state, path + [state]))
    
    return None

start = [1,2,3,4,0,6,7,5,8]

solution = bfs(start)

for step in solution:
    print(step[0:3])
    print(step[3:6])
    print(step[6:9])
    print()
