
#import sqlite3
from directions import *
#from pieceCheck import pieceCheck

import random
import pygame
from pygame import *
from sys import exit



pygame.init()
clock = pygame.time.Clock() #used to determine the fps of the game

opscrn = pygame.display.set_mode((1300, 600)) #setting the dimensions for the game options window
pygame.display.set_caption("Ludo Game Options")#setting the title of the game options window

optionsText = pygame.font.Font("Pixellari.ttf", 70)
#stating what the properties of the text will be so font and font size
textSurface = optionsText.render("SELECT YOUR OPTIONS", False, (131, 202, 180))
#what the text will be and telling the program the colour of the text

optionsTextS = pygame.font.Font("PIXELLARI.TTF", 35)
#same as above, this text is later rendered onto the screen
textSurfaceS = optionsTextS.render("Select number of players first", False, (131, 202, 180))


bluePlayer = False
redPlayer = False
greenPlayer = False
yelPlayer = False
botPlayer = False
startGame = False


class PlayerImgs(pygame.sprite.Sprite):
    def __init__(self, picPath, posX, posY):
        super(PlayerImgs, self).__init__()
        self.image = pygame.image.load(picPath)
        self.posX = posX
        self.posY = posY

    @property
    def rect(self):
        return self.image.get_rect(topleft=(self.posX, self.posY))


##the button group
blueButton = PlayerImgs("blueImg.png", 50, 200)
#creating an instance and assigning it to a variable
#so blueImg.png is picpath, 50 is posX and 200 is posY
#same applies to all the ones below

PlayerImgs_group = pygame.sprite.Group()
#here i am creating a sprite group and will have all the imgs/buttons grouped together
PlayerImgs_group.add(blueButton)
#this adds the instance i created above into the group.

redButton = PlayerImgs("redImg.png", 350, 200)
PlayerImgs_group.add(redButton)

greenButton = PlayerImgs("greenImg.png", 650, 200)
PlayerImgs_group.add(greenButton)

yelButton = PlayerImgs("yellowImg.png", 950, 200)
PlayerImgs_group.add(yelButton)

TwoPButton = PlayerImgs("2Pimg.png", 50, 350)
PlayerImgs_group.add(TwoPButton)

ThreePButton = PlayerImgs("3Pimg.png", 350, 350)
PlayerImgs_group.add(ThreePButton)

FourPButton = PlayerImgs("4Pimg.png", 650, 350)
PlayerImgs_group.add(FourPButton)

BotPButton = PlayerImgs("botButtonImg.png", 950, 350)
PlayerImgs_group.add(BotPButton)

playerNum = 0 #the number of players that will be in the game
players = [] #adds those players into an array


while startGame == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if len(players) >= 1: #to make sure that the user has selected how many players there will be
                startGame = True #This will close the game window by exiting the while loop

            else:
                print("Please select a player or some colours before exiting the game") #to let the user know they haven't selected
                #any number of players

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if TwoPButton.rect.collidepoint(pos):
                print("2 players selected")
                playerNum = 2

            if ThreePButton.rect.collidepoint(pos):
                print("3 players selected")
                playerNum = 3

            if FourPButton.rect.collidepoint(pos):
                print("4 players selected")
                playerNum = 4

            if (
                redButton.rect.collidepoint(pos)
                and playerNum != len(players)
                and redPlayer == False
            ):
                redPlayer = True
                print("Red Player Select")
                players.append("Red")
                print(playerNum - len(players), "more players can be selected")

            if (
                greenButton.rect.collidepoint(pos)
                and playerNum != len(players)
                and greenPlayer == False
            ):
                greenPlayer = True
                print("Green Player Select")
                players.append("Green")
                print(playerNum - len(players), "more players can be selected")

            if (
                blueButton.rect.collidepoint(pos)
                and playerNum != len(players)
                and bluePlayer == False
            ):
                bluePlayer = True
                print("Blue Player Select")
                players.append("Blue")
                print(playerNum - len(players), "more players can be selected")

            if (
                yelButton.rect.collidepoint(pos)
                and playerNum != len(players)
                and yelPlayer == False
            ):
                yelPlayer = True
                print("Yellow Player Select")
                players.append("Yellow")
                print(playerNum - len(players), "more players can be selected")

            if (
                BotPButton.rect.collidepoint(pos)
                and playerNum != len(players)
                and botPlayer == False
            ):
                botPlayer = True
                print("Bot Player Select")
                players.append("Bot")
                print(playerNum - len(players), "more players can be selected")

    #opscrn is the name of variable that the window is assigned to
    opscrn.fill((7, 15, 41))
    #this fills the screen with this colour in the background
    PlayerImgs_group.draw(opscrn)
    #this renders all the images in the sprite group onto the screen
    opscrn.blit(textSurface, (250, 50))
    #this attaches the text i assigned above to these coordinates
    opscrn.blit(textSurfaceS, (400, 120))
    pygame.display.flip()
    #this tells the program to change the display to show the new changes
    clock.tick(10)
    #this tells the program how many times to carry out the code above in a second


