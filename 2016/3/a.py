specs = open('input', 'r').read().strip().split('\n')

def isTriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True

count = 0
for spec in specs:
    lengths = spec.strip().split()
    a = int(lengths[0])
    b = int(lengths[1])
    c = int(lengths[2])
    if isTriangle(a, b, c):
        count += 1

print(count)
