from RoomList import RoomList
from Room import Room
from random import randrange

class Map:
    map = []        # A 2D integer array representing the map. Each value represents a room Id
    size = 0        # The size of the map

    '''
    This function will generate a map at the desired difficulty.
    Parameters {
        self: Represents the current Map object. Will not be set while calling the function.
        difficulty [integer]: Represents the difficulty.
    }
    This function will return None
    '''
    def GenerateMap(self, difficulty):
        mapSize = 0
        if difficulty == 0:
            mapSize = 5
        if difficulty == 1:
            mapSize = 9
        if difficulty == 2:
            mapSize = 15
        self.map = [[-1 for i in range(mapSize)] for j in range(mapSize)]
        self.size = mapSize

        center = int((mapSize - 1) / 2)
        self.map[center][center] = 0
        self.GenerateSection(center, center)
    
    '''
    This function is a recursive function that will generate a spot on the map at position (x, y) and the surrounding rooms.
    Parameters {
        self: Represents the current Map object. Will not be set while calling the function.
        x: The x position to generate
        y: The y position to generate
    }
    This function will return None
    '''
    def GenerateSection(self, x, y):
        roomSection = RoomList.GetRoomFromId(self.map[x][y])

        dNorth, dEast, dSouth, dWest = 0, 0, 0, 0
        if roomSection.doorNorth == 1 and self.map[x][y+1] == -1:
            dSouth = 1

            if self.CheckIndex(x, y+2) == 1:
                if self.map[x][y+2] == -1:
                    dNorth = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x][y+2])
                    if neighboringRoom.doorSouth == 1:
                        dNorth = 1

            if self.CheckIndex(x+1, y+1) == 1:
                if self.map[x+1][y+1] == -1:
                    dEast = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x+1][y+1])
                    if neighboringRoom.doorWest == 1:
                        dEast = 1
            
            if self.CheckIndex(x-1, y+1) == 1:
                if self.map[x-1][y+1] == -1:
                    dWest = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x-1][y+1])
                    if neighboringRoom.doorEast == 1:
                        dWest = 1
            
            PossibleRooms = RoomList.PossibleRoomsFromDoors(dNorth, dEast, dSouth, dWest)
            self.map[x][y+1] = PossibleRooms[randrange(len(PossibleRooms))].id
            self.GenerateSection(x, y+1)

        dNorth, dEast, dSouth, dWest = 0, 0, 0, 0
        if roomSection.doorEast == 1 and self.map[x+1][y] == -1:
            dWest = 1

            if self.CheckIndex(x+1, y+1) == 1:
                if self.map[x+1][y+1] == -1:
                    dNorth = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x+1][y+1])
                    if neighboringRoom.doorSouth == 1:
                        dNorth = 1

            if self.CheckIndex(x+2, y) == 1:
                if self.map[x+2][y] == -1:
                    dEast = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x+2][y])
                    if neighboringRoom.doorWest == 1:
                        dEast = 1
            
            if self.CheckIndex(x+1, y-1) == 1:
                if self.map[x+1][y-1] == -1:
                    dSouth = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x+1][y-1])
                    if neighboringRoom.doorNorth == 1:
                        dSouth = 1
            
            PossibleRooms = RoomList.PossibleRoomsFromDoors(dNorth, dEast, dSouth, dWest)
            self.map[x+1][y] = PossibleRooms[randrange(len(PossibleRooms))].id
            self.GenerateSection(x+1, y)

        dNorth, dEast, dSouth, dWest = 0, 0, 0, 0
        if roomSection.doorSouth == 1 and self.map[x][y-1] == -1:
            dNorth = 1

            if self.CheckIndex(x-1, y-1) == 1:
                if self.map[x-1][y-1] == -1:
                    dWest = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x-1][y-1])
                    if neighboringRoom.doorEast == 1:
                        dWest = 1

            if self.CheckIndex(x+1, y-1) == 1:
                if self.map[x+1][y-1] == -1:
                    dEast = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x+1][y-1])
                    if neighboringRoom.doorWest == 1:
                        dEast = 1
            
            if self.CheckIndex(x, y-2) == 1:
                if self.map[x][y-2] == -1:
                    dSouth = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x][y-2])
                    if neighboringRoom.doorNorth == 1:
                        dSouth = 1
            
            PossibleRooms = RoomList.PossibleRoomsFromDoors(dNorth, dEast, dSouth, dWest)
            self.map[x][y-1] = PossibleRooms[randrange(len(PossibleRooms))].id
            self.GenerateSection(x, y-1)

        dNorth, dEast, dSouth, dWest = 0, 0, 0, 0
        if roomSection.doorWest == 1 and self.map[x-1][y] == -1:
            dEast = 1

            if self.CheckIndex(x-2, y) == 1:
                if self.map[x-2][y] == -1:
                    dWest = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x-2][y])
                    if neighboringRoom.doorEast == 1:
                        dWest = 1

            if self.CheckIndex(x-1, y+1) == 1:
                if self.map[x-1][y+1] == -1:
                    dNorth = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x-1][y+1])
                    if neighboringRoom.doorSouth == 1:
                        dNorth = 1
            
            if self.CheckIndex(x-1, y-1) == 1:
                if self.map[x-1][y-1] == -1:
                    dSouth = 2
                else:
                    neighboringRoom = RoomList.GetRoomFromId(self.map[x-1][y-1])
                    if neighboringRoom.doorNorth == 1:
                        dSouth = 1
            
            PossibleRooms = RoomList.PossibleRoomsFromDoors(dNorth, dEast, dSouth, dWest)
            self.map[x-1][y] = PossibleRooms[randrange(len(PossibleRooms))].id
            self.GenerateSection(x-1, y)

    '''
    This function will check if the desired index exists on the map
    Parameters {
        x: The x index to check
        y: The y index to check
    }
    This function will return 0 for false or 1 for true
    '''
    def CheckIndex(self, x, y):
        if x < 0:
            return 0
        if x >= self.size:
            return 0
        if y < 0:
            return 0
        if y >= self.size:
            return 0
        return 1