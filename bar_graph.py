import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")

def bar_draw(t, height):
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(height)
    t.left(90)
    bob.up()
    t.forward(10)
    bob.down()

bob.up()
bob.goto(-150,-150)
bob.down()

bar = int(input("How many bars do you want? "))

    
for i in range(bar):
    ht = int(input("What is the value? "))
    bar_draw(bob, ht)
bob.goto(-150,-150)
wn.exitonclick()