import turtle as t
import math as mt

my_turtle = t.Turtle()
my_win = t.Screen()

def draw_spiral(my_turtle,line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle,line_len - 5)


def draw_circle(my_turtle,radius,delta):
    angle = mt.atan(delta / radius)
 #  num = mt.ceil( 2*(mt.pi * radius) / delta)
    num = mt.ceil(360 / angle) 

    for i in range(num):
        my_turtle.forward(delta)
        my_turtle.right(angle)
        

draw_circle(my_turtle,2,1)
    
#draw_spiral(my_turtle,100)
my_win.exitonclick()
    
