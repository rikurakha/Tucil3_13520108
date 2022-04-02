### Dasar-dasar papan puzzle
import random

## Papan puzzle
board = [2,3,7,4,1,5,10,8,6,15,11,12,9,13,14,16]
target = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

## Papan methods
def randomize():
    random.shuffle(board)

def posisi(x):
    return board.index(x)

def kurang(x):
    count = 0
    for i in range(16):
        if i > posisi(x):
            if board[i] < x:
                count += 1
    return count

def isBlankAtGrey():
    res = False
    if posisi(16) in [1,3,4,6,9,11,12,14]:
        res = True
    return res

# returns (bool, total count)
def isReachable():
    res = False
    count = 0
    for i in range(16):
        count += kurang(i+1)
    if (isBlankAtGrey()):
        count += 1
    if count % 2 == 0:
        res = True
    return res, count