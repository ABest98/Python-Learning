from turtle import *
from random import *

bgcolor("#030302")
hideturtle()
speed(0)

screen_width = window_width()
screen_height = window_height()

number_of_stars = 0

def starry_night() :

  x_pos = randrange(-screen_width, screen_width)
  y_pos = randrange(-screen_height, screen_height)

  size = randrange(1, 25)
  
  penup()
  goto(x_pos, y_pos)
  pendown()
  dot(size, "#f7f7f5")

print("How many stars would you like to be in your night sky ?")
user_amount = int(input())


while number_of_stars < user_amount :
  number_of_stars += 1
  starry_night()


done()