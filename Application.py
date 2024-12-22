import Game, GridCanvas, Preview, Piece, ControlHandler
import pygame

# TODO: define this in a more appropriate location
TILE_SIZE = 40
MAX_PREVIEW = 4

class Application:
    def __init__(self) -> None:
        self.window_size = (1200, 900)
        self.fps = 60
        self.colors = {
            'background': '#303030'
        }

        self.components = {
            'canvas': GridCanvas.GridCanvas(10, 21, TILE_SIZE),
            'preview': Preview.Preview(MAX_PREVIEW)
        }
        self.game = Game.Game()

        self.control_handler = ControlHandler.ControlHandler()
        self.control_handler.bind_on_hold(pygame.K_LEFT,    lambda: self.game.on_translate(-1), 80)
        self.control_handler.bind_on_hold(pygame.K_RIGHT,   lambda: self.game.on_translate(1),  80)
        self.control_handler.bind_on_hold(pygame.K_DOWN,    lambda: self.game.on_soft_drop(),   30)
        self.control_handler.bind_on_press(pygame.K_UP,     lambda: self.game.on_rotate(Piece.ORIENT_RIGHT))
        self.control_handler.bind_on_press(pygame.K_z,      lambda: self.game.on_rotate(Piece.ORIENT_LEFT))
        self.control_handler.bind_on_press(pygame.K_SPACE,  lambda: self.game.on_hard_drop())
        self.control_handler.bind_on_press(pygame.K_LSHIFT, lambda: self.game.on_hold())

    def run(self):
        pygame.init()
        window = pygame.display.set_mode(self.window_size)
        clock = pygame.time.Clock()
        tick_frame = 0

        running = True
        while (running):
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
            self.control_handler.tick(self.fps)
            
            # time events
            if tick_frame == 0:
                self.game.on_tick()
            
            # rendering
            self.components['canvas'].fill(self.colors['background'])
            self.render_shadow_on_canvas()
            self.render_piece_on_canvas(self.game.active_piece)
            for fixed_line in self.game.fixed_lines:
                for fixed_tile in fixed_line:
                    self.render_tile_on_canvas(fixed_tile)

            self.components['preview'].fill(self.colors['background'])
            for i in range(MAX_PREVIEW):
                piece = self.game.bag[-(i+1)]
                self.components['preview'].draw_piece(piece.shape, i)
            
            """for kick_tile in Game.Game.get_wall_kick_positions(
                self.game.active_piece.shape,
                self.game.active_piece.orientation,
                1
            ):
                self.render_tile_on_canvas(
                    Tile.Tile(kick_tile[0], kick_tile[1], "#defc71"),
                    self.game.active_piece.x,
                    self.game.active_piece.y
                )
            
            for kick_tile in Game.Game.get_wall_kick_positions(
                self.game.active_piece.shape,
                self.game.active_piece.orientation,
                -1
            ):
                self.render_tile_on_canvas(
                    Tile.Tile(kick_tile[0], kick_tile[1], "#fcd571"),
                    self.game.active_piece.x,
                    self.game.active_piece.y
                )"""
            
            window.blit(self.components['canvas'].surface, (10, 10))
            window.blit(self.components['preview'].surface, (500, 10))

            pygame.display.flip()

            # clock
            tick_frame = (tick_frame + 1) % (self.game.tick_time * 0.001 * self.fps)
            clock.tick(self.fps)

        pygame.quit()

    def render_tile_on_canvas(self, tile, rel_x=0, rel_y=0):
        self.components['canvas'].color_tile(
            tile.x + rel_x,
            tile.y + rel_y,
            tile.color
        )
    
    def render_piece_on_canvas(self, piece):
        for tile in piece.tiles:
            self.render_tile_on_canvas(tile, piece.x, piece.y)
    
    def render_shadow_on_canvas(self):
        shadow_piece = Piece.Piece(
            self.game.active_piece.x,
            self.game.active_piece.y,
            self.game.active_piece.shape
        )

        shadow_piece.rotate(self.game.active_piece.orientation)
        for tile in shadow_piece.tiles:
            tile.color = '#707070'

        while not self.game.check_collision(shadow_piece):
            shadow_piece.move(dx=0, dy=1)
        shadow_piece.move(dx=0, dy=-1)

        self.render_piece_on_canvas(shadow_piece)


if __name__ == '__main__':
    Application().run()