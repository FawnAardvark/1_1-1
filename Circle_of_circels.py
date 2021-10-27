import turtle as trtl

painter = trtl.Turtle()
painter.speed(100)
painter.shape('circle')

count = 0
while (count < 18):
    painter.pendown()
    painter.circle(12.5)
    painter.penup()
    painter.forward(20)
    painter.right(20)
    count = count + 1
wn = trtl.Screen()
wn.mainloop()