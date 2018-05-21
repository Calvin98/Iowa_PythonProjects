import turtle

wn = turtle.Screen()
t = turtle.Turtle()

def spiral(n):
    for i in range(n):
        t.forward(10)
        t.left(90 - i * 2)

spiral(100)



wn.exitonclick()