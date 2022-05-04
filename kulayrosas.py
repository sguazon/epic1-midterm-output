#Shina Guazon - BSCS 1B 
#MIDTERM OUTPUT

import turtle

sg = turtle.Turtle()
sr = turtle.Screen()

sr.title("flower power! girl power!")
sr.bgcolor('black')

sr.setworldcoordinates(-500,-500,500,500)
sg.speed(0)

fleur_leaf1 = 400
fleur_span1 = 90
fleur_angle1 = 90
fleur_angle2 = 135
fleur_leaf2 = 400
fleur_span2 = 80
fleur_angle3 = 100
fleur_angle4 = 145

set1 = ['green']
set2 = ['pink', 'hot pink', 'white']
set3 = ['white']

def leaves():
        sg.color(set1)
        sg.pensize(2)
        sg.goto(0,0)
        sg.circle(fleur_leaf1,fleur_span1)
        sg.left(fleur_angle1)   
        sg.circle(fleur_leaf1,fleur_span1)
        sg.left(fleur_angle2)
        sg.circle(fleur_leaf2,fleur_span2)
        sg.left(fleur_angle3)   
        sg.circle(fleur_leaf2,fleur_span2)
        sg.left(fleur_angle4)

def stem():
        sg.color(set3)
        sg.goto(0,0)
        sg.pensize(8)
        sg.forward(600)

def fleur():
    for i in range(350):
        sg.color(set2[i%3])
        sg.pendown()
        sg.circle(255-i,90)
        sg.left(90)
        sg.circle(255-i,80)
        sg.left(18)
        sg.circle(255-i,18)     
        sg.left(9)

leaves()

for i in range(30):
        leaves()
        fleur_leaf1 -= 10
        fleur_span1 += .5
        fleur_leaf2 -= 10
        fleur_span2 += .5
        fleur_angle1 -= .5
        fleur_angle2 -= .5
        fleur_angle3 -= .5
        fleur_angle4 -= .5

stem()

sg.penup()
sg.goto(40,10)
sg.pensize(2)

fleur()

sg.hideturtle()
sr.exitonclick()

#References: 
#petal & leaves - https://pythonturtle.academy/tutorial-drawing-a-flower-petal-or-a-leaf-with-python-turtle/ 
#number of petals - https://pythonturtle.academy/sixteen-petal-flower-with-python-turtle/
#flower pattern idea - https://www.youtube.com/watch?v=vMBrDD2mwl8
