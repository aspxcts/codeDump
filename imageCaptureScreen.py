import pyautogui
import cv2
import os
import time
import random
import time

IMAGES_PATH = 'C:\\Users\\bolts\\TennisShots\\optimizedData\\shots\\'
print("place mouse cursor in top left of rectangle")
time.sleep(3)
topleft = pyautogui.position()
print("coordinate recorded")
print("place mouse cursor in bottom right of rectangle")
time.sleep(3)
topleft = pyautogui.position()
print("coordinate recorded")
number_images = int(input('how many images to take? '))
shot = input('what shot(forehand, backhand, serve)? ')
shot_direction = input('where is this shot going(crosscourt, line, body, wide, T)? ')
shot_type = input('how is the shot hit(flat, topspin, high, slice, dropshot, kick)? ')
shot_name = shot + shot_direction + shot_type
shot_temp = shot_name
IMAGES_PATH += shot
IMAGES_PATH = os.path.join(IMAGES_PATH)