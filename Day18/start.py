"""
IN ORDER TO RUN THE CHALLENGES, YOU WILL NEED TO COMMENT OUT ALL OTHER CHALLENGES AND PARAMETERS INTERFERRING WITH THAT CHALLENGE
"""
import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("SteelBlue3")
# Challenge 1: Draw a square
for _ in range(4):
   tim.forward(100)
   tim.right(90)

# Challenge 2: Draw a dashed line
for _ in range(15):
   tim.forward(10)
   tim.penup()
   tim.forward(10)
   tim.pendown()

# Challenge 3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon. All in one go and on top of each other.
colors = ['green', 'red', 'yellow', 'navyblue', 'pink', 'purple', 'brown', 'aquamarine']
for i in range(3, 11):
   tim.pencolor(random.choice(colors))
   for _ in range(i):
       tim.forward(100)
       tim.right(360/i)

# Challenge 4: Draw a random walk
directions = [tim.left, tim.forward, tim.back, tim.right]
tim.pensize(10)
tim.speed(8)
i = 1
while i < 100:
   direction = random.choice(directions)
   color = random.choice(colors)
   tim.pencolor(color)
   direction(50)
   i += 1

# Alternative solution to Challenge 4 and with truly random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

turtle.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
   tim.color(random_color())
   tim.forward(50)
   tim.setheading(random.choice(directions))

# Challenge 5: Draw a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()