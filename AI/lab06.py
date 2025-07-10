import math

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to find the nearest city to the current city
def find_nearest_city(current_city, cities, visited):
    nearest_city = None
    min_distance = float('inf')
    for i, city in enumerate(cities):
        if i not in visited:
            dist = calculate_distance(current_city, city)
            if dist < min_distance:
                min_distance = dist
                nearest_city = i
    return nearest_city

# Heuristic approach to solve TSP
def greedy_tsp(cities):
    # Starting city (we start from the first city)
    start_city = 0
    visited = [start_city]  # List to keep track of visited cities
    total_distance = 0
    current_city = cities[start_city]
    
    # Loop until all cities are visited
    while len(visited) < len(cities):
        nearest_city = find_nearest_city(current_city, cities, visited)
        visited.append(nearest_city)
        total_distance += calculate_distance(current_city, cities[nearest_city])
        current_city = cities[nearest_city]
    
    # Add distance to return to the starting city
    total_distance += calculate_distance(current_city, cities[start_city])
    
    return visited, total_distance

# Example cities (x, y coordinates)
cities = [(0, 0), (2, 4), (4, 3), (5, 1), (7, 5)]

# Solve TSP using Greedy heuristic approach
visited_cities, total_distance = greedy_tsp(cities)

print("Visited Cities Order:", visited_cities)
print("Total Distance Traveled:", total_distance)