#---------------------------------------------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((1500, 720), pygame.RESIZABLE)
pygame.display.set_caption("Ludo Game")
clock = pygame.time.Clock()

class Pieces(pygame.sprite.Sprite):
    def __init__(self, picPath, posX, posY, name):
        super(Pieces, self).__init__()
        self.image = pygame.image.load(picPath)
        self.posX = posX
        self.posY = posY
        self.name = name

    @property
    def rect(self):
        return self.image.get_rect(topleft=(self.posX, self.posY))

ludoBImg = pygame.image.load("ludoBoard2.png")
ludoBImg = pygame.transform.scale(ludoBImg, (780, 720))

global pieceX, pieceY, pieceLoc, pieceCounter, startX, startY

pieceX = [
         [650, 547, 600, 600], #x coordinates for all red pieces
         [134, 83, 188, 133], #x coordinates for all green pieces
         [600, 600, 548, 652], #x coordinates for all blue pieces
         [136, 136, 85, 185] #x coordinates for all yellow pieces
]

pieceY = [
         [122, 122, 73, 170],  #y coordinates for all red pieces
         [75, 123, 122, 170],  #y coordinates for all green pieces
         [507, 602, 555, 555], #y coordinates for all blue pieces
         [508, 603, 555, 555]  #y coordinates for all yellow pieces
]


pieceLoc = [
           ["h", "h", "h", "h"], #holds the location status for all red peices
           ["h", "h", "h", "h"], #holds the location status for all green peices
           ["h", "h", "h", "h"], #holds the location status for all blue peices
           ["h", "h", "h", "h"]  #holds the location status for all yellow peices
]

pieceCounter = [
         [0, 0, 0, 0], #holds the counter for all red peices
         [0, 0, 0, 0], #holds the counter for all green peices
         [0, 0, 0, 0], #holds the counter for all blue peices
         [0, 0, 0, 0]  #holds the counter for all yellow peices
]

startX = [417,55,676,314] #holds the x coordinates for different colour pieces where index follows same order as above
startY = [51,291,386,625] #holds the y coordinates for different colour pieces where index follows same order as above

PiecesGroup = pygame.sprite.Group()


