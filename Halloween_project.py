#halloween art group project
#made by: William Bahou and Mohammed Jasim

#--------import statements-----
import turtle as tri
import random as rand
import turtle as trtl
import turtle as score_writer
#-------config-------
tri = tri.Turtle()
#--------initialize-------
new_xpos = 0
new_ypos = 0
score = 0

tri.shape("square")
tri.fillcolor("blue")
tri.color("blue")

trtl.speed(0)
trtl.penup()
trtl.goto(-250, 250)
trtl.hideturtle()


score_writer.speed(0)
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.hideturtle()

font_setup = ("Arial", 20, "normal")
timer = 60
counter_interval = 1000

def spot_clicked(x, y):
    update_score(x, y)
    change_position()
def update_score(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  trtl.clear()
  if timer <= 0:
    trtl.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    trtl.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    trtl.getscreen().ontimer(countdown, counter_interval)
update_score()
'''
def countdown():
  global timer, timer_up
  tri.clear()
  if timer <= 0:
    trtl.write("Time's Up", font=font_setup)
    timer_up = True

  else:
    trtl.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    tri.getscreen().ontimer(countdown, counter_interval)
'''
score = 0
def change_position(x,y):
    tri.penup()
    global score
    score += 1
    new_xpos = rand.randint(0, 400)
    new_ypos = rand.randint(0, 300)
    tri.goto(new_xpos, new_ypos)
    print(str(new_xpos) + ", " + str(new_ypos))
    


tri.onclick(spot_clicked)


#------functions-----

#----events---------
wn = trtl.Screen()
'''
wn.addshape('candy1.gif')
t.shape('candy1.gif')
'''
wn.ontimer(countdown, counter_interval)
wn.mainloop()