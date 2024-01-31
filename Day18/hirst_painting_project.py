# import colorgram

# rgb_colors = []
# colors = colorgram.extract('.\Day18\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# colors_list created by using commented out colorgram code above.
colors_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), 
               (145, 29, 36), (28, 53, 47), (55, 108, 89), (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), 
               (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213)]
tim.setheading(215)
tim.forward(500)
tim.setheading(0)
number_of_dots = 210

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)
    if dot_count % 15 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(750)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()