for i in range(len(players)):
    if players[i] == "Red":
        
        redP0 = Pieces("red.png", pieceX[0][0], pieceY[0][0], "redP0")
        PiecesGroup.add(redP0)

        
        redP1 = Pieces("red.png", pieceX[0][1], pieceY[0][1], "redP1")
        PiecesGroup.add(redP1)

        
        redP2 = Pieces("red.png", pieceX[0][2], pieceY[0][2], "redP2")
        PiecesGroup.add(redP2)

        
        redP3 = Pieces("red.png", pieceX[0][3], pieceY[0][3], "redP3")
        PiecesGroup.add(redP3)

        ###################

    if players[i] == "Green":
        
        greenP0 = Pieces("green.png", pieceX[1][0], pieceY[1][0], "greenP0")
        PiecesGroup.add(greenP0)

        
        greenP1 = Pieces("green.png", pieceX[1][1], pieceY[1][1], "greenP1")
        PiecesGroup.add(greenP1)

        
        greenP2 = Pieces("green.png", pieceX[1][2], pieceY[1][2], "greenP2")
        PiecesGroup.add(greenP2)

        
        greenP3 = Pieces("green.png", pieceX[1][3], pieceY[1][3], "greenP3")
        PiecesGroup.add(greenP3)

        ####################

    if players[i] == "Blue":
        
        blueP0 = Pieces("blue.png", pieceX[2][0], pieceY[2][0], "blueP0")
        PiecesGroup.add(blueP0)
        
        blueP1 = Pieces("blue.png", pieceX[2][1], pieceY[2][1], "blueP1")
        PiecesGroup.add(blueP1)
        
        blueP2 = Pieces("blue.png", pieceX[2][2], pieceY[2][2], "blueP2")
        PiecesGroup.add(blueP2)
        
        blueP3 = Pieces("blue.png", pieceX[2][3], pieceY[2][3], "blueP3")
        PiecesGroup.add(blueP3)

        ####################

    if players[i] == "Yellow":
        yelP0 = Pieces("yel.png", pieceX[3][0], pieceY[3][0], "yelP0")
        PiecesGroup.add(yelP0)
        
        yelP1 = Pieces("yel.png", pieceX[3][1], pieceY[3][1], "yelP1")
        PiecesGroup.add(yelP1)
        
        yelP2 = Pieces("yel.png", pieceX[3][2], pieceY[3][2], "yelP2")
        PiecesGroup.add(yelP2)
        
        yelP3 = Pieces("yel.png", pieceX[3][3], pieceY[3][3], "yelP3")
        PiecesGroup.add(yelP3)


rollButton = Pieces("rollButton.png", 1000, 180, "Roll")
PiecesGroup.add(rollButton)


def diceRoll():
    rolls = []
    rollSix = 0
    reRoll = True

    while reRoll == True:
        numberRolled = random.randint(1,6)

        if numberRolled != 6:
            reRoll = False
            rolls.append(numberRolled)

        elif numberRolled == 6:
            if rollSix == 3:
                print("You rolled 6 three times")
                rolls = []
                reRoll = False

            else:
                rolls.append(numberRolled)
                rollSix += 1

    return rolls

def movement(name, rolled, index):
    global pieceX
    global pieceY
    global pieceLoc
    global pieceCounter
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

    print(index,": is the index")
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
                    pieceX[index][pieceN[0]] = pieceX[index][pieceN[0]] - 52
                    print("did dl thingy on ", name)

                add(name, False)



            pieceCounter[index][pieceN[0]] += rolled[i]

        
        elif pieceLoc[index][pieceN[0]] == "h":
            pieceX[index][pieceN[0]] = startX[index]
            pieceY[index][pieceN[0]] = startY[index]
            pieceLoc[index][pieceN[0]] = "b"
            print(name, " coordiantes changed to starting position")


