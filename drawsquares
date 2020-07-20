import turtle
bob = turtle.Turtle()
wn = turtle.Screen()

def sq (t, sz):
    bob.up()
    bob.left(90)
    bob.forward(side / 2)
    bob.right(90)
    bob.backward(side / 2)
    bob.down()
    for i in range (4):
        t.forward(sz)
        t.right(90)
        
side = 20

n = int(input("How many squares? "))

for i in range (n):
    sq(bob, side)
    bob.up()
    bob.goto(0,0)
    bob.down()
    side = side + 20

wn.exitonclick()
