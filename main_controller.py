#! /usr/bin/env python3
import pygame
from time import sleep 
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("rover controller")

up = 119
down = 115
left = 97
right = 100

directions = [up, down, left, right]
dir_states = [False, False, False, False]
outputs = ["up", "down", "left", "right"]

def controller():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed = directions.index(event.key)
                dir_states[pressed] = True
            elif event.type == pygame.KEYUP:
                released = directions.index(event.key)
                dir_states[released] = False
        for dir in dir_states:
            if dir == True:
                print(outputs[dir_states.index(dir)])
        sleep(0.1)
            
if __name__ == "__main__":
    controller()

#w --> 119
#a --> 97
#s --> 115
#d --> 100
