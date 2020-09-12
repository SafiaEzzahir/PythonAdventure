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

    def is_clicked(self, mouse_x, mouse_y):
        if mouse_x < self.movex or mouse_x > (self.movex+self.sizex):
            return False
        if mouse_y < self.movey or mouse_y > (self.movey+self.sizey):
            return False
        return True