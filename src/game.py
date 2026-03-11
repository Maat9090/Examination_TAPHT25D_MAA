
from .grid import Grid
from .player import Player
from . import pickups
from .status import print_status


player = Player(15, 5)     # A.Spelaren ska börja nära mitten av rummet.
score = 0
inventory = []
grace_steps = 0
steps = 0

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
    # *************************************************************************************
    #Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    if command == "i":
      print("Here is your inventory")
      if not inventory:
          print("Your inventory is empty.")
      for item in inventory:
          print(item.name)
      continue

    # *************************************************************************************
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


    if dx == 0 and dy == 0: # om spelare inte rört sig
        continue

    new_x = player.pos_x + dx    #Vad blir för nästa ruta
    new_y = player.pos_y + dy

    maybe_item =g.get(new_x, new_y) #Kollr va som finns i rutan

    #*****************************************************************************************
    if maybe_item == g.wall:  # Om man hittar vägg
            #  vänster yv__höger yv____________övre yv_____nedre yv
            if new_x==0 or new_x==g.width-1 or new_y==0 or new_y==g.height-1: # kollar om det är inte ytterväggar
                print("You can't go there!")
            else:
                 for item in inventory:
                    if item.name == "shovel":  # Om spelaren har spade
                       g.clear(new_x, new_y)  # Tar bort väggen
                       inventory.remove(item)  # Tar bort spaden
                       maybe_item= g.empty
                       break
    # ************** L.Bördig jord - efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.**********
    if player.can_move(dx,dy, g):  #Kollr om rutan är ledig
        player.move(dx, dy)
        steps += 1 # Stegräknaren
        maybe_item = g.get(player.pos_x, player.pos_y) #Kollar om item finns i splarens position
    if steps % 25 ==0 : # För att få 25 stegar
        import random
        item = random.choice(pickups.pickups) #Slumpar från en item

        while True:   # Griden ger en plats
            x=g.get_random_x()
            y=g.get_random_y()

            if g.is_empty(x, y):  #Om platsen är tom, läggs en item
                g.set(x,y,item)
                print("A new item has been added.")
                break

     #**************************** O.Grace period-5p********************************************
    if grace_steps > 0: # kollar om det finns fri steg
        grace_steps -= 1 # om det finns, minskas här
    else:
          score -= 1  #Annars miskar lavan
    '''    
    # G.The floor is lava - för varje steg man går ska man tappa 1 poäng.
    #for item in inventory:
     #score -= 1  
    '''
    if maybe_item == g.trap :  # Minska 10p på fälla
      score -= 10
    # *******************************************************************************************
    if isinstance(maybe_item, pickups.Item):
          # we found something
           score += maybe_item.value
           inventory.append(maybe_item)  # Lägger till itm i inventory
           grace_steps = 5
           print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
           # g.set(player.pos_x, player.pos_y, g.empty)
           g.clear(player.pos_x, player.pos_y)


