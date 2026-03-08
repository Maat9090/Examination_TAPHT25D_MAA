from .grid import Grid
from .player import Player
from . import pickups
from .status import print_status



player = Player(15, 5)     # A.Spelaren ska börja nära mitten av rummet.
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)



command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g,score)

    command = input("Use WASD to move, I for inventory, Q/X to quit ")
    command = command.casefold()[:1]
#------------------------------------------------------------------------------------------
    #Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    if command == "i":
      print("Here is your inventory")
      if not inventory:
          print("Your inventory is empty.")
      for item in inventory:
          print(item.name)

#___________________________________________________________________________________________
#B.Förflyttningar i alla 4 riktningar. (Med tangenterna WASD.)
    if command == "d" and player.can_move(1, 0, g):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        maybe_item = g.get(player.pos_x + 1, player.pos_y)

        player.move(1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            inventory.append(maybe_item)      #Läggr till itm i inventory
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

    # ___________________________________________________________________________________________
    if command == "a" and player.can_move(-1, 0, g):  # move left

        maybe_item = g.get(player.pos_x - 1, player.pos_y)
        player.move(-1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            inventory.append(maybe_item)      #Läggr till itm i inventory
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)


   #___________________________________________________________________________________________
    if command == "w" and player.can_move(0, -1, g):  # move up

        maybe_item = g.get(player.pos_x , player.pos_y-1)
        player.move(0, -1)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            inventory.append(maybe_item)      #Läggr till itm i inventory
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

    #___________________________________________________________________________________________
    if command == "s" and player.can_move(0, 1, g):  # move down

        maybe_item = g.get(player.pos_x , player.pos_y+1)
        player.move(0, 1)
        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            inventory.append(maybe_item)      #Läggr till itm i inventory
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
