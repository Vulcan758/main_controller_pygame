#! /usr/bin/env python3
import pygame
from time import sleep 
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("gamepad controller")

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

up = 0
down = 1
left = 2
right = 3

directions = [up, down, left, right]
dir_states = [False, False, False, False]
outputs = ["up", "down", "left", "right"]

def controller(up, down, right, left):
    dir_ = None
    while True:
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION:
                if event.value > 0.75 and event.axis == 1:
                    print("GOING DOWN")
                    dir_states[down] = True
                if event.value < -0.75 and event.axis == 1:
                    print("GOING UP")
                    dir_states[up] = True
                if event.value < -0.75 and event.axis == 0:
                    print("GOING LEFT")
                    dir_states[left] = True
                if event.value > 0.75 and event.axis == 0:
                    print("GOING RIGHT")
                    dir_states[right] = True
            if event.type == JOYAXISMOTION and event.value > -0.25 and event.value < 0.25:
                if event.axis == 1:
                    dir_states[down] = False
                    dir_states[up] = False
                if event.axis == 0:
                    dir_states[left] = False
                    dir_states[right] = False
        for dir in dir_states:
            if dir == True:
                print(outputs[dir_states.index(dir)])            
        sleep(0.1)
if __name__ == "__main__":
    controller(up, down, right, left)
