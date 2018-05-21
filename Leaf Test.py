import turtle

wn = turtle.Screen()        
t = turtle.Turtle() 
t.color('red')
t.fillcolor('yellow')


t.right(18)    
for count in range(10):
      t.forward(18)
      t.left(8)

t.right(4)  
t.right(18) 
  
wn.exitonclick()