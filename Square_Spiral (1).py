import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
size = 10


for n in range(25):
    alex.forward(size)
    alex.left(90)
    size = size + 10
