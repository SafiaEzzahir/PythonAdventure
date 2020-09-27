import pygame, sys
import pgzrun
sys.path.insert(0,'..\common')
from sprite import Sprite
from GameObject import GameObject
from random import randint

WIDTH = 1000
HEIGHT = 600

#apple = Sprite("apple", 100, 100, 100, 100)

gameObjects = []
for i in range(1,10):
    incx = randint(1,100)/10
    incy = randint(1,100)/10
    obj = GameObject("apple", 100, 100, 100, 100, incx, incy)
    gameObjects.append(obj)

def draw():
    screen.clear()
   # apple.draw()
    for obj in gameObjects:
        obj.draw()

def update():
    for obj in gameObjects:
        obj.do()


pgzrun.go()