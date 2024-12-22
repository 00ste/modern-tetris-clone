import pygame

class GridCanvas:
    def __init__(self, width, height, tile_size) -> None:
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.surface = pygame.Surface((
            width * tile_size,
            height * tile_size
        ))
    
    def fill(self, color):
        self.surface.fill(color)

    def color_tile(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            pygame.draw.rect(self.surface, color, (
                x * self.tile_size,
                y * self.tile_size,
                self.tile_size,
                self.tile_size
            ))