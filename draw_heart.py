  
import turtle
wn = turtle.Screen()
ava = turtle.Turtle()
bob = turtle.Turtle()

ava.shape("turtle")
ava.color("LightPink")
ava.pensize(5)
ava.speed(7)

bob.shape("turtle")
bob.color("LightBlue")
bob.pensize(5)
bob.speed(7)

import math
pi = math.pi
dis = pi * 50 / 360
dis2 = pi * 135 / 360


def DrawHeart (turtle_name, turn):
    turtle_name.up()
    turtle_name.left(90)
    turtle_name.forward(50)
    turtle_name.down()
    for i in range(180):
        turn(1)
        turtle_name.forward(dis)
    for i in range(85):
        turn(1)
        turtle_name.forward(dis2)

DrawHeart (ava, ava.left)
DrawHeart (bob, bob.right)
cccccc
