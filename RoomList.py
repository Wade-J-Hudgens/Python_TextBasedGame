from Room import Room

class RoomList:
    hallway_4way = Room(0, "Hallway Intersection", 1, 1, 1, 1, u'\u256C')
    hallway_3way_northClosed = Room(1, "Hallway Intersection", 0, 1, 1, 1, u'\u2566')
    hallway_3way_eastClosed = Room(2, "Hallway Intersection", 1, 0, 1, 1, u'\u2563')
    hallway_3way_southClosed = Room(3, "Hallway Intersection", 1, 1, 0, 1, u'\u2569')
    hallway_3way_westClosed = Room(4, "Hallway Intersection", 1, 1, 1, 0, u'\u2560')
    hallway_2way_northSouth = Room(5, "Hallway", 1, 0, 1, 0, u'\u2551')
    hallway_2way_eastWest = Room(6, "Hallway", 0, 1, 0, 1, u'\u2550')
    hallway_turn_northEast = Room(7, "Hallway", 1, 1, 0, 0, u'\u255A')
    hallway_turn_eastSouth = Room(8, "Hallway", 0, 1, 1, 0, u'\u2554')
    hallway_turn_southWest = Room(9, "Hallway", 0, 0, 1, 1, u'\u2557')
    hallway_turn_westNorth = Room(10, "Hallway", 1, 0, 0, 1, u'\u255D')
    room_northOpen = Room(11, "Room", 1, 0, 0, 0, u'\u2568')
    room_eastOpen = Room(12, "Room", 0, 1, 0, 0, u'\u255E')
    room_southOpen = Room(13, "Room", 0, 0, 1, 0, u'\u2565')
    room_westopen = Room(14, "Room", 0, 0, 0, 1, u'\u2561')

    RoomListArr = [
        hallway_4way,
        hallway_3way_northClosed,
        hallway_3way_eastClosed,
        hallway_3way_southClosed,
        hallway_3way_westClosed,
        hallway_2way_northSouth,
        hallway_2way_eastWest,
        hallway_turn_northEast,
        hallway_turn_eastSouth,
        hallway_turn_southWest,
        hallway_turn_westNorth,
        room_northOpen,
        room_eastOpen,
        room_southOpen,
        room_westopen
    ]

    @staticmethod
    def GetRoomFromId(id):
        for i in RoomList.RoomListArr:
            if id == i.id:
                return i
        return None

    @staticmethod
    def PossibleRoomsFromDoors(doorNorth, doorEast, doorSouth, doorWest):
        returnValue = []
        for i in RoomList.RoomListArr:
            if doorNorth == 2 or doorNorth == i.doorNorth:
                if doorEast == 2 or doorEast == i.doorEast:
                    if doorSouth == 2 or doorSouth == i.doorSouth:
                        if doorWest == 2 or doorWest == i.doorWest:
                            returnValue.append(i)
        return returnValue