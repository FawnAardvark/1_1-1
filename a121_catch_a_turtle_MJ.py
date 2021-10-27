



# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----

#-----initialize turtle-----

tri_color = "yellow"
tri_shape = "triangle"
tri_size = "2"
tri = trtl.Turtle()
tri.color(tri_color)
tri.shapesize(int(tri_size))
tri.shape(tri_shape)
font_setup = ("Arial", 20, "normal")



#-----game functions--------

new_xpos = 0
new_ypos = 0
score = 0


timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

def countdown():
  global timer, timer_up
  tri.clear()
  if timer <= 0:
    tri.penup()
    tri.speed(0)
    tri.goto(200, 200)
    tri.speed(3)
    tri.clear()
    tri.pendown()
    tri.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    tri.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    tri.getscreen().ontimer(countdown, counter_interval)
def change_position(x,y):
    tri.penup()
    global score
    score += 1
    tri.speed(0)
    tri.goto(-200, 200)
    tri.speed(3)
    tri.clear()
    tri.write(score, font=font_setup)
    tri.hideturtle()
    new_xpos = rand.randint(0, 400)
    new_ypos = rand.randint(0, 300)
    tri.goto(new_xpos, new_ypos)
    print(str(new_xpos) + ", " + str(new_ypos))
    
    tri.showturtle()

#-----events----------------
tri.onclick(change_position)


wn = trtl.Screen()    
wn.mainloop()