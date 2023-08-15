from playsound import playsound
from time import sleep
import math

duration = int(input("duration: "))
time_interval = int(input("time interval: "))

for i in range(math.floor(duration/time_interval)):
    sleep(time_interval*60)
    playsound('../data/beep-01a.mp3')