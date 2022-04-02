### Algoritma pencarian solusi
import Board
import copy

## Important Variables
root = Board.board
final = Board.target
foundFinal = False
solution = []
activeNodes = [[root]]
activeCost = [999]
allStates = [root]

## Moving methods
def moveUp(board):
    blank = board.index(16)
    board[blank] = board[blank-4]
    board[blank-4] = 16

def moveDown(board):
    blank = board.index(16)
    board[blank] = board[blank+4]
    board[blank+4] = 16

def moveRight(board):
    blank = board.index(16)
    board[blank] = board[blank+1]
    board[blank+1] = 16

def moveLeft(board):
    blank = board.index(16)
    board[blank] = board[blank-1]
    board[blank-1] = 16

## Cost methods
def cost(src, dst):
    count = 0
    for i in range(16):
        if src[i] != 16:
            if src[i] != dst[i]:
                count += 1
    return count

def totalCost(node):
    return (cost(root,node)) + (cost(node,final))

## Expand method
def expand(node):
    state = copy.deepcopy(node[-1])
    global foundFinal

    if state.index(16)-4 >= 0:
        tempState = copy.deepcopy(state)
        tempNode = copy.deepcopy(node)
        moveUp(tempState)
        if tempState not in allStates:
            allStates.append(tempState)
            tempNode.append(tempState)
            if tempState == final:
                foundFinal = True
                tempNode.append("SOLVED")
            activeNodes.append(tempNode)
            activeCost.append(totalCost(tempState))
    
    if state.index(16) not in [3,7,11,15]:
        tempState = copy.deepcopy(state)
        tempNode = copy.deepcopy(node)
        moveRight(tempState)
        if tempState not in allStates:
            allStates.append(tempState)
            tempNode.append(tempState)
            if tempState == final:
                foundFinal = True
                tempNode.append("SOLVED")
            activeNodes.append(tempNode)
            activeCost.append(totalCost(tempState))

    if state.index(16)+4 <= 15:
        tempState = copy.deepcopy(state)
        tempNode = copy.deepcopy(node)
        moveDown(tempState)
        if tempState not in allStates:
            allStates.append(tempState)
            tempNode.append(tempState)
            if tempState == final:
                foundFinal = True
                tempNode.append("SOLVED")
            activeNodes.append(tempNode)
            activeCost.append(totalCost(tempState))

    if state.index(16) not in [0,4,8,12]:
        tempState = copy.deepcopy(state)
        tempNode = copy.deepcopy(node)
        moveLeft(tempState)
        if tempState not in allStates:
            allStates.append(tempState)
            tempNode.append(tempState)
            if tempState == final:
                foundFinal = True
                tempNode.append("SOLVED")
            activeNodes.append(tempNode)
            activeCost.append(totalCost(tempState))

    del activeCost[activeNodes.index(node)]
    activeNodes.remove(node)
        
def bestNodeIdx():
    return activeCost.index(min(activeCost))

def getSolution():
    global solution
    for i in activeNodes:
        if i[-1] == "SOLVED":
            solution = i