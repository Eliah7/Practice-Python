import turtle
import random as rn

def tree(branch_len,t,size,green):
    if branch_len > 5 and size > 0:
        t.pensize(size)
        t.pendown()
        t.pencolor(0,green,0)
        t.forward(branch_len)
        
        t.right(20)
        tree(branch_len - 15,t,size-1.5,green+0.1)
        t.left(40)
        tree(branch_len - 10,t,size-1.5,green+0.1)
        t.right(20)
        t.penup()
        t.backward(branch_len)
        
def main():
   t = turtle.Turtle()
   my_win = turtle.Screen()
   t.left(90)
   t.up()
   t.backward(100)
   t.down()
   t.color(0,0,0)
   tree(100, t,12,0)
   my_win.exitonclick()

main()
