import sys, pygame
import pgzrun

class Writing():
    def __init__(self, name, sizex, sizey, movex, movey):
        self.name = name
        self.sizex = sizex
        self.sizey = sizey
        self.movex = movex
        self.movey = movey

    def draw(self, screen):
        rect = pygame.Rect(self.movex, self.movey, self.sizex, self.sizey)
        screen.draw.filled_rect(rect, "red")
        screen.draw.textbox(self.name, rect, color=("black"))