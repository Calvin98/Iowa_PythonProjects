import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

# number of sides
n = 10

# length of each side
size = 30

interior_angle = 180 * (n - 2) / n
turn_angle = 180 - interior_angle
for count in range(n):
    alex.forward()

interior_angle = 180 * (n - 2) / n
turn_angle = 180 - interior_angle
for count in range(n):
    alex.forward(size)
    alex.left(turn_angle)

wn.exitonclick()
