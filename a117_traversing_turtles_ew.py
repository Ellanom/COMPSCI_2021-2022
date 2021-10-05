#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  my_turtles.append(t)

# create the starting point variable for each loop
startx = 0
starty = 0
direction = 15
spiral = 15

# give the turtles a command and a direction to go 
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.right(45)     
  t.forward(spiral)

# change the starting point for each turtle in the loop
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()
  spiral = spiral + 15

wn = trtl.Screen()
wn.mainloop()
