from room import Room
import pygame, sys
import pgzrun
from drawLetters import Writing
from character import Character

WIDTH = 1300
HEIGHT = 800

chef = Character("Head cook Applop", "A very strict character who prepare the most delicious of meals.", "chef")
guard = Character("Sir Amon Anom", "A loyal warrior who helps the local peasants.", "guard")
king = Character("King Anathon", "An old man who used to be a brave fighter and insists that everybody be called a name starting with 'A'.", "king")
peasant = Character("A peasant", "A humble but poor villager who is apparently sweeping the floor.", "peasant")
queen = Character("Queen Anira", "A polite lady who is very kind with her close friends.", "queen")

tower1 = Room("The west tower;", "A dark tower with narrow, winding stairs.", "tower1", False, None)
royal = Room("The royal appartments;", "The quiet bedrooms of the king and queen.", "royal", True, queen)
tower2 = Room("The east tower;", "A beautiful view on the village.", "tower2", False, None)
throne = Room("The throne room;", "A big room lined with red carpets.", "throne", True, king)
court = Room("The courtyard;", "A few animals are still kept there by the local farmers and usually the army trains here.", "c", True, peasant)
kitchen = Room("The kitchens;", "Dellicious banquets are prepared here although there are more rats there than there are people.", "kitchen.jpg", True, chef)
enter = Room("The entrance;", "The only way in the castle if you don't know the secret passage ways, but it's guarded day and night.", "entrance", True, guard)


tower1.set_links(None, throne, royal, None)
royal.set_links(None, court, tower2, tower1)
tower2.set_links(None, kitchen, None, royal)
throne.set_links(tower1, None, court, None)
court.set_links(royal, enter, kitchen, throne)
kitchen.set_links(tower2, None, None, court)
enter.set_links(court, None, None, None)

current_room = enter
current_room_image = Actor(kitchen.get_image())
current_room._surf = pygame.transform.scale(current_room_image._surf, (450, 250))

box = current_room.get_desc

n = Writing("North", 150, 50, 905, 50)
e = Writing("East", 100, 100, 1105, 150)
s = Writing("South", 150, 50, 855, 300)
w = Writing("West", 100, 100, 705, 150)


def draw():
    global current_room_image
    screen.fill("black")

    compass = Actor("compass")
    compass._surf = pygame.transform.scale(compass._surf, (300, 200))
    compass.move_ip(805, 100)
    compass.draw()

    current_room_image = Actor(current_room.get_image())
    current_room_image._surf = pygame.transform.scale(current_room_image._surf, (450, 250))
    current_room_image.move_ip(100, 50)
    current_room_image.draw()

    n.draw(screen)
    s.draw(screen)
    e.draw(screen)
    w.draw(screen)

    if current_room.get_character() != None:
        char_image = Actor(current_room.character.get_image())
        char_image._surf = pygame.transform.scale(char_image._surf, (150, 250))
        char_image.move_ip(555, 50)
        char_image.draw()
    else:
        pass

    room_desc = Rect(100, 375, 400, 350)
    screen.draw.filled_rect(room_desc, "light blue")
    screen.draw.textbox(current_room.get_desc(), room_desc, color=("black"))

def on_mouse_down(pos):
    global current_room

    (x,y) = pos
    if n.is_clicked(x, y):
        current_room = current_room.north_room
    if e.is_clicked(x, y):
        current_room = current_room.east_room
    if s.is_clicked(x, y):
        current_room = current_room.south_room
    if w.is_clicked(x, y):
        current_room = current_room.west_room
    
pgzrun.go()