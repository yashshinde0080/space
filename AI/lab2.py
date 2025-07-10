from queue import PriorityQueue

def is_valid(state):
    m_left, c_left, _, m_right, c_right = state
    return all(x >= 0 for x in state) and (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)

def generate_successors(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    m_left, c_left, boat, m_right, c_right = state
    return [(m_left - m, c_left - c, 1 - boat, m_right + m, c_right + c) if boat else
            (m_left + m, c_left + c, 1 - boat, m_right - m, c_right - c)
            for m, c in moves if is_valid((m_left - m, c_left - c, 1 - boat, m_right + m, c_right + c) if boat else
                                          (m_left + m, c_left + c, 1 - boat, m_right - m, c_right - c))]

def best_first_search(initial, goal):
    frontier, explored, parent = PriorityQueue(), set(), {initial: None}
    frontier.put((sum(initial[:2]), initial))
    while not frontier.empty():
        _, current = frontier.get()
        if current in explored:
            continue
        explored.add(current)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for neighbor in generate_successors(current):
            if neighbor not in explored:
                frontier.put((sum(neighbor[:2]), neighbor))
                parent[neighbor] = current
    return None

initial_state, goal_state = (3, 3, 1, 0, 0), (0, 0, 0, 3, 3)
solution = best_first_search(initial_state, goal_state)
print("Solution path:") if solution else print("No solution found.")
print("m_left, c_left, boat, m_right, c_right")
for step in solution or []:
    print(step)