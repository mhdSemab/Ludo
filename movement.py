from directions import *



def movement(name, rolled):
    pieceC = "" #piece color
    pieceN = [] #piece num
    check = True 

    counter = 0
    while check == True:
        if name[counter] == "P":
            pieceN.append(int(name[counter+1]))
            check = False
        else:
            pieceC += name[counter]
        counter += 1

    print(pieceC)
    print(pieceN)
    print(name)

    index = 0

    if pieceN == "green":
        index = 1

    elif pieceN == "blue":
        index = 2

    elif pieceN == "yel":
        index = 3

    for i in range(len(rolled)):
        moves = pieceDirections(pieceC, pieceCounter[index][pieceN[0]], rolled[i])
        
        if pieceLoc[index][pieceN[0]] == "b":
            for x in range(len(moves)):
                if moves[x] == "r":
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] + 52
                    print(name," moved right once")

                if moves[x] == "l":
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] - 52
                    print(name," moved left once")

                if moves[x] == "u":
                    pieceY[index][pieceN[0]] = pieceY[index][pieceN[0]] - 48
                    print(name," moved up once")

                if moves[x] == "d":
                    pieceY[index][pieceN[0]] = pieceY[index][pieceN[0]] + 48
                    print(name," moved down once")

                if moves[x] == "ul" or moves[x] == "lu":
                    pieceY[index][pieceN[0]] = pieceY[index][pieceN[0]] - 48
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] - 52
                    print("did ul thingy on ", name)

                if moves[x] == "ru" or moves[x] == "ur":
                    pieceY[index][pieceN[0]] = pieceY[index][pieceN[0]] - 48
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] + 52
                    print("did ru thingy on ", name)

                if moves[x] == "dr" or moves[x] == "rd":
                    pieceY[index][pieceN[0]] = pieceY[index][pieceN[0]] + 48
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] + 52
                    print("did dr thingy on ", name)

                if moves[x] == "dl" or moves[x] == "ld":
                    pieceY[index][pieceN[0]] = pieceY[index][pieceN[0]] + 48
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] + 52
                    print("did dl thingy on ", name)

            pieceCounter[index][pieceN[0]] += rolled[i]

    
        elif pieceLoc[index][pieceN[0]] == "h":
            pieceX[index][pieceN[0]] = startX[index]
            pieceY[index][pieceN[0]] = startY[index]
            pieceLoc[index][pieceN[0]] = "b"
            print(name, " coordiantes changed to starting position")


    #get the the amount the user has rolled
    #using the string slicing to workout which piece needs to be moved
    #move the piece that needs to be moved
    #it should do one move at a time
    #it needs to be able to change the values of the pieces in the array
    #it should also check for the queues so only the person who should be rolling, is rolling
