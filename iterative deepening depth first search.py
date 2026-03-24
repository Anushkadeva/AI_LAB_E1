def dls(graph, node, goal, depth, visited):
 
    if depth == 0 and node == goal:
        return True
    
    if depth > 0:
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
                visited.remove(neighbor)  # backtrack
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set([start])
        print(f"Searching at depth: {depth}")
        if dls(graph, start, goal, depth, visited):
            print(f"Goal '{goal}' found at depth {depth}")
            return True
    print("Goal not found")
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


iddfs(graph, 'A', 'F', max_depth=3)