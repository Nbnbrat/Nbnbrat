# Healthy Programmer
# 9am - 5pm
# Water - water.mp3(3.5 liters) - Drank - logilab
# Eyes - eyes.mp3 - every 30 min - Edone - logilab
# Physical activity - physical.mp3 every - 45 min - EXDone
# import pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


#from datetime import datetime
#import pytz
#
# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now(pytz.timezone('Asia/Calcutta')))


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('HealthyProgrammer.txt','a') as f:
        f.write(f'{msg} {datetime.now()}\n')
    f.close()
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyesecs = 12
    exsecs = 20

    health = True
    while health:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alarm.\n")
            musiconloop("mp3music/water.mp3",'drank')
            init_water = time()
            log_now("Drank water at")


        if time() - init_eyes > eyesecs:
            print("It's eye care time. Enter 'eydone' to stop the alarm.\n")
            musiconloop("mp3music/birds.mp3",'eydone')
            init_eyes = time()
            log_now("Eye care done at")



        if time() - init_exercise > exsecs:
            print("Physical activity time. Enter 'exdone' to stop the alarm.\n")
            musiconloop("mp3music/walk.mp3",'exdone')
            init_exercise = time()
            log_now("Exercise done at")







