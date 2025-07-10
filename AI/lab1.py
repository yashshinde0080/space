def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    def is_valid_state(state):
        # Check if the state is already visited or invalid
        return state not in visited

    def dfs(state):
        # If the target is reached, return the path
        if state[0] == target or state[1] == target:
            solution.append(state)
            return True

        # Mark the state as visited
        visited.add(state)
        solution.append(state)

        # Possible moves from the current state
        moves = [
            (jug1_capacity, state[1]),  # Fill Jug 1
            (state[0], jug2_capacity),  # Fill Jug 2
            (0, state[1]),              # Empty Jug 1
            (state[0], 0),              # Empty Jug 2
            (min(state[0] + state[1], jug1_capacity), max(0, state[1] - (jug1_capacity - state[0]))),  # Pour Jug 2 -> Jug 1
            (max(0, state[0] - (jug2_capacity - state[1])), min(state[0] + state[1], jug2_capacity))   # Pour Jug 1 -> Jug 2
        ]
        
        for move in moves:
            if is_valid_state(move):
                if dfs(move):
                    return True

        # Backtrack
        solution.pop()
        return False

    # Initialize variables
    visited = set()
    solution = []
    initial_state = (0, 0)

    # Start DFS from the initial state
    if dfs(initial_state):
        return solution
    else:
        return "No solution found"

# Example Usage
jug1_capacity = int(input("Enter Jug 1 capacity : "))
jug2_capacity = int(input("Enter Jug 2 capacity : "))
target = int(input("Enter Target Volume : "))
result = water_jug_dfs(jug1_capacity, jug2_capacity, target)
print("Solution:", result)