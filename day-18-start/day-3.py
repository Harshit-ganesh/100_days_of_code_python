import turtle as t
import random

tim = t.Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
for x in range(3, 11):
    tim.color(random.choice(colors))
    for y in range(x):
        tim.right(360 / x)
        tim.forward(100)

screen = t.Screen()
screen.exitonclick()
