


def add(spriteName):
    if spriteName == "redP0":
        PiecesGroup.remove(redP0)
        redP0 = Pieces("red.png", pieceX[0][0], pieceY[0][0], "redP0")
        PiecesGroup.add(redP0)
        

    if spriteName == "redP1":
        PiecesGroup.remove(redP1)
        redP1 = Pieces("red.png", pieceX[0][1], pieceY[0][1], "redP1")
        PiecesGroup.add(redP1)

    if spriteName == "redP2":
        PiecesGroup.remove(redP2)
        redP2 = Pieces("red.png", pieceX[0][2], pieceY[0][2], "redP2")
        PiecesGroup.add(redP2)

    if spriteName == "redP3":
        PiecesGroup.remove(redP3)
        redP3 = Pieces("red.png", pieceX[0][3], pieceY[0][3], "redP3")
        PiecesGroup.add(redP3)

    if spriteName == "greenP0":
        PiecesGroup.remove(greenP0)
        greenP0 = Pieces("green.png", pieceX[1][0], pieceY[1][0], "greenP0")
        PiecesGroup.add(greenP0)
        
    if spriteName == "greenP1":
        PiecesGroup.remove(greenP1)
        greenP1 = Pieces("green.png", pieceX[1][1], pieceY[1][1], "greenP1")
        PiecesGroup.add(greenP1)

    if spriteName == "greenP2":
        PiecesGroup.remove(greenP2)
        greenP2 = Pieces("green.png", pieceX[1][2], pieceY[1][2], "greenP2")
        PiecesGroup.add(greenP2)

    if spriteName == "greenP3":
        PiecesGroup.remove(greenP3)
        greenP3 = Pieces("green.png", pieceX[1][3], pieceY[1][3], "greenP3")
        PiecesGroup.add(greenP3)

    if spriteName == "blueP0":
        PiecesGroup.remove(blueP0)
        blueP0 = Pieces("blue.png", pieceX[2][0], pieceY[2][0], "blueP0")
        PiecesGroup.add(blueP0)

    if spriteName == "blueP1":
        PiecesGroup.remove(blueP1)
        blueP1 = Pieces("blue.png", pieceX[2][1], pieceY[2][1], "blueP1")
        PiecesGroup.add(blueP1)

    if spriteName == "blueP2":
        PiecesGroup.remove(blueP2)
        blueP2 = Pieces("blue.png", pieceX[2][2], pieceY[2][2], "blueP2")
        PiecesGroup.add(blueP2)
 
    if spriteName == "blueP3":
        PiecesGroup.remove(blueP3)
        blueP3 = Pieces("blue.png", pieceX[2][3], pieceY[2][3], "blueP3")
        PiecesGroup.add(blueP3)

    if spriteName == "yelP0":
        PiecesGroup.remove(yelP0)
        yelP0 = Pieces("yel.png", pieceX[3][0], pieceY[3][0], "yelP0")
        PiecesGroup.add(yelP0) 

    if spriteName == "yelP1":
        PiecesGroup.remove(yelP1)
        yelP1 = Pieces("yel.png", pieceX[3][1], pieceY[3][1], "yelP1")
        PiecesGroup.add(yelP1)

    if spriteName == "yelP2":
        PiecesGroup.remove(yelP2)
        yelP2 = Pieces("yel.png", pieceX[3][2], pieceY[3][2], "yelP2")
        PiecesGroup.add(yelP2)

    if spriteName == "yelP3":
        PiecesGroup.remove(yelP3)
        yelP3 = Pieces("yel.png", pieceX[3][3], pieceY[3][3], "yelP3")
        PiecesGroup.add(yelP3)


    print(spriteName, " moved to a new position on the board")
    PiecesGroup.draw(screen)

    #this subroutine will add sprites into the sprite group
    #this subroutine should check if the piece is being added for the first time or if it is being updated
    #if it is being added for the second time or anything after that the sprite should be removed from the group first and then added back with different coordinates
    #this should also update the screen