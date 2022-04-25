'''
Wade Hudgens
03 / 18 / 2022

This program is a text based adventure game. You have been trapped in the backrooms and need to escape through the
exit door. To do so, you will need to gather all the keys in the map.

The map is randomly generated.

The player will have the option to move throughout the map by using the N, E, S, and W keys to move north, south, east, and west.

To pick up items the player will input I

To quit the game, the player will input Q

To test the game, you can enter 'show map' to display the entire map, and 'show exit' to display the entire exit
'''


from Map import Map
from RoomList import RoomList
from Player import Player
from random import randrange
from ItemList import ItemList
import os
import math

print (r"""

 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌░▌   ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌          ▐░░▌    ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌░▌   ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌ ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                

""")
term_size = os.get_terminal_size()
print (term_size.columns * '=')
print ("Enter your charcters name:", end= ' ')
charactersName = input()
print()

# Player chooses a difficulty level
difficulty = ""
while difficulty != "1" and difficulty != "2" and difficulty != "3":
    print ("Enter 1 for easy")
    print ("Enter 2 for medium")
    print ("Enter 3 for hard")
    print ("Enter your difficulty:", end=" ")
    difficulty = input()
    if difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("\t" + str(difficulty) + " is not a valid difficulty")
difficulty = int(difficulty) - 1

# Generate the map 
m = Map()
m.GenerateMap(difficulty)
player = Player()
player.name = charactersName

exitDoorLocationX = 0
exitDoorLocationY = 0
keys = []

# Generate the exit doors
possibleExitDoorLocations = []
for i in range(m.size-1, -1, -1):
    for j in range(0, m.size):
        mapV = m.map[j][i]
        if mapV == 11 or mapV == 13 or mapV == 13 or mapV == 14:
            appendValue = [j, i]
            possibleExitDoorLocations.append(appendValue)
exitDoorIndex = randrange(len(possibleExitDoorLocations))
exitDoorLocationX = possibleExitDoorLocations[exitDoorIndex][0]
exitDoorLocationY = possibleExitDoorLocations[exitDoorIndex][1]

# Generate the location of all the keys
itemCounter = 0
for i in range(m.size-1, -1, -1):
    for j in range(0, m.size):
        if (j != exitDoorLocationX or i != exitDoorLocationY) and (m.map[j][i] != -1) and (j != math.floor(m.size / 2) or i != math.floor(m.size / 2)):
            appendValue = [j, i, ItemList.ItemListArr[itemCounter].itemId]
            keys.append(appendValue)

            itemCounter += 1
            if itemCounter >= len(ItemList.ItemListArr):
                itemCounter = 0
amountOfKeysToFind = len(keys)

gameRunning = 1         # Determines if the game loop is active
firstIteration = 1      # If it is 1 then it is the first loop of the game
lastRoom = ""           # Is equal to the name of the last room the player was in
showMessage = 0         # Determines if a message should be shown to the player
message = ""            # The message that will be shown to the player
showFullMap = 0         # If it is 1, then the full map will be revealed
showExitGate = 0        # If it is 1, then the exit gate will be revealed

