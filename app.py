import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(0)
""" t.forward(200)
def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90) 
    square(50)
def message(input): 
    print(input)
message("hi") """

""" def equal(x): 
    for i in range(3):
     t.forward(x)
     t.left(120)
equal(90) """

""" def right():
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(135)
    t.forward(50)
right() """
""" def rectangle(x):
    for i in range(4):
        t.forward(x+25)
        t.left(90) 
rectangle(100)        
 """

def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)  
def squareright5 (iRange):
    length=100
    for i in range(iRange):
        square(100,90)
        t.right(5)
        

squareright5(60)
 
'''def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)  
def doublesquares(iRange):
    length=25
    for i in range(iRange):
        square(length,90)
        length=length*2
doublesquares(5) '''


'''def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)  
def addsquares(iRange):
    length=25
    for i in range(iRange):
        square(length,90)
        length+=25
addsquares(5) '''
'''def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)  
def squares (iRange):
    length=5
    for i in range(iRange):
        square(length,90)
        t.right(5)
        length+=5

squares(60) '''
'''
def star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)  
def stars (iRange):
    length=5
    for i in range(iRange):
        star(length,144)
        t.right(5)
        length+=5

stars(65)
'''



        
    
turtle.done()

    