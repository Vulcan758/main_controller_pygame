import pygame
from time import sleep 
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("rover controller")

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

up = 119
down = 115
left = 97
right = 100

directions = [up, down, left, right]
dir_states = [False, False, False, False]
outputs = ["up", "down", "left", "right"]

while True:
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)            
        if event.type == JOYBUTTONUP:
            print(event)            
        if event.type == JOYAXISMOTION:
            print(event)

