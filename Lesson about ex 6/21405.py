print(28*13+84*78-7*24)
from turtle import *

screensize(3000, 3000)
tracer(False)
lt(90)
m = 20
rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()

for x in range(-30, 20):
    for y in range(-60, 40):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()