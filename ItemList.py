from Item import Item

class ItemList:
    item1 = Item(0, "Red Key")
    item2 = Item(1, "Blue Key")
    item3 = Item(2, "White Key")
    item4 = Item(3, "Black Key")
    item5 = Item(4, "Green Key")
    item6 = Item(5, "Yellow Key")
    item7 = Item(6, "Grey Key")
    item8 = Item(7, "Orange Key")

    ItemListArr = [
        item1, 
        item2, 
        item3, 
        item4, 
        item5, 
        item6, 
        item7, 
        item8
    ]

    @staticmethod
    def GetItemFromId(id):
        for i in ItemList.ItemListArr:
            if id == i.itemId:
                return i
        return None