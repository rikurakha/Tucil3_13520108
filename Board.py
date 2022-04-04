### Dasar-dasar papan puzzle
import copy
import random

from sympy import GoldenRatio

## Papan puzzle
board = []
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

def displayScore():
    global board
    print("\nStarting state:")
    for j in range(16):
        if j in [3,7,11,15]:
            if board[j] < 10:
                print("0"+str(board[j]))
            else:
                if board[j] == 16:
                    print("  ")
                else:
                    print(board[j])
        else:
            if board[j] < 10:
                print("0"+str(board[j]), end=" ")
            else:
                if board[j] == 16:
                    print("  ", end=" ")
                else:
                    print(board[j], end=" ")
    print("\n i | kurang(i)")
    for i in range(16):
        if i+1 < 10:
            print("0"+str(i+1),"|",kurang(i+1))
        else:
            print(str(i+1)+" |",kurang(i+1))
    print("Sigma(kurang(i)) + X =", isReachable()[1])
    if isReachable()[0]:
        print("The puzzle is solvable, solving now...\n")
    else:
        print("The puzzle is not solvable.")
        
def inputPuzzle(textName):
    global board
    with open(textName,"r") as file:
        temp = []
        lines = file.readlines()
        for i in lines:
            as_list = i.split(" ")
            for j in range(4):
                if j == 3:
                    temp.append(int(as_list[3].replace("\n","")))
                else:
                    temp.append(int(as_list[j]))
    board = copy.deepcopy(temp)
    file.close()