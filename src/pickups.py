
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value, symbol): #Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol
#---------------------------------------------------------------------------------------------------------------------------------------------
#Uppdatering av pickups med value och symboler
pickups = [Item("carrot",20,"C"), Item("apple",20,"A"), Item("strawberry",20,"S"),
           Item("cherry",20,"Y"), Item("watermelon",20,"W"), Item("radish",20,"R"),
           Item("cucumber",20,"B"), Item("meatball",10,"M")]

#---------------------------------------------------------------------------------------------------------------------------------------------
def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

