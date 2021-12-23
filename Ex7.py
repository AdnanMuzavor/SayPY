from os import times_result
from pygame import mixer
from datetime import datetime
from time import time
# To play respective sound


def musicplayer(music, stopper):
    mixer.init()
    mixer.music.load(music)

    while True:
        mixer.music.play()
        m = input(f"Enter {stopper} once done.")

        if m == stopper:
            writeintolog(f"{m}")
            mixer.music.stop()
            break

# to write respective task into file


def writeintolog(msg):
    with open("Ex7file.txt", "a") as f:
        f.write(f"{msg} at {datetime.now()}\n")




Initwater = time()
Initeye = time()
Initex = time()
waterinterval = 15
eyeinterval = 18
exinterval = 10
while True:
    if time()-Initwater > waterinterval:
        musicplayer("playerwin.mp3", "Drank")
        Initwater = time()
    if time()-Initeye > eyeinterval:
        musicplayer("dealerwon.mp3", "Eye done")
        Initeye = time()
    if time()-Initex > exinterval:
        musicplayer("clicksound.mp3", "Ex done")
        Initex = time()
