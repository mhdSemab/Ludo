def pieceDirections(pieceColor, count, rolled):
    #creates an array called moving
    #each peice has its own coutner and the value of the coutner is passed by count it is an array for each piece and colour
    #depending on what the user has rolled, the moves that need to be made are added into the moving list
    #then those values are returned.
    moving = []
    if pieceColor.upper() == "RED":
        directions = [
            "d",
            "d",
            "d",
            "d",
            "dr",
            "r",
            "r",
            "r",
            "r",
            "r",
            "d",
            "d",
            "l",
            "l",
            "l",
            "l",
            "l",
            "ld",
            "d",
            "d",
            "d",
            "d",
            "d",
            "l",
            "l",
            "u",
            "u",
            "u",
            "u",
            "u",
            "ul",
            "l",
            "l",
            "l",
            "l",
            "l",
            "u",
            "u",
            "r",
            "r",
            "r",
            "r",
            "r",
            "ru",
            "u",
            "u",
            "u",
            "u",
            "u",
            "r",
            "d",
            "d",
            "d",
            "d",
            "d",
            "d",
        ]
        
        for i in range(rolled):
            try:
                moving.append(directions[count])
                count += 1
            except IndexError:
                moving.append(directions[count:])
                print ("Rolled a number too big")

    if pieceColor.upper() == "GREEN":
        directions = [
                "r",
                "r",
                "r",
                "r",
                "ru",
                "u",
                "u",
                "u",
                "u",
                "u",
                "r",
                "r",
                "d",
                "d",
                "d",
                "d",
                "d",
                "dr",
                "r",
                "r",
                "r",
                "r",
                "r",
                "d",
                "d",
                "l",
                "l",
                "l",
                "l",
                "l",
                "ld",
                "d",
                "d",
                "d",
                "d",
                "d",
                "l",
                "l",
                "u",
                "u",
                "u",
                "u",
                "u",
                "ul",
                "l",
                "l",
                "l",
                "l",
                "l",
                "u",
                "r",
                "r",
                "r",
                "r",
                "r",
                "r",]

        for i in range(rolled):
            try:
                moving.append(directions[count])
                count += 1
            except IndexError:
                moving.append(directions[count:])
                print ("Rolled a number too big")

    if pieceColor.upper() == "BLUE":
        directions = [
                "l",
                "l",
                "l",
                "l",
                "l",
                "d",
                "d",
                "d",
                "d",
                "d",
                "d",
                "l",
                "l",
                "u",
                "u",
                "u",
                "u",
                "u",
                "u",
                "l",
                "l",
                "l",
                "l",
                "l",
                "l",
                "u",
                "u",
                "r",
                "r",
                "r",
                "r",
                "r",
                "r",
                "u",
                "u",
                "u",
                "u",
                "u",
                "u",
                "r",
                "r",
                "d",
                "d",
                "d",
                "d",
                "d",
                "d",
                "r",
                "r",
                "r",
                "r",
                "r",
                "r",
                "d",
                "l",
                "l",
                "l",
                "l",
                "l",
                "l",
        ]

        for i in range(rolled):
            try:
                moving.append(directions[count])
                count += 1
            except IndexError:
                moving.append(directions[count:])
                print ("Rolled a number too big")

    if pieceColor[0:3].upper() == "YEL":
        directions = [
                "u",
                "u",
                "u",
                "u",
                "u",
                "l",
                "l",
                "l",
                "l",
                "l",
                "l",
                "u",
                "u",
                "r",
                "r",
                "r",
                "r",
                "r",
                "r",
                "u",
                "u",
                "u",
                "u",
                "u",
                "u",
                "r",
                "r",
                "d",
                "d",
                "d",
                "d",
                "d",
                "d",
                "r",
                "r",
                "r",
                "r",
                "r",
                "r",
                "d",
                "d",
                "l",
                "l",
                "l",
                "l",
                "l",
                "l",
                "d",
                "d",
                "d",
                "d",
                "d",
                "d",
                "l",
                "u",
                "u",
                "u",
                "u",
                "u",
                "u",
        ]

        for i in range(rolled):
            try:
                moving.append(directions[count])
                count += 1
            except IndexError:
                moving.append(directions[count:])
                print ("Rolled a number too big")
    
    return moving

    
