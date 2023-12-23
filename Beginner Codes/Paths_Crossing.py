def path_crossing(path):
    directions = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }

    x, y = 0, 0

    visited = set()
    
    for i in path:
        visited.add((x, y))

        dx, dy = directions[i]

        x, y = dx + x, dy + y

        if (x, y) in visited:
            return True
    
    return False

path = input('Enter a path with N/S/E/W directions: ')

if path_crossing(path):
    print('Point(s) was found that cross each other')
else:
    print('The path does not cross')