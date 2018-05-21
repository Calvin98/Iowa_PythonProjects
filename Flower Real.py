import turtle

def draw_arc(t):
    t.right(18)    
    for count in range(10):
        t.forward(10)
        t.left(4)        
    t.right(4)  
    t.right(18) 
    
def draw_squiggle(t):
    t.right(90)
    for count in range(10):
        t.forward(10)
        t.left(4)
    t.right(4)
    t.right(18)
    t.left(10)
    for count in range(10):
        t.forward(10)
        t.right(4)
    t.left(4)
    t.left(18)
    t.penup()
    t.right(90)
    for count in range(10):
        t.backward(10)
        t.left(4)
    t.right(4)
    t.right(18)
    t.left(10)
    for count in range(10):
        t.backward(10)
        t.right(4)
    t.left(4)
    t.left(18)
    t.pendown()
    

def draw_petal(t):
    t.begin_fill()
    draw_arc(t)
    t.left(180)
    draw_arc(t)
    t.left(180)
    t.end_fill()

wn = turtle.Screen()        
alex = turtle.Turtle() 
alex.color('red')
alex.fillcolor('yellow')
alex.speed(0)

n = 10

size = 30

interior_angle = 180 * (n - 2) / n
turn_angle = 180 - interior_angle

for count in range(n):
    alex.forward(size)
    petal_turn = interior_angle / 2
    alex.right(petal_turn)
    draw_squiggle(alex)
    draw_petal(alex)
    alex.left(petal_turn)
    alex.left(turn_angle)


wn.exitonclick()
        
    