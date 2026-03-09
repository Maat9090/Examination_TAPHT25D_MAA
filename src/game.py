from tokenize import maybe

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
  #  command = command.casefold()[:1]
#------------------------------------------------------------------------------------------
    #Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    if command == "i":
      print("Here is your inventory")
      if not inventory:
          print("Your inventory is empty.")
      for item in inventory:
          print(item.name)
      continue

#___________________________________________________________________________________________

    dx=0 # x-led (höger/vänster)
    dy=0 #y-led (upp/ner)

    if command == "d":
        dx=1
    elif command == "a":
        dx=-1
    elif command == "w":
        dy=-1
    elif command == "s":
        dy=1

    if (dx !=0 or dy !=0) and player.can_move(dx,dy, g):   #Om spelaren gå i den riktningen
       new_x = player.pos_x + dx    #Vad blir för nästa ruta
       new_y = player.pos_y + dy
       maybe_item =g.get(new_x, new_y) #Kollr va som finns i rutan
    #*************************************************************************************

       if maybe_item == g.trap :  # Minska 10p på fälla
          score -= 10
    #*************************************************************************************

       player.move(dx, dy)
   #*************************************************************************************
       score -= 1  # G.The floor is lava - för varje steg man går ska man tappa 1 poäng.
   # *************************************************************************************
       if isinstance(maybe_item, pickups.Item):
          # we found something
           score += maybe_item.value
           inventory.append(maybe_item)  # Läggr till itm i inventory
           print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
           # g.set(player.pos_x, player.pos_y, g.empty)
           g.clear(player.pos_x, player.pos_y)


