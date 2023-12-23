def path_crossing(path):
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # The idea is to use a set to store the visited points
    directions = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }

    x, y = 0, 0 # Initial position

    # We use set to store the visited points because it is faster to check if a point has been visited
    visited = set()
    
    for i in path:
        visited.add((x, y)) # Add the current point to the visited set

        dx, dy = directions[i] # Get the direction

        x, y = dx + x, dy + y # Update the position

        # Check if the current point has been visited
        if (x, y) in visited:
            return True
    # If the path does not cross, return False
    return False

# Test
path = input('Enter a path with N/S/E/W directions: ')

if path_crossing(path):
    print('Point(s) was found that cross each other')
else:
    print('The path does not cross')