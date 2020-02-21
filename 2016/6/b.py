messages = open('input', 'r').read().strip().split('\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

messageLength = len(messages[0])
columns = []
for i in range(messageLength):
    columns.append('')

for message in messages:
    for i in range(messageLength):
        columns[i] += message[i]

message = ''
for column in columns:
    frequency = {}
    for letter in alphabet:
        count = column.count(letter)
        if count == 0:
            continue
        pool = frequency.get(count, [])
        pool.append(letter)
        frequency[count] = pool
    keys = list(frequency.keys())
    keys.sort()
    message += frequency.get(keys[0])[0]

print(message)
