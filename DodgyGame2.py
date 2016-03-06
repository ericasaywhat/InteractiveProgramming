import pygame
from pygame.locals import QUIT, KEYDOWN
import time
from random import *
import cv2
import numpy as np

class SkyModel(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.BIRD_Y = 0
        self.USER_X = 250
        self.RADIUS = 10
        self.bird = Bird(randint(1,500), self.BIRD_Y , self.RADIUS)
        self.user = User(self.USER_X, 500, 100)



    def update(self):
        self.bird.update()


class View(object):
    """ Provides a view of the brick breaker model in a pygame
        window """
    def __init__(self, model, size):
        """ Initialize with the specified model """
        self.model = model
        self.screen = pygame.display.set_mode(size)


    def draw(self):
        """ Draw the game to the pygame window """
        # draw all the bricks to the screen
        self.screen.fill(pygame.Color(135, 206, 250))
        pygame.draw.circle(self.screen,
                           pygame.Color('yellow'),
                           (self.model.bird.center_x, self.model.bird.center_y),
                           self.model.bird.radius)
        pygame.draw.circle(self.screen,
                           pygame.Color('white'),
                           (self.model.user.center_x, self.model.user.center_y),
                           self.model.user.radius)

        # r = pygame.Rect(self.model.paddle.left,
        #                 self.model.paddle.top,
        #                 self.model.paddle.width,
        #                 self.model.paddle.height)
        # pygame.draw.rect(self.screen, pygame.Color('orange'), r)
        pygame.display.update()



class Bird(object):
    """ Represents a bird in my dodging game """
    def __init__(self, center_x, center_y, radius):
        """ Create a ball object with the specified geometry """
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.growth = 5
    
    def update(self):
        """ Update the position of the ball due to time passing """
        # self.radius += self.growth
        self.center_y += 20

class User(object):
    """ Represents the user in my dodging game """
    def __init__(self, center_x, center_y, radius):
        """ Create a ball object with the specified geometry """
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

class Movement(object):
    def __init__(self, model):
        self.model = model
    def handle_event(self, event):
        for (x,y,w,h) in faces:
            self.model.user.center_x = 500-(2*x)
            break
            print x
        



if __name__ == '__main__':
    pygame.init()
    size = (500, 500)
    MOVE = pygame.USEREVENT + 1
    move_event = pygame.event.Event(MOVE)
    pygame.time.set_timer(MOVE, 1)
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('/home/arianaolson/haarcascade_frontalface_alt.xml')
    # kernel = np.ones((21,21), 'uint8')

    model = SkyModel(size[0], size[1])
    view = View(model, size)
    movement = Movement(model)
    running = True
    
    while running:
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            else:
                movement.handle_event(event)
        model.update()
        view.draw()
        time.sleep(.01)
    cap.release()     
    cv2.destroyAllWindows()

   