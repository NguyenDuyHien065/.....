from turtle import *
print("No capital word in your turtle command !!!")
hien = Turtle ()
while True :
    command = input("Command to move the turtle[fd , lt , rt , bd] ")
    command_list = command.split(" ")
    print(command)



    for turtle in command_list:
        if turtle == "fd" :
            hien.forward(100)
        elif turtle == "lt":
            hien.left(90)
        elif turtle == "rt":
            hien.right(90)
        elif turtle == "bd":
            hien.backward(90)
        else :
            print("You can only use fd , lt , rt , bd , to move the turtle . TRY AGAIN")





mainloop()