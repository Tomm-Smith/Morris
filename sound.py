#!/usr/bin/env python


import winsound


"""
- a dot lasts for one second
- a dash last for three seconds
- the space between dots and dashes that are part of the same letter is one second
- the space between different letters is three seconds
- the space between different words is seven seconds
"""

string = """Another turning point, a fork stuck in the road
Time grabs you by the wrist, directs you where to go
So make the best of this test, and don't ask why
It's not a question, but a lesson learned in time
It's something unpredictable
But in the end, it's right
I hope you had the time of your life
So take the photographs and still frames in your mind
Hang it on a shelf in good health and good time
Tattoos of memories, and dead skin on trial
For what it's worth, it was worth all the while
It's something unpredictable
But in the end, it's right
I hope you had the time of your life
It's something unpredictable
But in the end, it's right
I hope you had the time of your life
It's something unpredictable
But in the end, it's right
I hope you had the time of your life
"""

alph = {'A' : [0,1], 'B' : [1,0,0,0], 'C' : [1,0,1,0], 'D' : [1,0,0], 'E' : [0], 'F' : [0,0,1,0], 
        'G' : [1,1,0], 'H' : [0,0,0,0,], 'I' : [0,0,], 'J' : [0,1,1,1], 'K' : [1,0,1], 
        'L' : [0,1,0,0], 'M' : [1,1], 'N' : [1,0], 'O' : [1,1,1], 'P' : [0,1,1,0], 'Q' : [1,1,0,1],
        'R' : [0,1,0], 'S' : [0,0,0], 'T' : [1], 'U' : [0,0,1], 'V' : [0,0,0,1], 'W' : [0,1,1],
        'X' : [1,0,0,1], 'Y' : [1,0,1,1], 'Z' : [1,1,0,0], 
        0 : [1,1,1,1], 1 : [0,1,1,1], 2 : [0,0,1,1,1], 3 : [0,0,0,1,1], 4 : [0,0,0,0,1], 
        5 : [0,0,0,0,0], 6 : [1,0,0,0,0], 7 : [1,1,0,0,0], 8 : [1,1,1,0,0], 9 : [1,1,1,1,0]}
        
        
dot = 3
dash = 7
char_space = 1
word_space = 3

for char in string.upper():
    try:
        for bit in alph[char]:
            if bit == 0:
                winsound.Beep(700, 60 * dot)
            else:
                winsound.Beep(700, 60 * dash)
    except:
        pass


