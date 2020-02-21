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
    keys = list(counts.keys())
    keys.sort(reverse=True)
    
    for key in keys:
        for letter in counts.get(key, []):
            checksum += letter
            if len(checksum) == 5:
                return checksum

def decode(name, sector):
    decoded = ''
    for letter in name:
        if letter == '-':
            decoded += ' '
            continue
        index = alphabet.find(letter) + sector
        index = index % len(alphabet)
        decoded += alphabet[index]
    return decoded

sectorSum = 0
for room in rooms:
    bigSplit = room.split('[')
    littleSplit = bigSplit[0].rpartition('-')
    
    checksum = bigSplit[1][:-1]
    name = littleSplit[0]
    sector = int(littleSplit[2])
    if checksum == getChecksum(name):
        realName = decode(name, sector)
        if realName.count('north') > 0:
            print(realName)
            print(str(sector))

