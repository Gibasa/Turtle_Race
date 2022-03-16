from turtle import Turtle, Screen
import random


is_race_on = False
winner = ""
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Qual a sua aposta?", prompt="Qual tartaruga você acha que vai ganhar? Digite a cor:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            winner = turtle.pencolor()
            is_race_on = False
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

if user_bet == winner:
    print("Parabéns! Sua tartaruga venceu!")
else:
    print("Que pena! Sua tartaruga foi muito lenta.")


screen.exitonclick()
