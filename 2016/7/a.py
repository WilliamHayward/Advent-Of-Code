addresses = open('input', 'r').read().strip().replace(']','[').split('\n')

count = 0

def isABBA(string):
    if string[0] == string[1]:
        return False
    if string[0] == string[-1] and string[1] == string[-2]:
        return True
    print(string)
    return False

def containsABBA(string):
    for i in range(len(string)):
        test = string[i:i+4]
        if len(test) < 4:
            break
        if isABBA(test):
            return True
    return False

def supportsTLS(address):
    components = address.split('[') # Replaced ] with [ in first line
    hypernet = False
    contains = False
    for component in components:
        componentContains = containsABBA(component)
        if componentContains:
            if hypernet:
                return False
            contains = True
        hypernet = not hypernet
    return contains

for address in addresses:
    if supportsTLS(address):
        count += 1
print(count)
