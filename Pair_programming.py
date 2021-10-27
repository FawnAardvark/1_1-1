import turtle as trtl
import random
t = trtl.Turtle()
t.speed(0)
def triangle(a):
    hyp = a* 2 **0.5
    t.forward(a)
    t.left(135)
    t.forward(hyp)
    t.left(135)
    t.forward(a)
def square(color,size):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
colors = ['red', 'blue', 'green', 'pink', 'yellow', 'orange', 'black']

for i in range(400):
    numb = random.randint(0,6)
    color = colors[int(numb)]
    square(color, 200)
    t.right(1)

t.fillcolor("white")
t.begin_fill()
t.penup()
t.goto(-400,-400)
t.pendown()
t.pencolor("white")
t.setheading(0)
triangle(800)
t.end_fill()
t.penup()

'''
for i in range(360):
    numb = random.randint(0,6)
    color = colors[int(numb)]
    square(color, 50)
    t.right(1)
'''
'''
for i in range(120):
    numb = random.randint(0,6)
    color = colors[int(numb)]
    circle(color)
    t.right(3)
'''
wn = trtl.Screen()   
wn.mainloop()
