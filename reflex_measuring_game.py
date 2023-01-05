import turtle
import random
import time

def score(x,y):
    global p

    p+=1
    show.clear()
    show.write("Score: {}".format(p),align="center", font= ("Courier", 24, "normal"))
    shape.goto(random.randint(-300,300),random.randint(-300,300))




board =turtle.Screen()
board.title("Reflex Measuring Game")
board.bgcolor("lightblue")
board.setup(width=600, height=600)

shape=turtle.Turtle()
shape.speed(0)
shape.shape("circle")
shape.color("red")
shape.shapesize(3)
shape.penup()
shape.goto(random.randint(-300,300),random.randint(-300,300))
p=0
show= turtle.Turtle()
show.shape("square")
show.speed(0)
show.color("black")
show.penup()
show.goto(0,260)
show.hideturtle()
show.write("Start", align="center", font= ("Courier", 24, "normal"))


time_duration=7
while True:
    beginning_time= time.time()
    while(time.time()- beginning_time)< time_duration:
        shape.onclick(score)

    else:

        p=0
        show.clear()
        show.write("Start: {}".format(p), align="center", font= ("Courier",24,"normal"))




