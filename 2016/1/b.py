directions = open('input', 'r').read().strip().split(', ')
x = 0
y = 0
facing = 0 #North
visited = {}
visited[(x, y)] = True

for direction in directions:
    if direction[0] == 'R':
        facing += 1
    else:
        facing -= 1

    if facing < 0:
        facing = 3
    elif facing > 3:
        facing = 0

    count = int(direction[1:])

    for i in range(count):
        if facing == 0: # North
            y += 1 
        elif facing == 1: # East
            x += 1
        elif facing == 2: # South
            y -= 1
        elif facing == 3: # West
            x -= 1
        position = (x, y)
        if visited.get(position, False):
            # Absolute values because direction isn't relevant, just distance
            x = abs(x)
            y = abs(y)
            print(x + y) 
            exit()
        visited[position] = True
