directions = open('input', 'r').read().strip().split(', ')
x = 0
y = 0
facing = 0 #North
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

    if facing == 0: # North
        y += count
    elif facing == 1: # East
        x += count
    elif facing == 2: # South
        y -= count
    elif facing == 3: # West
        x -= count

# Absolute values because direction isn't relevant, just distance
x = abs(x)
y = abs(y)
print(x + y)
