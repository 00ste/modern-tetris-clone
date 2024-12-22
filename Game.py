import Piece, Tile
import random, math

ALL_PIECES = [Piece.Piece(5, 1, shape) for shape in Piece.PIECE_TYPES]

class Game:
    def __init__(self) -> None:
        self.fixed_lines = [[] for _ in range(21)]
        self.bag = []
        self.generate_bag()
        self.generate_bag()
        self.active_piece = self.bag.pop()
        self.tick_time = 500
        self.held_piece = None
        self.has_held = False
        self.lock_timer = 0
        self.max_lock_timer = 2
        self.lock_attempts = 0
        self.max_lock_attempts = 3
      
    def get_wall_kick_positions(shape, orientation, right_angles):
        start = orientation % 4
        end = (orientation + right_angles) % 4

        if shape in ['S', 'Z', 'T', 'L', 'J']:

            if end == Piece.ORIENT_LEFT:
                return [(x, -y) for (x, y) in [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)]]
            
            if end == Piece.ORIENT_RIGHT:
                return [(x, -y) for (x, y) in [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)]]
            
            if start == Piece.ORIENT_LEFT:
                return [(x, -y) for (x, y) in [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)]]
            
            if start == Piece.ORIENT_RIGHT:
                return [(x, -y) for (x, y) in [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)]]
            
        if shape == 'I':

            if (start, end) in [(Piece.ORIENT_ZERO, Piece.ORIENT_RIGHT), (Piece.ORIENT_LEFT, Piece.ORIENT_FLIP)]:
                return [(x, -y) for (x, y) in [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)]]
            
            if (start, end) in [(Piece.ORIENT_RIGHT, Piece.ORIENT_ZERO), (Piece.ORIENT_FLIP, Piece.ORIENT_LEFT)]:
                return [(x, -y) for (x, y) in [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)]]
            
            if (start, end) in [(Piece.ORIENT_RIGHT, Piece.ORIENT_FLIP), (Piece.ORIENT_ZERO, Piece.ORIENT_LEFT)]:
                return [(x, -y) for (x, y) in [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)]]
            
            if (start, end) in [(Piece.ORIENT_FLIP, Piece.ORIENT_RIGHT), (Piece.ORIENT_LEFT, Piece.ORIENT_ZERO)]:
                return [(x, -y) for (x, y) in [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)]]
        
        return []
          
    def generate_bag(self):
        piece_types = [shape for shape in Piece.PIECE_TYPES]
        random.shuffle(piece_types)
        while (len(piece_types) > 0):
            self.bag.append(Piece.Piece(5, 1, piece_types.pop()))
    
    def check_collision(self, piece):
        for tile in piece.tiles:

            # out of bounds collision
            if piece.x + tile.x < 0 or piece.x + tile.x >= 10 or piece.y + tile.y >= 21:
                return True
            
            # fixed tiles collision
            for fixed_line in self.fixed_lines:
                for fixed_tile in fixed_line:
                    if piece.x + tile.x == fixed_tile.x and piece.y + tile.y == fixed_tile.y:
                        return True
        return False
    
    def attempt_locking(self):
        if self.lock_timer >= self.max_lock_timer:
            self.consolidate_piece()
        else:
            self.lock_timer += 1

    def consolidate_piece(self):
        # consolidate active piece into fixed tiles
        for tile in self.active_piece.tiles:
            self.fixed_lines[math.floor(tile.y + self.active_piece.y)].append(Tile.Tile(
                tile.x + self.active_piece.x,
                tile.y + self.active_piece.y,
                tile.color
            ))
        self.lock_timer = 0
    
        # generate new active piece
        self.active_piece = self.bag.pop()
        # TODO: Extract this 4 and write the number of
        # next pieces that should be shown on the screen
        if len(self.bag) <= 4:
            self.generate_bag()

        # remove full lines
        for i in range(len(self.fixed_lines)):
            if len(self.fixed_lines[i]) == 10:
                self.fixed_lines.remove(self.fixed_lines[i])
                self.fixed_lines.insert(0, [])

        # update y position of all fixed tiles
        for y, fixed_line in enumerate(self.fixed_lines):
            for fixed_tile in fixed_line:
                fixed_tile.y = y
        
        # reset held piece
        self.has_held = False
        
    def on_tick(self):
        # make piece fall
        self.active_piece.move(dx=0, dy=1)

        if self.check_collision(self.active_piece):
            self.active_piece.move(dx=0, dy=-1)
            self.attempt_locking()
            # self.consolidate_piece()

    def on_hold(self):
        if not self.has_held:
            self.has_held = True

            # first hold
            if self.held_piece == None:
                self.held_piece = self.active_piece
                self.active_piece = self.bag.pop()
                if len(self.bag) <= 4:
                    self.generate_bag()

            # all other holds
            else:
                temp = self.held_piece
                self.held_piece = self.active_piece
                self.active_piece = temp

            self.lock_timer = 0
            self.held_piece.set_pos(5, 0)

    def on_translate(self, dx):
        self.active_piece.move(dx=dx, dy=0)
        if self.check_collision(self.active_piece):
            self.active_piece.move(dx=-dx, dy=0)

    def on_soft_drop(self):
        self.active_piece.move(dx=0, dy=1)
        if self.check_collision(self.active_piece):

            self.active_piece.move(dx=0, dy=-1)
            # self.attempt_locking()
            # self.consolidate_piece()
    
    def on_hard_drop(self):
        while not self.check_collision(self.active_piece):
            self.active_piece.move(dx=0, dy=1)
        self.active_piece.move(dx=0, dy=-1)
        self.consolidate_piece()

    def on_rotate(self, right_angles):   
        self.active_piece.rotate(right_angles)

        # wall kicks
        wall_kick_positions = Game.get_wall_kick_positions(
            self.active_piece.shape,
            self.active_piece.orientation - right_angles,
            right_angles
        )
        # try every possible cursed direction
        for direction in wall_kick_positions:
            self.active_piece.move(dx=direction[0], dy=direction[1])
            if not self.check_collision(self.active_piece):
                return
            self.active_piece.move(dx=-direction[0], dy=-direction[1])
        
        # give up
        self.active_piece.rotate(-right_angles)


            


