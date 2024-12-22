import Tile

# TODO: Abstract colours to some macros to define in the application
# for example 'I': I_COLOR, where I_COLOR is defined in a different file,
# together with the background colour
PIECE_COLOR = {
    'I': '#02f4e4',
    'J': '#028bf4',
    'L': '#f4a802',
    'S': '#87f402',
    'Z': '#f42a02',
    'O': '#f4f002',
    'T': '#f4029b'
}

ORIENT_ZERO, ORIENT_RIGHT, ORIENT_FLIP, ORIENT_LEFT = range(4)

PIECE_TYPES = PIECE_COLOR.keys()

class Piece:
    def __init__(self, x, y, shape) -> None:
        self.shape = shape
        self.x = x
        self.y = y
        self.orientation = 0
        self.rotation_center = (0, 0)
        
        self.tiles = []
        positions = []
        if (shape == 'I'):
            positions.append((0, 0))
            positions.append((1, 0))
            positions.append((2, 0))
            positions.append((-1, 0))
            self.rotation_center = (0.5, 0.5)
        elif (shape == 'J'):
            positions.append((0, 0))
            positions.append((-1, -1))
            positions.append((-1, 0))
            positions.append((1, 0))
        if (shape == 'L'):
            positions.append((0, 0))
            positions.append((1, -1))
            positions.append((-1, 0))
            positions.append((1, 0))
        if (shape == 'S'):
            positions.append((0, 0))
            positions.append((0, -1))
            positions.append((1, -1))
            positions.append((-1, 0))
        if (shape == 'Z'):
            positions.append((0, 0))
            positions.append((0, 1))
            positions.append((1, 1))
            positions.append((-1, 0))
        if (shape == 'O'):
            positions.append((0, 0))
            positions.append((0, 1))
            positions.append((1, 1))
            positions.append((1, 0))
            self.rotation_center = (0.5, 0.5)
        if (shape == 'T'):
            positions.append((0, 0))
            positions.append((0, -1))
            positions.append((-1, 0))
            positions.append((1, 0))
        
        for position in positions:
            self.tiles.append(Tile.Tile(
                position[0],
                position[1],
                PIECE_COLOR[shape]
            ))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def rotate(self, right_angles):
        self.orientation =  (self.orientation + right_angles) % 4
        right_angles = right_angles % 4
        
        if right_angles == ORIENT_ZERO: return

        o = self.rotation_center

        for tile in self.tiles:
            new_x = 0
            new_y = 0
            
            if (right_angles == ORIENT_RIGHT):
                new_x = -tile.y + o[0] + o[1]
                new_y = tile.x - o[0] + o[1] 
        
            elif (right_angles == ORIENT_FLIP):
                new_x = -tile.x + 2*o[0]
                new_y = -tile.y + 2*o[1]
            
            elif (right_angles == ORIENT_LEFT):
                new_x = tile.y - o[1] + o[0]
                new_y = -tile.x + o[0] + o[1]
            
            tile.x = new_x
            tile.y = new_y