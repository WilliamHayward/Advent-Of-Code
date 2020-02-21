addresses = open('input', 'r').read().strip().replace(']','[').split('\n')

count = 0

def isABA(string):
    if string[0] != string[2]:
        return False
    if string[0] == string[1]:
        return False
    return True

def containsBAB(ABA, hypernets):
    A = ABA[0]
    B = ABA[1]
    BAB = B + A + B
    for hypernet in hypernets:
        if hypernet.count(BAB) > 0:
            return True
    return False

def supportsSSL(address):
    components = address.split('[') # Replaced ] with [ in first line
    hypernet = False
    hypernets = []
    supernets = []
    for component in components:
        if hypernet:
            hypernets.append(component)
        else:
            supernets.append(component)
        hypernet = not hypernet

    supports = False
    for supernet in supernets:
        for i in range(len(supernet)):
            test = supernet[i:i+3]
            if len(test) < 3:
                break
            if isABA(test):
                if containsBAB(test, hypernets):
                    supports = True
    return supports
         
for address in addresses:
    if supportsSSL(address):
        count += 1
print(count)