# Set player position equal to the center and start the loop
player.playerX = int((m.size - 1) / 2)
player.playerY = int((m.size - 1) / 2)
player.knownLocations = [[0 for i in range(m.size)] for j in range(m.size)]     # A 2D array which represents the known positions of the player
while gameRunning == 1:
    # The branch determines if the players location is equal to the exit door's location and then determines if the player wins or loses.
    if player.playerX == exitDoorLocationX and player.playerY == exitDoorLocationY:
        if amountOfKeysToFind <= len(player.inventory):
            print(
                "As you walk into this room you notice a door with " + str(amountOfKeysToFind) + " different keyholes. " +
                "As you walk torward the door you realize the door you just came from has vanished. " +
                "Because you have found all " + str(len(player.inventory)) + " keys, you are able open the locked door and " +
                "escape back to reality."
                )
            print()
            print(r"""
            
  ___    ___ ________  ___  ___          ___       __   ___  ________   ___       
 |\  \  /  /|\   __  \|\  \|\  \        |\  \     |\  \|\  \|\   ___  \|\  \      
 \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \    \ \  \ \  \ \  \\ \  \ \  \     
  \ \    / / \ \  \\\  \ \  \\\  \       \ \  \  __\ \  \ \  \ \  \\ \  \ \  \    
   \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \|\__\_\  \ \  \ \  \\ \  \ \__\   
 __/  / /      \ \_______\ \_______\       \ \____________\ \__\ \__\\ \__\|__|   
|\___/ /        \|_______|\|_______|        \|____________|\|__|\|__| \|__|   ___ 
\|___|/                                                                      |\__\
                                                                             \|__|
                                                                                  

            """)
            gameRunning == 0
            break
        else:
            print(
                "As you walk into this room you notice a door with " + str(amountOfKeysToFind) + " different keyholes. " +
                "As you walk torward the door you realize the door you just came from has vanished. " +
                "Because you have only found " + str(len(player.inventory)) + " keys, you are not able to open the locked door. " +
                "You are trapped."
                )
            print()
            print(r"""
            
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   

            """)
            gameRunning == 0
            break

    player.knownLocations[player.playerX][player.playerY] = 1   # Makes the players current location known
    term_size = os.get_terminal_size()
    print (term_size.columns * '=')
    # If it is the first iteration, display an opening sequence
    if (firstIteration == 1):
        print (
            "You wake up to the sound of flourecient buzzing on a damp and cold floor feeling like you have been unconsious for an eternity. " +
            "You stand to your feet to orient yourself and notice your in a place that looks like an empty office. " +
            "The walls are a faded yellow, the carpet is damp, and the place is lit by flourecent lights on the celing. " +
            "You see 4 doors. One on the north wall, the east wall, the south wall, and the west wall."
            )
        print()
    else:
        playersRoom = RoomList.GetRoomFromId(m.map[player.playerX][player.playerY])     # Gets the current room the player is in
        roomType = playersRoom.name
        print("You have found " + str(len(player.inventory)) + " / " + str(amountOfKeysToFind) + " keys.")

        #Prints the players inventory
        print("Inventory: ", end="")
        to_print = ""
        if player.inventory.count(0) > 0:
            to_print += (str(player.inventory.count(0)) + " red key, ")
        if player.inventory.count(1) > 0:
            to_print += (str(player.inventory.count(1)) + " blue key, ")
        if player.inventory.count(2) > 0:
            to_print += (str(player.inventory.count(2)) + " white key, ")
        if player.inventory.count(3) > 0:
            to_print += (str(player.inventory.count(3)) + " black key, ")
        if player.inventory.count(4) > 0:
            to_print += (str(player.inventory.count(4)) + " green key, ")
        if player.inventory.count(5) > 0:
            to_print += (str(player.inventory.count(5)) + " yellow key, ")
        if player.inventory.count(6) > 0:
            to_print += (str(player.inventory.count(6)) + " grey key, ")
        if player.inventory.count(7) > 0:
            to_print += (str(player.inventory.count(7)) + " orange key, ")
        to_print = to_print[:-2]
        print(to_print)

        #This branch will display the known or revealed map
        for i in range(m.size-1, -1, -1):
            for j in range(0, m.size):
                if m.map[j][i] == -1 or (player.knownLocations[j][i] == 0 and showFullMap == 0):
                    print(' ', end='')
                else:
                    if player.playerX == j and player.playerY == i:
                        print(u'\u2573', end='')
                    elif showExitGate == 1 and i == exitDoorLocationY and j == exitDoorLocationX:
                        print(u'\u2588', end='')
                    else:
                        print(RoomList.GetRoomFromId(m.map[j][i]).symbol, end='')
            print()

        if showMessage == 1:        # If a message needs to be displayed, display it.
            print(message)
            print()
            showMessage = 0
        if lastRoom == playersRoom.name:
            print ("You walk into a " + roomType + ".")
        else:
            print ("You are still in a " + roomType + ".")

        #The below branches determine what direction a player can move
        if playersRoom.doorNorth == 1:
            print ("You see a door that heads north.")
        if playersRoom.doorEast == 1:
            print ("You see a door that heads east.")
        if playersRoom.doorSouth == 1:
            print ("You see a door that heads south.")
        if playersRoom.doorWest == 1:
            print ("You see a door that heads west.")
    print()

    N_isValid = 0       # Represents if N is a valid movement
    E_isValid = 0       # Represents if E is a valid movement
    W_isValid = 0       # Represents if W is a valid movement
    S_isValid = 0       # Represents if S is a valid movement
    # Display valid inputs
    print ("\tI: Inspect this room for items")
    if RoomList.GetRoomFromId(m.map[player.playerX][player.playerY]).doorNorth == 1:
        print ("\tN: Go north")
        N_isValid = 1
    if RoomList.GetRoomFromId(m.map[player.playerX][player.playerY]).doorEast == 1:
        print ("\tE: Go east")
        E_isValid = 1
    if RoomList.GetRoomFromId(m.map[player.playerX][player.playerY]).doorSouth == 1:
        print ("\tS: Go south")
        S_isValid = 1
    if RoomList.GetRoomFromId(m.map[player.playerX][player.playerY]).doorWest == 1:
        print ("\tW: Go west")
        W_isValid = 1
    print ("\tQ: QUIT GAME")
    print()
    print("\tSHOW MAP: (Cheat) Shows the entire map")
    print("\tSHOW EXIT: (Cheat) Shows the exit")
    print()
    print ("What do you want to do?")
    print("> ", end=" ")
    inp = input()
    lastRoom = RoomList.GetRoomFromId(m.map[player.playerX][player.playerY]).name

    if inp.upper() == "Q":
        gameRunning = 0
    elif inp.upper() == "I":
        # This branch will iterate over the key array and determine if a location of a key is equal to the players location. If it is, it adds the key to the players inventory.
        for key in keys:
            if key[0] == player.playerX and key[1] == player.playerY:
                player.inventory.append(key[2])
                showMessage = 1
                message = "You have found a " + ItemList.GetItemFromId(key[2]).itemName + "!"
                keys.remove(key)
        if (showMessage == 0):
            showMessage = 1
            message = "You did not find a key."
    elif inp.upper() == "N" and N_isValid == 1:
        player.playerY += 1
    elif inp.upper() == "E" and E_isValid == 1:
        player.playerX += 1
    elif inp.upper() == "S" and S_isValid == 1:
        player.playerY -= 1
    elif inp.upper() == "W" and W_isValid == 1:
        player.playerX -= 1 
    elif inp.upper() == "SHOW MAP":
        showFullMap = 1
    elif inp.upper() == "SHOW EXIT":
        showExitGate = 1
    firstIteration = 0