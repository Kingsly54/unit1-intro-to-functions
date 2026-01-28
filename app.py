import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def square(x):
    t.forward(x)
    t.left(90) 
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90) 
    t.forward(x)
    t.left(90) 
def message(input): 
    print(input)

square(50)
message("h")
    
turtle.done()