def add(spriteName, starting):
    global redP0
    global redP1
    global redP2
    global redP3

    global greenP0
    global greenP1
    global greenP2
    global greenP3

    global blueP0
    global blueP1
    global blueP2
    global blueP3

    global yelP0
    global yelP1
    global yelP2
    global yelP3

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

    elif spriteName == "greenP0":
        PiecesGroup.remove(greenP0)
        greenP0 = Pieces("green.png", pieceX[1][0], pieceY[1][0], "greenP0")
        PiecesGroup.add(greenP0)
        
    elif spriteName == "greenP1":
        PiecesGroup.remove(greenP1)
        greenP1 = Pieces("green.png", pieceX[1][1], pieceY[1][1], "greenP1")
        PiecesGroup.add(greenP1)

    elif spriteName == "greenP2":
        PiecesGroup.remove(greenP2)
        greenP2 = Pieces("green.png", pieceX[1][2], pieceY[1][2], "greenP2")
        PiecesGroup.add(greenP2)

    elif spriteName == "greenP3":
        PiecesGroup.remove(greenP3)
        greenP3 = Pieces("green.png", pieceX[1][3], pieceY[1][3], "greenP3")
        PiecesGroup.add(greenP3)

    elif spriteName == "blueP0":
        PiecesGroup.remove(blueP0)
        blueP0 = Pieces("blue.png", pieceX[2][0], pieceY[2][0], "blueP0")
        PiecesGroup.add(blueP0)

    elif spriteName == "blueP1":
        PiecesGroup.remove(blueP1)
        blueP1 = Pieces("blue.png", pieceX[2][1], pieceY[2][1], "blueP1")
        PiecesGroup.add(blueP1)

    elif spriteName == "blueP2":
        PiecesGroup.remove(blueP2)
        blueP2 = Pieces("blue.png", pieceX[2][2], pieceY[2][2], "blueP2")
        PiecesGroup.add(blueP2)
 
    elif spriteName == "blueP3":
        PiecesGroup.remove(blueP3)
        blueP3 = Pieces("blue.png", pieceX[2][3], pieceY[2][3], "blueP3")
        PiecesGroup.add(blueP3)

    elif spriteName == "yelP0":
        PiecesGroup.remove(yelP0)
        yelP0 = Pieces("yel.png", pieceX[3][0], pieceY[3][0], "yelP0")
        PiecesGroup.add(yelP0) 

    elif spriteName == "yelP1":
        PiecesGroup.remove(yelP1)
        yelP1 = Pieces("yel.png", pieceX[3][1], pieceY[3][1], "yelP1")
        PiecesGroup.add(yelP1)

    elif spriteName == "yelP2":
        PiecesGroup.remove(yelP2)
        yelP2 = Pieces("yel.png", pieceX[3][2], pieceY[3][2], "yelP2")
        PiecesGroup.add(yelP2)

    elif spriteName == "yelP3":
        PiecesGroup.remove(yelP3)
        yelP3 = Pieces("yel.png", pieceX[3][3], pieceY[3][3], "yelP3")
        PiecesGroup.add(yelP3)

    PiecesGroup.draw(screen)

    print(spriteName, " moved to a new position on the board")
    

rolls = [0]
rollsRemaining = 0
playerQueueNum = 0
dicerolled = False
turndone = True
gameFinished = False

gameWindowPlayer = pygame.font.Font("PIXELLARI.TTF", 40)
gameWindowPlayerSurface = gameWindowPlayer.render("f", False, (131, 202, 180))

rolledText = pygame.font.Font("PIXELLARI.TTF", 30)
rolledTextS = rolledText.render("f", False, (131, 202, 180))

rollText = pygame.font.Font("PIXELLARI.TTF", 30)
rollTextS = rolledText.render("", False, (131, 202, 180))

def highscore():
    pass
    #need this for nea marks
    #time how long the game goes on
    #the shortest time is the high score
    #save into a file
    #tell user if they beat the time
    #only save high score nothing else




