from turtle import *

# Initial Ballon Diameter
diameter = 50
# Diameter that the Ballon will pop at
pop_diameter = 200
# Function to draw initial balloon
def draw_ballon() :
  color("#d90f0f")
  dot(diameter)
# Function to increase ballon size
def inflate_balloon() :
  global diameter
  diameter += 10
  draw_ballon()
  # Conditional statement if diameter is more than or equal to pop_diameter the balloon pops 
  if diameter >= pop_diameter :
    clear()
    diameter = 40
    write("POP!")

draw_ballon()
# Assigns function inflate_balloon to the up arrow key
onkey(inflate_balloon, "Up")
# Will keep program running to listen for keypress 
listen()

done()