instructions = open('input', 'r').read().strip().split('\n')

x = 1
y = 1
keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
code = ''
def clamp(lower, upper, val):
    if val > upper:
        val = upper
    elif val < lower:
        val = lower
    return val

for instruction in instructions:
    for direction in instruction:
        if direction == 'D':
            y += 1
        elif direction == 'U':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        
        x = clamp(0, 2, x)
        y = clamp(0, 2, y)
    code += keypad[y][x]
print(code)
