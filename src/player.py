class Player:
    marker = "ᗧ"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    # **************************************************************************

    # C.Man ska inte kunna gå igenom väggar.
    def can_move(self, x, y, grid):
        # Nya positioner
        new_x=self.pos_x+x
        new_y=self.pos_y+y
        # kollar om det finns vägg eller något annat
        check = grid.get(new_x, new_y)
        if check==grid.wall:    #****Om det finns vägg går ej att flyttas*****
            return False
        return True
    ##**************************************************************************



