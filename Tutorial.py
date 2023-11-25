from random import *
from turtle import *

num = 0

for x in range(10) :
  num += 1
  print(num)

while num < 20 :
  num += 1
  print(num)

random_number = randrange(1, 10)

forward(randrange(20, 100))
left(randrange(0,360))
forward(randrange(20, 100))

done()