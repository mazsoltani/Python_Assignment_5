import turtle

polygon = turtle.Turtle()

for num_sides in range(3,20):
    for j in range(num_sides):
        side_length = 70
        angle = 360.0 / num_sides
        polygon.forward(side_length)
        polygon.right(angle)
        
    
turtle.done()
         
    