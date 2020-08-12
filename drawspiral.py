print("Hello, user!")
print(" ")

like = input("Do you like spirals?")
print(" ")
#asks if you like spirals

if like == "yes" or like == "Yes" or like == "yep" or like == "yup" or like == "yeah":
    print("Well, that's nice. I don't.")
elif like == "no" or "No" or "nope":
    print("Well, then we have something in common! Not liking spirals!")
else:
    print("Well, whatever will work.")
print(" ")        
#responds accordingly 
#needs improvement -> it should be able to tell if the answer is a yes, no, or sth else
    #improved

for say in ["So, let's get right to the point:", " ", "This program draws a spiral,", " ", "and the number of angles it'll have depends on... YOU!"]:
    print(say)
    #briefly introduces the objective of the program

print(" ")
    
choice = input("So, how many angles (per a layer of spiral) do you want?")
print(" ")
#gets user input for the wanted shape

while type(choice) == str:
    try:
        choice = int(choice)
        if choice < 3:
            print("Input error, try again.")
            print(" ")
            choice = input("So, how many angles (per a layer of spiral) do you want?")
            print(" ")
    except ValueError:
        print("Input error, try again.")
        print(" ")
        choice = input("So, how many angles (per a layer of spiral) do you want?")
        print(" ")

print("So it's", choice, ", huh? Got that.")
print(" ")
#makes sure that the input is a valid number (>2)

import turtle 
wn = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
#turtle setting

for l in (range(0, 125, 3)):
    bob.forward(l)
    bob.left(180 - ((choice * 180 - 360) / choice))
 #draws the spiral

print("No need to thank me.") 
