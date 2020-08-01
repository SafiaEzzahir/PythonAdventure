import pygame, sys

class Character():
    def __init__(self, name, desc, img):
        self.name = name
        self.description = desc
        self.image = img

    def get_name(self):
        return self.name

    def get_desc(self):
        d = self.name + "\n" + self.description + "\n"

    def get_image(self):
        return self.image

    def get_image2(self):
        return self.image