while gameFinished == False:
    gameWindowPlayerSurface = gameWindowPlayer.render(players[playerQueueNum].upper() + " SHOULD BE ROLLING", False, (131, 202, 180))
    rolledTextS = rolledText.render(players[playerQueueNum].upper()+" PLAYER CAN USE THE ROLL :", False, (131, 202, 180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if rollButton.rect.collidepoint(pos) and rollsRemaining == 0 and turndone == True:
                print("Rolling")
                rolls = diceRoll()
                dicerolled = True
                turndone = False
                rollsRemaining = len(rolls)
                pygame.time.wait(1000)
                print("You rolled", rolls)
                #gameWindowPlayerSurface = gameWindowPlayer.render(str(players[playerQueueNum]) + " player click on a piece to move it!", False, (0, 0, 0))
                onBoard = (pieceCheck(players[playerQueueNum], pieceLoc))

                try:
                    if onBoard[0] == 4 and rolls[0] != 6:
                        #gameWindowPlayerSurface = gameWindowPlayer.render("You have no pieces on the board moving onto the next player", False, (0, 0, 0))
                        dicerolled = False
                        turndone = True
                        rollsRemaining = 0
                        rolls = [0]
                        if rollsRemaining == 0 and turndone == True:
                            playerQueueNum += 1
                            print("Incremented playerQueueNum")
                            if playerQueueNum > len(players)-1:
                                print("playerQueueNum set to 0")
                                playerQueueNum = 0

                except IndexError:
                    print("rolls list is empty")

            for s in PiecesGroup:
                if s.rect.collidepoint(pos):
                    print("Clicked on a sprite")
                    print(s.name)



    while turndone == False:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                try:
                    print (turndone, ": is turndone")
                    print (players[playerQueueNum],"is the player quing")

                    if redP0.rect.collidepoint(pos) and players[playerQueueNum].lower() == "red" and turndone == False:
                        movement(redP0.name, rolls, 0)
                        add(redP0.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        PiecesGroup.draw(screen)


                    elif redP1.rect.collidepoint(pos) and players[playerQueueNum].lower() == "red" and turndone == False:
                        movement(redP1.name, rolls, 0)
                        add(redP1.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        PiecesGroup.draw(screen)

                    elif redP2.rect.collidepoint(pos) and players[playerQueueNum].lower() == "red" and turndone == False:
                        movement(redP2.name, rolls, 0)
                        add(redP2.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        PiecesGroup.draw(screen)

                    elif redP3.rect.collidepoint(pos) and players[playerQueueNum].lower() == "red" and turndone == False:
                        movement(redP3.name, rolls, 0)
                        add(redP3.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                except NameError:
                    print("red NameError")

                try:
                    if greenP0.rect.collidepoint(pos) and players[playerQueueNum].lower() == "green" and turndone == False:
                        movement(greenP0.name, rolls, 1)
                        add(greenP0.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if greenP1.rect.collidepoint(pos) and players[playerQueueNum].lower() == "green" and turndone == False:
                        movement(greenP1.name, rolls, 1)
                        add(greenP1.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if greenP2.rect.collidepoint(pos) and players[playerQueueNum].lower() == "green" and turndone == False:
                        movement(greenP2.name, rolls, 1)
                        add(greenP2.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if greenP3.rect.collidepoint(pos) and players[playerQueueNum].lower() == "green" and turndone == False:
                        movement(greenP3.name, rolls, 1)
                        add(greenP3.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                except NameError:
                    print("Green NameError")

                try:

                    if blueP0.rect.collidepoint(pos) and players[playerQueueNum].lower() == "blue" and turndone == False:
                        movement(blueP0.name, rolls, 2)
                        add(blueP0.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if blueP1.rect.collidepoint(pos) and players[playerQueueNum].lower() == "blue" and turndone == False:
                        movement(blueP1.name, rolls, 2)
                        add(blueP1.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if blueP2.rect.collidepoint(pos) and players[playerQueueNum].lower() == "blue" and turndone == False:
                        movement(blueP2.name, rolls, 2)
                        add(blueP2.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if blueP3.rect.collidepoint(pos) and players[playerQueueNum].lower() == "blue" and turndone == False:
                        movement(blueP3.name, rolls, 2)
                        add(blueP3.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                except NameError:
                    print("Blue NameError")


                try:
                    if yelP0.rect.collidepoint(pos) and players[playerQueueNum].lower() == "yellow" and turndone == False:
                        movement(yelP0.name, rolls, 3)
                        add(yelP0.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if yelP1.rect.collidepoint(pos) and players[playerQueueNum].lower() == "yellow" and turndone == False:
                        movement(yelP1.name, rolls, 3)
                        add(yelP1.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if yelP2.rect.collidepoint(pos) and players[playerQueueNum].lower() == "yellow" and turndone == False:
                        movement(yelP2.name, rolls, 3)
                        add(yelP2.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)

                    if yelP3.rect.collidepoint(pos) and players[playerQueueNum].lower() == "yellow" and turndone == False:
                        movement(yelP3.name, rolls, 3)
                        add(yelP3.name, False)
                        rollsRemaining = 0
                        rolls = [0]
                        turndone = True
                        print("Rolls are",rolls)
                        print("Rolls Reaminging:",rollsRemaining)
                        PiecesGroup.draw(screen)
                except NameError:
                    print("Yellow NameError")


        if rollsRemaining == 0 and turndone == True:
            playerQueueNum += 1
            print("Incremented playerQueueNum")
            if playerQueueNum > len(players)-1:
                print("playerQueueNum set to 0")
                playerQueueNum = 0


    
    screen.fill((7, 15, 41))
    screen.blit(ludoBImg, (0, 0))
    screen.blit(gameWindowPlayerSurface, (850, 350))
    screen.blit(rolledTextS, (850, 450))
    screen.blit(rollTextS, (850, 550))
    PiecesGroup.draw(screen)
    pygame.display.update()
    clock.tick(10)



