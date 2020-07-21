import turtle

def DrawSpiral (t, sd):
    for i in (range(0, 125, 3)):
        t.forward (i)
        t.left(180 - ((sd * 180 - 360) / sd))

bob = turtle.Turtle()
wn = turtle.Screen()
bob.shape("turtle")

side = int(input("number of sides: "))
DrawSpiral(bob, side)
