import hashlib
doorID = 'abbhdwsy'
count = 0
password = '________'

while password.count('_') > 0:
    test = doorID + str(count)
    md5 = hashlib.md5()
    md5.update(test.encode('utf-8'))
    testMD5 = md5.hexdigest()
    if testMD5[0:5] == '00000':
        index = testMD5[5]
        if index.isnumeric():
            index = int(index)
            if index < 8 and password[index] == '_':
                password = password[0:index] + testMD5[6] + password[index+1:]
                print(password)
    count += 1



print(password)

