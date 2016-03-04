import pygame
from pygame.locals import QUIT, KEYDOWN
import time
from random import choice
from math import sqrt
import cv2
import numpy as np

class Sky():
    def __init__(self, width = 500, height = 500):
        pygame.init()
        self.screen = pygame.display.set_mode((height,width))
        pygame.display.set_caption = ('DodgyGame')
        # self.actors = {} do we need actors
        self.width = width
        self.height = height
    
    def _draw_background(self):
        self.screen.fill(pygame.Color(135, 206, 250))
        pygame.display.update()
        
    def main_loop(self):
        running = True
        while running:
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

    def movement(self):
        pass
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/arianaolson/haarcascade_frontalface_alt.xml')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    a = int(cap.get(3))
    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255))
        if x > a:
            print 'right'
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows   
if __name__ == "__main__":
    g = Sky()
    g.main_loop()
   