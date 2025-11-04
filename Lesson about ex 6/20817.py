print(28*13+84*78-7*24)
from turtle import *

screensize(3000, 3000)
tracer(False)
lt(90)
m = 5

for i in range(3):
    fd(27 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()
for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()

for x in range(-30, 20):
    for y in range(-60, 40):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()