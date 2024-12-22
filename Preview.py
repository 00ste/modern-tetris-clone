import pygame

class Preview:
    def __init__(self, max_preview_pieces) -> None:
        self.max_preview_pieces = max_preview_pieces
        self.tile_size = 30
        self.padding = 20
        self.surface = pygame.Surface((
            4*self.tile_size * 1 + self.padding * 2,
            4*self.tile_size * self.max_preview_pieces + self.padding * (self.max_preview_pieces)
        ))

    def fill(self, color):
        self.surface.fill(color)
    
    def draw_piece(self, shape, slot):
        if slot >= self.max_preview_pieces: return

        # TODO: Change colour from white to piece colour
        if shape == 'I':
            self.draw_rect(0, 1.5, 4, 1, slot, '#707070')
        elif shape == 'O':
            self.draw_rect(1, 1, 2, 2, slot, '#707070')
        elif shape == 'S':
            self.draw_rect(1.5, 1, 2, 1, slot, '#707070')
            self.draw_rect(0.5, 2, 2, 1, slot, '#707070')
        elif shape == 'Z':
            self.draw_rect(0.5, 1, 2, 1, slot, '#707070')
            self.draw_rect(1.5, 2, 2, 1, slot, '#707070')
        elif shape == 'T':
            self.draw_rect(1.5, 1, 1, 1, slot, '#707070')
            self.draw_rect(0.5, 2, 3, 1, slot, '#707070')
        elif shape == 'J':
            self.draw_rect(0.5, 1, 1, 1, slot, '#707070')
            self.draw_rect(0.5, 2, 3, 1, slot, '#707070')
        elif shape == 'L':
            self.draw_rect(2.5, 1, 1, 1, slot, '#707070')
            self.draw_rect(0.5, 2, 3, 1, slot, '#707070')

    def draw_rect(self, x_ts, y_ts, width_ts, height_ts, slot, color):
        pygame.draw.rect(self.surface, color, (
                self.padding + self.tile_size * x_ts,
                self.padding * slot + self.tile_size * (4 * slot + y_ts),
                width_ts * self.tile_size,
                height_ts * self.tile_size
            ))

