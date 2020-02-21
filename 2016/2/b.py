instructions = open('input', 'r').read().strip().split('\n')

x = 1
y = 1
keypad = [
    [' ', ' ', '1', ' ', ' '],
    [' ', '2', '3', ' ', ' '],
    ['5', '6', '7', '8', '9'],
    [' ', 'A', 'B', 'C', ' '],
    [' ', ' ', 'D', ' ', ' ']
]

code = ' '
def clamp(lower, upper, val):
    if val > upper:
        val = upper
    elif val < lower:
        val = lower
    return val

for instruction in instructions:
    for direction in instruction:
        newY = y
        newX = x
        if direction == 'D':
            newY += 1
        elif direction == 'U':
            newY -= 1
        elif direction == 'R':
            newX += 1
        elif direction == 'L':
            newX -= 1
        
        newX = clamp(0, 4, newX)
        newY = clamp(0, 4, newY)
        if keypad[newY][newX] != ' ':
            x = newX
            y = newY
    code += keypad[y][x]
print(code)
