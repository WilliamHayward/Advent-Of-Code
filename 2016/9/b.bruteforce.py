import re
# About time I started using regex for these

message = open('input', 'r').read().strip()
#message = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
expression = r'\([0-9]+x[0-9]+\)'
def decompress(compressed):
    decompressed = ''
    matches = re.finditer(expression, compressed)
    pointer = 0

    for match in matches:
        span = match.span()
        start = span[0]
        end = span[1]
        if start < pointer:
            continue;
        decompressed += compressed[pointer:start]
        text = match.group()[1:-1] # Trim parenthesis
        text = text.split('x')
        size = int(text[0])
        repeats = int(text[1])
        pointer = end + size
        text = compressed[end:pointer]
        for n in range(repeats):
            decompressed += text
    decompressed += compressed[pointer:]
    return decompressed


while len(re.findall(expression, message)) > 0 :
    message = decompress(message)
    print(len(message))

