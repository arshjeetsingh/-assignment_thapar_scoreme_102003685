
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    n = len(graph)
    if not validate_graph(graph, n):
        return 0
    topo_order = topological_sort(graph, n)
    return calculate_longest_path(graph, topo_order)

def validate_graph(graph, n):
    for node_index, edges in enumerate(graph):
        for (adj_node, weight) in edges:
            if adj_node >= n:
                print(f"Error: Node {adj_node} referenced in edges but only {n} nodes (0 to {n-1}) exist.")
                return False
    return True

def topological_sort(graph, n):
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]  # Return reversed stack to get topological order

def calculate_longest_path(graph, topo_order):
    dist = [float('-inf')] * len(graph)
    for node in topo_order:
        if dist[node] == float('-inf'):
            dist[node] = 0  # Starting node in the path
        for neighbor, weight in graph[node]:
            if dist[neighbor] < dist[node] + weight:
                dist[neighbor] = dist[node] + weight
    return max(dist)

def input_graph():
    import ast
    print("Enter the graph as a list of lists. Each sublist should contain tuples (j, w) where 'j' is the node and 'w' is the weight.")
    print("Example: [[(1, 3), (2, 2)], [(3, 4)], [(3, 1)], []]")
    input_string = input("Enter the graph: ")
    try:
        graph = ast.literal_eval(input_string)
        if isinstance(graph, list) and all(isinstance(node, list) and all(isinstance(edge, tuple) and len(edge) == 2 for edge in node) for node in graph):
            return graph
        else:
            print("Invalid graph format. Please ensure it's a list of lists of tuples.")
            return None
    except:
        print("Invalid input. Please make sure your input is in the correct format.")
        return None

if __name__ == "__main__":
    graph = input_graph()
    if graph is not None:
        result = longest_path(graph)
        if result != 0:
            print("Longest path length:", result)
