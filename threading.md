# Multithreading in Python

## Introduction
There comes a time in one's life when plain old blocking code just won't work for your application needs. The wonderful journey of tech over the years has given us a world brimming with asynchronous request and response calls. Included within Python's standard library is technology that allows for some semblance of asynchronicity even if there may be perils and complications lurking in the dark caverns in which it resides. The path that leads us to the multithreading beasts lair is surprisingly straight forward however. Lets take a few steps down the twisting path here together.

## What should we watch out for?
Adding multithreading to your application increases the complexity of your program in unexpected ways. One of the pitfalls to avoid is touching the same memory location with multiple theads. Complicated interlocks must be implemented if threads need to share the same resource. This is beyond the scope of this article as this is to serve as only an introduction to further your learning. 

## How to get started
Lets see what a simple multi-threaded pomodoro timer looks like in python. 

First Thread and time must be imported into your script.

~~~ from threading import Thread 
    import time~~~



Lets make a function called pomodoro that will 
