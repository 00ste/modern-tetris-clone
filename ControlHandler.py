import pygame

class ControlHandler:
    def __init__(self) -> None:
        # key -> [function mapping, was triggered]
        self.press_binds = {}

        # key -> [function mapping, frame time, retrigger time]
        self.hold_binds = {}

    def bind_on_press(self, key, action):
        self.press_binds[key] = [action, False]
    
    def bind_on_hold(self, key, action, retrigger_time):
        self.hold_binds[key] = [action, 0, retrigger_time]
    
    def tick(self, fps):
        for key in self.press_binds.keys():
            if pygame.key.get_pressed()[key]:
                if not self.press_binds[key][1]:
                    self.press_binds[key][0]()
                    self.press_binds[key][1] = True
            else:
                self.press_binds[key][1] = False

        for key in self.hold_binds.keys():
            if pygame.key.get_pressed()[key]:
                if self.hold_binds[key][1] == 0:
                    self.hold_binds[key][0]()
                self.hold_binds[key][1] += 1000/fps
                if self.hold_binds[key][1] >= self.hold_binds[key][2]:
                    self.hold_binds[key][1] = 0
            else:
                self.hold_binds[key][1] = 0