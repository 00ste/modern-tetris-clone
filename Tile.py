class Tile:
    def __init__(self, x, y, color) -> None:
        self.color = color
        self.fixed = False

        self.x = x
        self.y = y