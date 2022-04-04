import Board
import Search
import time

### Algoritma utama
fileName = str(input("Input starting puzzle file name: "))
Board.inputPuzzle(fileName)
Search.updateSearch()

pick = input("Randomize puzzle board? *not recommended* [Y/N]: ")
if pick in ["Y","y"]:
    Board.randomize()
    print("The puzzle board has been randomized")
else:
    pass

Board.displayScore()

if Board.isReachable()[0]:

    ## Searching
    start = time.time()
    Search.expand(Search.activeNodes[0])
    while not Search.foundFinal:
        Search.expand(Search.activeNodes[Search.bestNodeIdx()])   
    Search.getSolution()
    end = time.time()

    ## Display solution
    for i in Search.solution:
        if i == "SOLVED":
            print(i, "dalam", round(end-start, 100)*1000, "milliseconds")
            print("Jumlah simpul dalam pohon ruang status:", len(Search.allStates))
        else:
            for j in range(16):
                if j in [3,7,11,15]:
                    if i[j] < 10:
                        print("0"+str(i[j]))
                    else:
                        if i[j] == 16:
                            print("  ")
                        else:
                            print(i[j])
                else:
                    if i[j] < 10:
                        print("0"+str(i[j]), end=" ")
                    else:
                        if i[j] == 16:
                            print("  ", end=" ")
                        else:
                            print(i[j], end=" ")
            print()