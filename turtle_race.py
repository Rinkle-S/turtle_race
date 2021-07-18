import turtle
from turtle import Turtle, Screen, begin_fill, bgcolor, color, end_fill, forward, goto, pendown, penup, right, shape, stamp, write
from random import randint

screen = Screen()
screen.setup(700, 400)
screen.title("Turtle Race")
bgcolor("forestgreen")

#TITLE
penup()
goto(-60,160)
color("white")
write("TURTLE RACE",font=("Arial",20,"bold"))

#Dirt track
goto(-250,150)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(500)
    right(90)
    forward(300)
    right(90)
end_fill()

#finish line
gap_size = 20
shape("square")
penup()

color("white")
#WHITE ROW1
for j in range(7):
    goto(220, (120 - (j*gap_size*2)))
    stamp()
#WHITE ROW2
for k in range(8):
    goto(220+gap_size, (140 - (k*gap_size*2)))
    stamp()
color("black")
#BLACK ROW1
for j in range(8):
    goto(220, (140 - (j*gap_size*2)))
    stamp()
#BLACK ROW2
for k in range(7):
    goto(220+gap_size, (120 - (k*gap_size*2)))
    stamp()

ringo = Turtle(shape="turtle")
ringo.color("violet")
ringo.penup()
ringo.goto(-230,100)

bingo = Turtle(shape="turtle")
bingo.color("blue")
bingo.penup()
bingo.goto(-230,60)

timmy = Turtle(shape="turtle")
timmy.color("green")
timmy.penup()
timmy.goto(-230,20)

sweety = Turtle(shape="turtle")
sweety.color("yellow")
sweety.penup()
sweety.goto(-230,-20)

loki = Turtle(shape="turtle")
loki.color("white")
loki.penup()
loki.goto(-230,-60)

groot = Turtle(shape="turtle")
groot.color("red")
groot.penup()
groot.goto(-230,-100)

turtles = [ringo, bingo, timmy, loki, groot, sweety]
user_bet = screen.textinput("User Input", "Guess, Which turtle is going to win?")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You won!!")
            else:
                print(f"You lost. {winning_colour} turtle is the winner!!")
        random_dist = randint(0,8)
        turtle.forward(random_dist)


screen.exitonclick()
