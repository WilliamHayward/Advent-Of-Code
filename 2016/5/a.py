import hashlib
doorID = 'abbhdwsy'
count = 0
password = ''

while len(password) < 8:
    test = doorID + str(count)
    md5 = hashlib.md5()
    md5.update(test.encode('utf-8'))
    testMD5 = md5.hexdigest()
    if testMD5[0:5] == '00000':
        print(testMD5[5])
        password += testMD5[5]
    count += 1



print(password)

