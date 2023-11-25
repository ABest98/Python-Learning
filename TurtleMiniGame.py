from turtle import *

move_distance = 20
speed(0)

bgcolor("#D2691E")
# Going to the starting position for the ocean
penup()
goto(500, 685)
pendown()

# Changing color to blue
color("blue")

# Filling in the ocean area
begin_fill()
goto(1500, 685)
goto(1500, -685)
goto(500, -685)
goto(500, 685)
end_fill()

# Moves marker back to starting position
penup()
goto(-200,0)
shape("turtle")
color("green")

# Setting up functions for moving
def move_up() :
  # Rotates turtle to face up
  setheading(90)
  forward(move_distance)
  check_goal()

def move_down() :
  setheading(270)
  forward(move_distance)
  check_goal()

def move_left() :
  setheading(180)
  forward(move_distance)
  check_goal()

def move_right() :
  setheading(0)
  forward(move_distance)
  check_goal()

# Setting up function that will determine if you won
def check_goal() :
  if xcor() > 500 :
    # Hiding the turtle
    hideturtle()
    color("white")
    # Displaying a message for winning
    write("YOU WIN!")
    # Turns off the onkey listeners
    onkey(None, "Up")
    onkey(None, "Down")
    onkey(None, "Left")
    onkey(None, "Right")

# Assigning key inputs to movement functions
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
# Makes python wait and listen for key inputs
listen()

done()