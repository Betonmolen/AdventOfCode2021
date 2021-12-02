def calcPosition(line):
    
    forward = 0
    depth = 0
    for i in range(0,len(line)):
        splitline = line[i].split(' ')
        if  splitline[0] == 'forward':
            forward += int(splitline[1])
        elif splitline[0] == 'down':
            depth += int(splitline[1])
        elif splitline[0] == 'up':
            depth -= int(splitline[1])

    
    return forward*depth

def calcPositionAim(line):
    
    forward = 0
    depth = 0
    aim = 0
    for i in range(0,len(line)):
        splitline = line[i].split(' ')
        if  splitline[0] == 'forward':
            forward += int(splitline[1])
            depth += aim * int(splitline[1])
        elif splitline[0] == 'down':
            aim += int(splitline[1])
        elif splitline[0] == 'up':
            aim -= int(splitline[1])
    
    return forward*depth




file = open('input_day2.txt', 'r')
line = file.read().split('\n')
file.close()
result = calcPosition(line)
result2 = calcPositionAim(line)
print(result)
print(result2)