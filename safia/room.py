import pygame, sys

class Room():
    def __init__(self, name, desc, img, hasPerson, character):
        self.name = name
        self.description = desc
        self.image = img
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.character = character

    def get_name(self):
        return self.name


    def get_desc(self):
        d = self.name + "\n" + self.description + "\n"
        if self.north_room != None:
            d = d + "North: " + self.north_room.get_name() + "\n"
        if self.south_room != None:
            d = d + "South: " + self.south_room.get_name() + "\n"
        if self.east_room != None:
            d = d + "East: " + self.east_room.get_name() + "\n"
        if self.west_room != None:
            d = d + "West: " + self.west_room.get_name() + "\n"
        return d

#    def set_image(self, img):
#        self.image = img
    def get_image(self):
        return self.image

    def get_north_link(self):
        return self.north_room

    def get_south_link(self):
        return self.south_room

    def get_east_link(self):
        return self.east_room

    def get_west_link(self):
        return self.west_room

    def set_links(self,n,s,e,w):
        self.north_room = n
        self.east_room = e
        self.south_room = s
        self.west_room = w

    def get_character(self):
        return self.character