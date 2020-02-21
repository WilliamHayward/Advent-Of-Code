instructions = open('input', 'r').read().strip().split('\n')

SCREEN_HEIGHT = 6
SCREEN_WIDTH = 50
screen = []
for y in range(SCREEN_HEIGHT):
    screen.append([])
    for x in range(SCREEN_WIDTH):
        screen[y].append(False)

def shiftRow(y, dist):
    for n in range(dist):
        final = screen[y][-1]
        for x in range(SCREEN_WIDTH - 1, 0, -1):
            screen[y][x] = screen[y][x-1]
        screen[y][0] = final

def shiftColumn(x, dist):
    for n in range(dist):
        final = screen[-1][x]
        for y in range(SCREEN_HEIGHT - 1, 0, -1):
            screen[y][x] = screen[y-1][x]
        screen[0][x] = final

def printScreen():
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            c = 'F'
            if screen[y][x]:
                c = 'T'
            print(c, end='')
        print()
    print()

for instruction in instructions:
    components = instruction.split(' ')
    if components[0] == 'rotate':
        position = int(components[2][2:])
        distance = int(components[4])
        if components[1] == 'column':
            shiftColumn(position,distance)
        else:
            shiftRow(position, distance)
    else:
        width = int(components[1].split('x')[0])
        height = int(components[1].split('x')[1])
        for y in range(height):
            for x in range(width):
                screen[y][x] = True

count = 0
for y in range(SCREEN_HEIGHT):
    for x in range(SCREEN_WIDTH):
        if screen[y][x]:
            count += 1

print(count)
