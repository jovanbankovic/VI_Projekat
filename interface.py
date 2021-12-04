from _common import invalidPreGameParamsMessage, minAmountOfWalls, maxAmountOfWalls

def printStartingPositions(i, j, player1, player2, x):
    myList = (i, j)
    if myList in player1:
        if (j == x - 1):
            print("%1s" % " O", end="")
        else:
            print("%1s" % " O", end=" │")
    elif myList in player2:
        if (j == x - 1):
            print("%1s" % " X", end="")
        else:
            print("%1s" % " X", end=" │")
    else:
        if (j == x - 1):
            print("%1s" % "  ", end="")
        else:
            print("%1s" % " ", end="  │")

def initInterface(x, y, k, player1, player2):
    print("   ", end="")
    for j in range(x):
        print("%4s" % hex(j+1).split('x')[-1].upper(), end="")
    print('    ')
    print("   ", end="")
    for j in range(x):
        print("%4s" % "═", end="")

    for i in range(y):
        print("\n%4s╟" % hex(i+1).split('x')[-1].upper(), end="")
        for j in range(x):
            printStartingPositions(i, j, player1, player2, x)

        print("%2s" % "╢", end="%s" % hex(i+1).split('x')[-1].upper())
        print()
        print("   ", end="")
        if(i < y - 1):
            for j in range(x):
                print("%4s" % "─", end='')

    for j in range(x):
        print("%4s" % "═", end="")

    print()
    print("   ", end="")
    for j in range(x):
        print("%4s" % hex(j+1).split('x')[-1].upper(), end="")


