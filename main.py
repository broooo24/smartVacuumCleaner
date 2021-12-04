# + done; c chair;i iphone; u unreached
# chair - can not be cleared only its position
# iphone -can not be cleared its position plus ups and downs
matrix = [[' ', ' ', ' '], [' ', 'c', ' '], ['i', ' ', ' '], [' ', ' ', ' ']]

iphoneListx = []
iphoneListy = []
iphoneAreax = []
iphoneAreay = []
chairListx = []
chairListy = []
lengthHorizontal = len(matrix)
lengthVertical = len(matrix[0])
filledMatrix = [['+', '+', '+'], ['+', '+', '+'],
                ['+', '+', '+'], ['+', '+', '+']]


def findChairPosition(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 'c':
                currentRow = i
                currentColumn = j
                chairListx.append(currentRow)
                chairListy.append(currentColumn)


def findIphonePosition(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 'i':
                currentRow = i
                currentColumn = j
                iphoneListy.append(currentRow)
                iphoneListx.append(currentColumn)


def findIphoneArea(currentRow, currentColumn):
    i = 0
    while i < len(currentRow):
        # iphone is not in the first line
        if(currentRow[i] > 0):
            row = currentRow[0]-1
            column = currentColumn[0]
            iphoneAreax.append(column)
            iphoneAreay.append(row)
        # iphone is not in the last line
        if(currentRow[i] < lengthHorizontal):
            row = currentRow[0]+1
            column = currentColumn[0]
            iphoneAreax.append(column)
            iphoneAreay.append(row)
        i = i + 1


def fillUnreachedIphone():
    for y, x in zip(iphoneAreay, iphoneAreax):
        filledMatrix[y][x] = 'u'
    for y, x in zip(iphoneListy, iphoneListx):
        filledMatrix[y][x] = 'u'


def fillUnreachedChair():
    for y, x in zip(chairListy, chairListx):
        filledMatrix[y][x] = 'u'


print(filledMatrix)
findChairPosition(matrix)
print(chairListx)
print(chairListy)
findIphonePosition(matrix)
print("iphone x: ", iphoneListx)
print("iphone y: ", iphoneListy)

findIphoneArea(iphoneListy, iphoneListx)

print("iphone area y: ", iphoneAreay)
print("iphone area x: ", iphoneAreax)


fillUnreachedIphone()
fillUnreachedChair()
print(filledMatrix)
