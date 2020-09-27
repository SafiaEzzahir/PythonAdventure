import pygame, sys
import pgzrun
from pgzero.builtins import Actor, animate, keyboard

class Sprite:
    def __init__(self, filename, x, y, width, height):
        self.sprite = Actor(filename)
        self.x = x
        self.y = y
        self.sprite.x = x
        self.sprite.y = y

    def moveTo(self, x,y):
        self.x = x
        self.y = y
        self.sprite.x = x
        self.sprite.y = y

    def draw(self):
        self.sprite.draw()

    #def move(self,x, y):

    #def scale(self, scale_x, scale_y):
