#!/usr/bin/python3

# Multi Threading in Python
from threading import Thread
import time

def pomodoro(timer_name, set_time):
    print("Pomodoro : " + timer_name + " start")
    cur_time = 0
    while cur_time < set_time:
        time.sleep(1)
        print(timer_name + " timer running" )
        cur_time += 1

    print( 'POMODORO! ' + timer_name)

pomodoro("Blocking Timer 1", 3)
pomodoro("Blocking Timer 2", 5)

p1 = Thread(target=pomodoro, args=("Multithreaded timer 1", 8))
p2 = Thread(target=pomodoro, args=("Multithreaded timer 2", 4))
p1.start()
p2.start()

print("Main Completed!")

