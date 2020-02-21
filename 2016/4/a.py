rooms = open('input', 'r').read().strip().split('\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
   
def getChecksum(name):
    counts = {}
    for letter in alphabet:
        count = name.count(letter)
        pool = counts.get(count, [])
        pool.append(letter)
        pool.sort()
        counts[count] = pool
    
    checksum = ''
    print(counts)
    print(counts.keys())
    keys = list(counts.keys())
    keys.sort(reverse=True)
    print(keys)
    
    for key in keys:
        for letter in counts.get(key, []):
            checksum += letter
            if len(checksum) == 5:
                print(checksum)
                return checksum
sectorSum = 0
for room in rooms:
    bigSplit = room.split('[')
    littleSplit = bigSplit[0].rpartition('-')
    
    checksum = bigSplit[1][:-1]
    name = littleSplit[0]
    sector = int(littleSplit[2])
    if checksum == getChecksum(name):
        sectorSum += sector

print(sectorSum)
