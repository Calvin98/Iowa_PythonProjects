import turtle

def draw_arc(t):
    t.right(18)    
    for count in range(10):
        t.forward(10)
        t.left(4)        
    t.right(4)  
    t.right(18)
    
def draw_leafarc(t):
    t.right(18)    
    for count in range(10):
        t.forward(20)
        t.left(4)        
    t.right(4)  
    t.right(18) 
    
def draw_leafarc2(t):
    t.right(18)    
    for count in range(10):
        t.forward(10)
        t.left(4)        
    t.right(4)  
    t.right(18) 
    
    
def draw_leaf(t):
    t.color('green')
    t.fillcolor('light green')
    t.begin_fill()
    draw_leafarc(t)
    t.left(180)
    draw_leafarc(t)
    t.left(180)
    t.end_fill()
    t.fillcolor('dark green')
    t.begin_fill()
    draw_leafarc2(t)
    t.left(180)
    draw_leafarc2(t)
    t.left(180)
    t.end_fill()
    t.color('red')
    t.fillcolor('yellow')
    
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
    draw_leaf(t)
    t.penup()
    t.right(10.3)
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
    t.left(80)
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
    
for count in range(10):
    alex.forward(size * 1/2)
    draw_squiggle(alex)
    alex.forward(size * 1/2)
    petal_turn = interior_angle * 1/2 
    alex.right(petal_turn)    
    draw_petal(alex)
    alex.left(petal_turn)
    alex.left(turn_angle)



wn.exitonclick()
        
    