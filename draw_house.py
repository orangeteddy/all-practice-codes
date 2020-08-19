import turtle as trtl

t = trtl.Turtle()
wn = trtl.Screen()

t.shape("turtle")
t.turtlesize(3)
t.pensize(7)
wn.bgcolor("SkyBlue")

t.up()
t.goto(-190,-150)
t.down()

t.fillcolor("green")
t.begin_fill()
for i in (380, 75, 380, 75):
  t.forward(i)
  t.right(90)
t.end_fill()

t.fillcolor("wheat1")
t.up()
t.goto(-125,-150)
t.left(90)
t.down()

t.begin_fill()
for i in (150, 250, 150):
  t.forward(i)
  t.right(90)
t.end_fill()

t.fillcolor("orangered")
t.up()
t.goto(-125, 0)
t.begin_fill()
t.right(135)
t.down()
t.forward(175)
t.goto(125,0)
t.left(45)
t.end_fill()

t.up()
t.goto(-75,-150)
t.down()

t.fillcolor("mediumslateblue")
t.begin_fill()
for i in (100, 75, 100):
  t.forward(i)
  t.right(90)
t.end_fill()

t.fillcolor("white")

for i in (-150, -115, -80):
  t.up()
  t.goto(i, 150)
  t.begin_fill()
  if i == -150 or i == -80:
    t.circle(30)
  else:
    t.goto(i, 160)
    t.circle(37)
  t.end_fill()
  
for i in (80, 115, 150):
  t.goto(i, 185)
  t.begin_fill()
  if i == 150 or i == 80:
    t.circle(30)
  else:
    t.goto(i, 195)
    t.circle(37)
  t.end_fill()
  
t.shape("circle")
t.turtlesize(1)
t.color("black")
t.pencolor("black")
t.goto(-52,-100)
t.stamp()

wn = trtl.exitonclick()
