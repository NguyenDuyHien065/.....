from turtle import *

shape("triangle")
speed(0)
color_list = ['red', 'blue', 'brown', 'yellow', 'grey']
a = 0
b = 3
for c in color_list:
    a = a  + 180
    color(c)
    for i in range(b):
        forward(100)
        left(180 - (a / b))
    b = b + 1




mainloop()