import re
# About time I started using regex for these

compressed = open('input', 'r').read().strip()
decompressed = ''
expression = r'\([0-9]+x[0-9]+\)'
matches = re.finditer(expression, compressed)
pointer = 0

for match in matches:
    span = match.span()
    start = span[0]
    end = span[1]
    if start < pointer:
        print(pointer)
        continue;
    decompressed += compressed[pointer:start]
    text = match.group()[1:-1] # Trim parenthesis
    size = int(text.split('x')[0])
    repeats = int(text.split('x')[1])
    pointer = end + size
    text = compressed[end:pointer]
    for n in range(repeats):
        decompressed += text
decompressed += compressed[pointer:]
print(decompressed)
print(len(decompressed))
