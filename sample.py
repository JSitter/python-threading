#!/usr/bin/python3

# Multi Threading in Python
from threading import Thread
import time

def pomodoro(name, set_time):
    print("Pomodoro : " + name + " start")
    cur_time = 0
    while cur_time < set_time:
        time.sleep(1)
        print(name + " timer" )
        cur_time += 1

    print( 'POMODORO! ' + name)

def Main():
    p1 = Thread(target=pomodoro, args=("Go Outside", 8))
    p2 = Thread(target=pomodoro, args=("Get Coffee", 4))
    p1.start()
    p2.start()

    print("Main Completed!")

if __name__ == "__main__":
    Main()