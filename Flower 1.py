import turtle
import math 

wn=turtle.Screen()
pop=turtle.Turtle()



n=int(input("How many sides would you like? "))
size = int(input("How big do you want your shape? "))
Interior_angle=180*(n-2)/n
turn_angle=180-Interior_angle
start_x=-size/2
start_y=-size/2*math.tan(math.radians(n/2))

pop.penup()
pop.goto(start_x,start_y)
pop.pendown()
pop.speed(0)

for count in range(n):
    pop.forward(size)
    pop.color('red')
    pop.fillcolor('yellow')
    pop.begin_fill()
    pop.right(120)
    pop.forward(size)
    pop.right(120)
    pop.forward(size)
    pop.right(120)
    pop.forward(size)
    pop.end_fill()
    pop.left(turn_angle)
    
    
   
    
wn.exitonclick()    