import pygame
from math import sqrt

class Sky():
    def __init__(self, width = 500, height = 500):
        pygame.init()
        self.screen = pygame.display.set_mode((height,width))
        pygame.display.set_caption = ('DodgyGame')
        # self.actors = {} do we need actors
        self.width = width
        self.height = height
    
    def _draw_background(self):
        self.screen.fill((135, 206, 250))
        
    def main_loop(self):
        running = True
        while (running):
            self._draw_background()

class Birds(object):
    def __init__(self, radius, coord, image_loc, is_obstacle = True):
        self.radius = radius
        self.coord = coord
        self.image = pygame.image.load(image_loc)
        self.is_obstacle = is_obstacle

    def _update(self):
        if self.radius < 100: #certain size:
            self.radius += 10
        else:
            pass
            # erase?

class User(object):
    def __init__(self, radius, coord, image_loc):
        self.radius = radius
        self.coord = coord
        self.image = pygame.image.load(image_loc)

    def _movement(self):
        pass
        # opencv stuff here? idk


if __name__ == "__main__":
    g = Sky()
    g.main_loop
    