from turtle import *

def move_and_turn(distance, angle) :
  forward(distance)
  left(angle)

# Changing color of the background
bgcolor("black")
# Changing color of the pen
color("red")
# Starting point to fill an object
begin_fill()
# Creating two circles
circle(50)
circle(-50)
# End point of filling an object
end_fill()

color("blue")

circle(100)
circle(-100)

color("green")

circle(150)
circle(-150)

color("gold")

# Clears the screen
clear()

begin_fill()

move_and_turn(100, 120)
move_and_turn(100, 120)
move_and_turn(100, 120)
forward(100)

end_fill()

# Picks the pen up
penup()
forward(50)
# Places the pen back down
pendown()

forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)

done()