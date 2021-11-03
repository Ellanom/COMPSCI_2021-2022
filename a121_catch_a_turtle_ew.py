# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
turt = trtl.Turtle()
import random as rand1
rand = rand1.Random()
import turtle as trtl1
scorewr = trtl1.Turtle()
import turtle as trtl2
counter = trtl2.Turtle()
#-----game configuration----
trt_color = "purple"
trt_shape = "turtle"
trt_size = 3
turt.penup()
turt.color(trt_color)
turt.shape(trt_shape)
turt.shapesize(trt_size)

scorewr.hideturtle()
scorewr.penup()
scorewr.goto(-50,250)
score = 0

font_setup = ("Arial",20,"normal")

counter.hideturtle()
counter.penup()
counter.goto(20,250)
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

turtle_colors = ["#eccfd1", "#eccfe4", "#dacfec", "#cfe3ec", "#cfecd8", "#eaeccf", "#ecddcf"]
turtle_sizes = [.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

#-----game functions--------
def trt_clicked(x,y):
    global timer_up, timer
    if timer_up != True:
        update_score()
        change_position()
        size_change()
        color_change()
    else:
        turt.hideturtle()

def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    new_angle = rand.randint(-360,360)
    turt.setheading(new_angle)
    turt.goto(new_xpos,new_ypos)

def update_score():
    global score
    score = score + 1
    scorewr.clear()
    scorewr.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def color_change():
    new_color = rand.choice(turtle_colors)
    turt.color(new_color)
    turt.stamp()
    turt.color("purple")

def size_change():
    new_size = rand.choice(turtle_sizes)
    turt.shapesize(new_size)
#-----events---------------- 
turt.onclick(trt_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor('#eeecec')
wn.mainloop()
