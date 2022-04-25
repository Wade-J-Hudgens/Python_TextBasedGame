class Room:
    doorNorth = 0
    doorEast = 0
    doorSouth = 0
    doorWest = 0
    name = ""
    id = -1
    symbol = ""

    def __init__(self, id, name, north, east, south, west, symbol):
        self.doorNorth = north
        self.doorEast = east
        self.doorSouth = south
        self.doorWest = west
        self.name = name
        self.id = id
        self.symbol = symbol