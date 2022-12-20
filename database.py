def playerUserNames():
    #get the name for each player that has been selected
    #create the database or open it
    #add their name to the database
    #it should contain the name of the player
    #the name should all be in capital
    #it should store how many wins they have
    #increase their wins when the game ends if they end up winning
    #save the database as a file as a csv so data can be manipulated and create outputs on the game window.
    
    playerData = sqlite3.connect('playerData.db')
    print("Opened database")
    playerData.execute('''CREATE TABLE PLAYER
    (ID STRING PRIMARY TEXT   NOT NULL,
    NAME               TEXT     NOT NULL,
    LASTC               TEXT    NOT NULL,
    WINS                INT     NOT NULL;
    ''')
    
    playerData.execute()
    print("Created database")
    playerData.executescript('''
    INSERT INTO PLAYER (ID,NAME,WINS) VALUES
    (1,'sabhsbahbsa','RED',4),
    (2, 'dinsag','YELLOW',412);
    ''')

    print("Added items into database")
    result = playerData.fetchall()
    print(result)