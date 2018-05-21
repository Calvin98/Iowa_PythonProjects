# Draws a "flower" by adding a petal-like shape to each vertex
# of a polygon.  Illustrates problem-solving with procedural
# decomposition:
#
# Can we solve a simpler problem?  Can we solve part of the problem?
# - draw just the n-gon? (We know this one, done in lab)
# - draw just one petal?
# - draw just one arc of a petal?
#    - try a concrete example: turn right 10 degrees, 
#      draw 10 segments and turn 4 degrees left each time?
# - draw a straight line extending out from each vertex
import turtle

def draw_arc(t):
    '''
    Draws an arc consisting of 10 segments, turning 4 degrees after each segment.
    The arc is oriented in the turtle's initial direction, and the 
    turtle faces the same direction at the end of the arc.
    '''
    # With 10 segments, there will be only 9 internal angles within the arc,
    # which is a total of 36 degrees. 
    # To end up along the same line as the turtle's direction, the initial 
    # right turn should be half the sum of the internal angles, or 18 degrees.
    t.right(18)    
    for count in range(10):
        t.forward(10)
        t.left(4)        
    
    # to straighten out so we're facing the same direction, we need to 
    # undo the last left turn, and then undo the initial 18 degree turn
    t.right(4)  
    t.right(18) 

def draw_petal(t):
    '''
    Draws a filled pair of arcs.
    '''
    t.begin_fill()
    draw_arc(t)
    t.left(180)
    draw_arc(t)
    t.left(180)
    t.end_fill()

# set up a turtle
wn = turtle.Screen()        
alex = turtle.Turtle() 
alex.color('red')
alex.fillcolor('yellow')
alex.speed(0)

# number of sides
n = 10

# length of each side
size = 30

# code to draw a polygon
interior_angle = 180 * (n - 2) / n
turn_angle = 180 - interior_angle

for count in range(n):
    alex.forward(size)
    
    # warm-up problem: at each vertex, draw a line sticking out
    #petal_turn = interior_angle / 2
    #alex.right(petal_turn)        
    #alex.forward(50)
    #alex.backward(50)
    #alex.left(petal_turn)
    
    # at each vertex, draw a petal
    petal_turn = interior_angle / 2
    alex.right(petal_turn)    
    draw_petal(alex)
    alex.left(petal_turn)
    
    # continue with the polygon
    alex.left(turn_angle)


wn.exitonclick()