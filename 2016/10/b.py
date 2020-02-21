instructions = open('input', 'r').read().strip().split('\n')
#instructions = open('input.short', 'r').read().strip().split('\n')

# Goals
HIGH_COMPARE = 61
LOW_COMPARE = 17
# Bot Structure: tuple ([chips], [queued instructions])

# Note - give messages always have low before high
# bot i gives low to bot n and high to bot m
# Positions:
# i = 1
# n = 6
# m = 11
bots = {}

def getBot(identifier):
    return bots.get(identifier, ([],[]))

def giveChip(identifier, chip):
    bot = getBot(identifier)
    bot[0].append(chip)
    print('Gave ' + str(chip) + ' to ' + identifier + '. Has: ' + str(bot[0]))
    if len(bot[0]) > 1:
        while len(bot[1]) > 0:
            queuedInstruction = bot[1].pop(0)
            performInstruction(identifier, queuedInstruction)
    bots[identifier] = bot

def performInstruction(botID, instruction):
    bot = getBot(botID)
    components = instruction.split(' ')
    bot[0].sort()
    low = bot[0].pop(0)
    lowDestination = ''.join(components[5:7])
    #bots.get(lowDestination, ([],[]))[0].append(low)
    print(botID + ' giving ' + str(low) + 'to ' + lowDestination)
    giveChip(lowDestination, low)
    print(botID + ': ' + str(getBot(botID)[0]))
    print(lowDestination + ': ' + str(getBot(lowDestination)[0]))

    high = bot[0].pop()
    highDestination = ''.join(components[10:12])
    #bots.get(highDestination, ([],[]))[0].append(high)
    print(botID + ' giving ' + str(high) + 'to ' + highDestination)
    giveChip(highDestination, high)
    print(botID + ': ' + str(getBot(botID)[0]))
    print(highDestination + ': ' + str(getBot(highDestination)[0]))

    if low == LOW_COMPARE and high == HIGH_COMPARE:
        print(botID)
        #exit()
    bots[botID] = bot

for instruction in instructions:
    components = instruction.split(' ')
    if components[0] == 'value':
        identifier = ''.join(components[-2:])
        #print(identifier)
        chip = int(components[1])
        giveChip(identifier, chip)
    else:
        identifier = ''.join(components[0:2])
        bot = getBot(identifier)
        if len(bot[0]) > 1:
            #print(identifier + ': ' + instruction)
            performInstruction(identifier, instruction)
        else:
            print('Insufficient chips, queueing \'' + instruction + '\'')
            bot[1].append(instruction)
        bots[identifier] = bot

#print(bots)
output0 = getBot('output0')[0][0]
output1 = getBot('output1')[0][0]
output2 = getBot('output2')[0][0]

total = output0 * output1 * output2

print(total)

