import cv2
import os
import time
import random
import time

IMAGES_PATH = 'C:\\Users\\bolts\\TennisShots\\data\\'
number_images = int(input('how many images to take? '))
shot = input('what shot(forehand, backhand, serve)? ')
shot_direction = input('where is this shot going(crosscourt, line, body, wide, T)? ')
shot_type = input('how is the shot hit(flat, topspin, high, slice, dropshot, kick)? ')
shot_name = shot + shot_direction + shot_type
shot_temp = shot_name
IMAGES_PATH += shot
IMAGES_PATH = os.path.join(IMAGES_PATH)

time.sleep(3)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture device.")
    exit()

for imgnum in range(number_images):
    shot_name = shot_temp
    randomint = random.randint(0,10000)
    shot_name += str(randomint)
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    imgname = os.path.join(IMAGES_PATH, f'{shot_name}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()