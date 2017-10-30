###############################
# A python alarm OR stopwatch #
###############################

from time import sleep
import os

'''
ask if alarm clock or stopwatch
if alarm then do alarm
else do stopwatch
'''

# alarm
time = int(input("Please enter the amount of time, in seconds, before alarm: "))


for x in [0,time]:
    while x != time:
        print(x + 1)
        sleep(1)
        x += 1
    else:
        os.system("say times up!")
        break