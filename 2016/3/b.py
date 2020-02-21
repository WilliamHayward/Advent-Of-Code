specs = open('input', 'r').read().strip().split('\n')

def isTriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True
row = 0
triangles = []
for spec in specs:
    triangles.append([])
    lengths = spec.strip().split()
    a = int(lengths[0])
    b = int(lengths[1])
    c = int(lengths[2])
    triangles[row].append(a)
    triangles[row].append(b)
    triangles[row].append(c)
    row += 1

triangle = []
count = 0
for x in range(3):
    for y in range(len(triangles)):
        triangle.append(triangles[y][x])
        if len(triangle) == 3:
            print(triangle)
            a = triangle[0]
            b = triangle[1]
            c = triangle[2]
            if isTriangle(a, b, c):
                count += 1
            triangle = []
print(count)
