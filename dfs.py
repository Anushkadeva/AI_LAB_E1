
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)



def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)



if __name__ == "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    print("Recursive DFS:")
    dfs_recursive(graph, 'A')

    print("\nIterative DFS:")
    dfs_iterative(graph, 'A')