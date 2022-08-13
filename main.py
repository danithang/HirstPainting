import colorgram
import turtle as t
import random

# empty brackets to put tuple in
# rgb_colors = []
# variable to extract colors out of image
# colors = colorgram.extract('image.jpg', 30)
# for loop to add colors from image to a tuple to print
# for color in colors:
# r = color.rgb.r
# g = color.rgb.g
# b = color.rgb.b
# new_color = (r, g, b)
# appending tuple new_color to the empty brackets
# rgb_colors.append(new_color)

# print(rgb_colors)

# Because we are using rgb values colormode of Turtle has to have 255 because 255 is the biggest
t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.speed("fast")

painting_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
                   (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
                   (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
                   (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
                   (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# set heading at around 225 to make him go down at an angle, then picking a place where turtle can start then set
# heading to zero to get turtle to move forward from placed picked
tim.setheading(225)
tim.penup()
# moving forward from new position
tim.forward(300)
tim.setheading(0)
# creating a variable because there will be 100 dots in a 10 x 10 box, 101 is accounting for the range starting at 0
number_of_dots = 101

# for loop to say dot_count will continue to 100 with the range telling it to go from 1 to 100
for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(painting_colors))
    tim.forward(50)

    # commands to get the turtle to move up and start at the beginning above the first line
    # if statement means dot_count is either divisible by 10 with no remainders and turtle will go to new line and
    # continue
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(360)




tim.hideturtle()


screen = t.Screen()
screen.exitonclick()
