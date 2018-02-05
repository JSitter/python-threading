# Multithreading in Python

## Introduction
There comes a time in one's life when plain old blocking code just won't work for your application needs. The wonderful journey of tech over the years has given us a world brimming with asynchronous request and response calls. Included within Python's standard library is technology that allows for some semblance of asynchronicity even if there may be perils and complications lurking in the dark caverns in which it resides. The path that leads us to the multithreading beasts lair is surprisingly straight forward however. Lets take a few steps down the twisting path here together.

## What should we watch out for?
Adding multithreading to your application increases the complexity of your program in unexpected ways. One of the pitfalls to avoid is touching the same memory location with multiple theads. Complicated interlocks must be implemented if threads need to share the same resource. This is beyond the scope of this article as this is to serve as only an introduction to further your learning. 

## How to get started
Lets see what a simple multi-threaded pomodoro timer looks like in python. 

First Thread and time must be imported into your script.

~~~ 
    from threading import Thread 
    import time
~~~

Lets make a function called pomodoro that will be called when we want to set a timer.

~~~
    def pomodoro(timer_name, set_time):
        cur_time = 0
        while cur_time < set_time:
            time.sleep(1)
            print(timer_name + " timer running" )
            cur_time += 1

        print( 'POMODORO! ' + timer_name)
~~~

This is a simple function that will print out to the console on each iteration of the timer.
If this function is run normally as such 

~~~
    pomodoro("Blocking Timer1", 3)
    pomodoro("Blocking Timer2", 5)
~~~ 

In this example our second timer must wait for the first one to finish before it starts.

With multithreading we can do a bit better.

We must first instantiate a new Thread by calling it with the name of our function as well as any arguments that need to be passed into it.

~~~
    pomodoro1 = Thread(target=pomodoro, args=("Multithreaded timer 1", 8))
    pomodoro2 = Thread(target=pomodoro, args=("Multithreaded timer 2", 4))
~~~

Our new threads just need to be started and we're off!

~~~
    pomodoro1.start()
    pomodoro2.start()
~~~

At this point you'll notice that the second timer will finish before the first one as we would expect. We no longer have to wait for slow code to complete before starting shorter operations.

Now that we have threads started can we also shut them down?

That is a story for another time.