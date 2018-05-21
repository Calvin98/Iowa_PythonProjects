import turtle

wn = turtle.Screen()        
t = turtle.Turtle() 
t.color('red')
t.fillcolor('yellow')


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
    t.begin_fill()
    draw_leafarc(t)
    t.left(180)
    draw_leafarc(t)
    t.left(180)
    t.end_fill()
    t.fillcolor('red')
    t.begin_fill()
    draw_leafarc2(t)
    t.left(180)
    draw_leafarc2(t)
    t.left(180)
    t.end_fill()
    t.fillcolor('yellow')

draw_leaf(t)

wn.exitonclick()


