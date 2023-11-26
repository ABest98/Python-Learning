from turtle import *

sides = 0
shape = input()

def move_and_turn(angle) :
  forward(50)
  right(angle)

if "square" in shape :
  while sides < 4 :
    sides += 1
    move_and_turn(90)
elif "octagon" in shape :
  while sides < 8 :
    sides += 1
    move_and_turn(45)
else :
  circle(50)


done()