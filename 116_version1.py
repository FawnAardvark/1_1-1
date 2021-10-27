#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20) # Spider body

legs = 8
'''y = 70'''
leg_length = 70
angle_leg = 180 / legs
print("angle_leg = ", angle_leg)
spider.pensize(5)# spider legs width
angle_increasing = 4


def eye():
    position_eye = 0
    for i in range(2):
        spider.penup()
        spider.goto(0 + position_eye, 20)
        spider.pendown()
        spider.fillcolor("red")
        spider.begin_fill()
        spider.circle(10)
        spider.end_fill()
        position_eye += 25



while (angle_increasing < legs): #Draw legs
  spider.goto(0,20)
  spider.setheading(angle_leg*angle_increasing)
  spider.forward(leg_length)
  print("angle_leg*angle_increasing = ", angle_leg*angle_increasing)
  angle_increasing = angle_increasing + 1
angle_increasing =4
while (angle_increasing < legs): #Draw legs
  spider.goto(0,25)
  spider.setheading(180-angle_leg*-angle_increasing)
  spider.forward(leg_length)
  print("angle_leg*angle_increasing = ", angle_leg*angle_increasing)
  angle_increasing = angle_increasing + 1

eye()

wn = trtl.Screen()
wn.mainloop()