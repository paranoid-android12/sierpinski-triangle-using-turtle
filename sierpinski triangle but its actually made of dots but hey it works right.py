import turtle
import random
loop = False
first = 0
second = 0
third = 0
dist = 0
t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-350,-280)
t.down()
first = t.xcor(),	t.ycor()
t.fd(650)
second = t.xcor(),	t.ycor()
t.rt(-120)
t.fd(650)
third = t.xcor(),	t.ycor()
t.rt(-120)
t.fd(650)

t.rt(140)
t.up()

t.fd(60)

coords = [first, second, third]
loop = True
while loop:
    rand = random.randint(1,3)
    if rand == 1:
        t.setheading(t.towards(first[0], first[1]))
        dist = t.distance(first)
        t.fd(dist/2)
        t.dot(4)
    if rand == 2:
        t.setheading(t.towards(second[0], second[1]))
        dist = t.distance(second)
        t.fd(dist/2)
        t.dot(4)
    if rand == 3:
        t.setheading(t.towards(third[0], third[1]))
        dist = t.distance(third)
        t.fd(dist/2)
        t.dot(4)



