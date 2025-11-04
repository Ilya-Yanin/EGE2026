print(29*19+31*8-8*15)
from turtle import *

screensize(6000, 6000)
tracer(False)
lt(90)
m = 5

for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()

for x in range(-5, 85):
    for y in range(-5, 60):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()