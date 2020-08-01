import pygame, sys
import pgzrun
from location import Location
from person import Person 

WIDTH = 1280
HEIGHT =720

pygame.key.set_repeat(50000, 500000)
text_box = Rect(0, 0, 820, 150)
text_box.move_ip(50, 520)
person_text = Rect(0, 0, 100 ,100)
person_text.move_ip(1100,80)
name_box = Rect(0, 0, 100, 50)
name_box.move_ip(1100, 240)

up_box = Actor("arrow-up")
down_box = Actor("arrow-down")
left_box = Actor("arrow-left")
right_box = Actor("arrow-right")
location_object = Actor("shield")
location_object._surf = pygame.transform.scale(location_object._surf, (100, 100))
location_object._update_pos()
location_object.move_ip(50, 40)

location_character = Actor("bear")
location_character._update_pos()
location_character.move_ip(610, 40)


bear = Person("honeybear","bear","Do you want to become friends with me?")


up_box.move_ip(950, 75)
down_box.move_ip(950, 175)
left_box.move_ip(900, 125)
right_box.move_ip(1000, 125)


l1 = Location(0, "location1", "It all starts at the entrance of the magic, spooky forest.", None, None)
l2 = Location(1, "location2", "You see nothing special, just woods.Deep dark woods. Continue you journey to find something.", None, None)
l3 = Location(2, "location3", "You are in a nice and quite area. You see a super special sword and take it to improve your Attack.", "sword", None)
l4 = Location(3, "location4", "Nothing to be done here just  boaring woods .", None, None)
l5 = Location(4, "location5", "You see an amazing shield on the ground. You take it to improve your defense.", "shield", None)
l6 = Location(5, "location6", "You arrive near an amazing pond. You help yourself with some water.", None, None)
l7 = Location(6, "location7", "You approache a dark cave. A soldier is ready to attack you.", None, bear)
l8 = Location(7, "location8", "A nice princess thanks you for saving her. She gives you a key for the treasure chest", None, None)
l9 = Location(8, "location9", "You see a big and mysterious chest on the ground.", None, None)

l1.set_locations(l2  ,None,None,None)
l2.set_locations(l4  ,l1  ,l3  ,None)
l3.set_locations(None,None,None,l2)
l4.set_locations(l7  ,l2  ,l5  ,l6)
l5.set_locations(None,None,None,l4)
l6.set_locations(None,None,l4  ,None)
l7.set_locations(l8  ,l4  ,None,None)
l8.set_locations(None,l7  ,None,l9)
l9.set_locations(None,None,l8  ,None)

locations = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
location = locations[0]

             

def update_location():
    global main_box, location_object
    main_box = Actor(location.get_name())
    main_box.move_ip(50, 40)
    if location.get_item() != None:
        location_object = Actor(location.get_item())
        location_object._surf = pygame.transform.scale(location_object._surf, (100, 100))
        location_object.move_ip(50, 40)
        location_object._update_pos()
    if location.get_character() != None:
        location_character = Actor(location.get_character().image)
        location_character._surf = pygame.transform.scale(location_character._surf, (100, 100))
        location_character._update_pos()
        location_character.move_ip(50, 40)



def draw():
  global location
    
  screen.fill("black")
  main_box.draw();
  screen.draw.filled_rect(text_box, "sky blue")
  screen.draw.textbox(location.get_desc(), text_box, color=("black"))  

  if location.get_item() != None and (location.get_isItemVisible()==True):
    print("itemVisible:" + str(location.get_isItemVisible()))
    location_object.draw()

  if location.get_character() != None:
    location_character.draw()
    screen.draw.filled_rect(person_text, "light pink")
    screen.draw.textbox(location.get_character().sentence, person_text, color=("black")) 
    screen.draw.filled_rect(name_box, "light pink")
    screen.draw.textbox(location.get_character().name, name_box, color=("black"))  
 


  up_box.draw();
  down_box.draw();
  left_box.draw();
  right_box.draw();



def on_mouse_down(pos):
    global movements, location,kcleared
    if up_box.collidepoint(pos):
        if(location.get_location_forward() != None):
            location.leave_location()
            location = location.get_location_forward()
            update_location()            
    if down_box.collidepoint(pos):
        if(location.get_location_backward()!= None):
            location.leave_location()
            location = location.get_location_backward()
            update_location()
    if right_box.collidepoint(pos):
        if(location.get_location_right() != None):
            location.leave_location()
            location = location.get_location_right()
            update_location()                
    if left_box.collidepoint(pos):
        if(location.get_location_left() != None):
            location.leave_location()
            location = location.get_location_left()
            update_location()


update_location()
        
    
pgzrun.go()
