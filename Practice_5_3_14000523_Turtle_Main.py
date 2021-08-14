import turtle

polygon = turtle.Turtle()
num_sides = 3
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
num_sides = num_sides+1
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
num_sides = num_sides+1
side_length = 70
angle = 360.0 / num_sides     
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
num_sides = num_sides+1
side_length = 70
angle = 360.0 / num_sides     
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
num_sides = num_sides+1
side_length = 70
angle = 360.0 / num_sides     
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
         
turtle.done()