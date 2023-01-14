import turtle
a=turtle.Screen()
a.bgcolor("black")
t=turtle.Turtle()
t.speed("fastest")
t.color("white")
rotate=int(180)

def Circles(c,size):
    for i in range(10):
        c.circle(size)
        size=size-4
def Func(c,size,rep):
    for i in range(rep):
        Circles(c,size)
        c.right(360/rep)
Func(t,200,10)
t1=turtle.Turtle()
t1.speed(0)
t1.color("blue")
rotate=int(90)

def Circles(c,size):
    for i in range(4):
        c.circle(size)
        size=size-10
def Func(c,size,rep):
    for i in range(rep):
        Circles(c,size)
        c.right(360/rep)

Func(t1,160,10)

t2=turtle.Turtle()
t2.speed(0)
t2.color("red")
rotate=int(80)

def Circles(c,size):
    for i in range(4):
        c.circle(size)
        size=size-5

def Func(c,size,rep):
    for i in range(rep):
        Circles(c,size)
        c.right(360/rep)

Func(t2,120,10)

t3=turtle.Turtle()
t3.speed(0)
t3.color("green")
rotate=int(90)

def Circles(c,size):
    for i in range(4):
        c.circle(size)
        size=size-19

def Func(c,size,rep):
    for i in range(rep):
        Circles(c,size)
        c.right(360/rep)
Func(t3,80,10)

t4=turtle.Turtle()
t4.speed(0)
t4.color("yellow")
rotate=int(90)

def Circles(c,size):
    for i in range(4):
        c.circle(size)
        size=size-20

def Func(c,size,rep):
    for i in range(rep):
        Circles(c,size)
        c.right(360/rep)

Func(t4,40,10)

turtle.done()