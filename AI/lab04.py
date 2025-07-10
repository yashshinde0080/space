class Node:
    def __init__(self, name, node_type, children=None, heuristic=0):
        self.name = name
        self.node_type = node_type  # 'AND' or 'OR'
        self.children = children if children else []
        self.heuristic = heuristic
        self.solved = False

# Define the nodes
D = Node('D', 'OR', heuristic=3)
E = Node('E', 'OR', heuristic=2)
F = Node('F', 'OR', heuristic=1)
B = Node('B', 'AND', children=[D, E])
C = Node('C', 'OR', children=[F])
A = Node('A', 'OR', children=[B, C])

def ao_star(node):
    if not node.children:
        node.solved = True
        return node.heuristic

    costs = []
    for child in node.children:
        if node.node_type == 'AND':
            cost = sum(ao_star(c) for c in child.children) if child.children else ao_star(child)
        else:  # OR node
            cost = ao_star(child)
        costs.append((cost, child))

    # Choose the minimum cost child (for OR), total cost (for AND)
    if node.node_type == 'OR':
        min_cost, best_child = min(costs, key=lambda x: x[0])
        node.heuristic = min_cost
        node.children = [best_child]  # Keep only the best path
    else:  # AND node, already summed up
        total_cost = sum(cost for cost, _ in costs)
        node.heuristic = total_cost

    node.solved = True
    return node.heuristic

# Run AO* from root A
final_cost = ao_star(A)

# Print the solution path
def print_solution(node):
    if not node.children:
        print(node.name, end=" ")
        return
    print(node.name, end=" -> ")
    for child in node.children:
        print_solution(child)

print(f"Final cost to solve A: {final_cost}")
print("Solution path:")
print_solution(A)