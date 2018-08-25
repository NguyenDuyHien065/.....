from turtle import *
turtle_list = []



turtle_list = []
for i in range (5):
    t = Turtle ()
    turtle_list.append(t)
m = 90
position = int(input("Turtle position :"))

color_str = (input("Choose your color:"))
shape_str = (input("Shape"))
turtle_list[position - 1]
turtle_list[position-1].color(color_str)
turtle_list[position - 1].shape(shape_str)


for tt in turtle_list:
    tt.forward(100)

    tt.left(m)
    tt.forward(200)
    m += 90







mainloop()
