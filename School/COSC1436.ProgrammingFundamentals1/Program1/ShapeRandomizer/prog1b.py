"""
9-17-2014
Programming Project 01b
This program will take user input and draw different sized shapes to the screen.
"""

import random
import turtle

#Function to randomize colors
def color_random():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


t = turtle.Turtle()
win = turtle.Screen()
win.title("Shape Randomizer 5000")

#Create a list of directions for the computer to randomize from
random_heading = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

#Greeting and description
print("Welcome to the Shape Randomizer 5000!")
print("")
print("This program will randomize the color and heading and along with your input, it will draw some shapes!")
print("To begin, enter in the following information (ALL INPUT MUST BE INTEGERS GREATER THAN 0)")
print("")

"""
Getting user input to control the number of shapes drawn, the speed of the turtle, and the size of the shapes.
To test if user input was integers, I encased the entire input block in a while loop and tested each one using an if
statement. If input was correct, get_input is set to false and loop is exited. If input is not correct, python prints a
reminder and loop is restarted.
"""
input_error = True
while input_error:
    num_shapes = input("Enter the number of shapes to draw: ")
    print("")
    print("1-slowest\t3-slow\t\t6-normal\t10-fast\t\t0-fastest")
    speed_turtle = input("Enter the speed in which the shapes are drawn: ")
    print("")
    print("The next two inputs are used to determine the length of each edge of the shape.\nGenerally, between 100 and"
          " 350 work the best but play around with the values and see what happens.")
    min_length = input("Enter a MIN value: ")
    max_length = input("Enter a MAX value: ")
    print("")
    print("The smaller you make the next min and max, the more circular the shapes will look.\nGenerally, between 150"
          " and 170 work the best.")
    min_sides = input("Enter a MIN value: ")
    max_sides = input("Enter a MAX value: ")

    '''if num_shapes.isDigit() & speed_turtle.isDigit() & min_length.isDigit() & max_length.isDigit() & min_sides.isDigit() & max_sides.isDigit():'''
    num_shapes = int(num_shapes)
    speed_turtle = int(speed_turtle)
    min_length = int(min_length)
    max_length = int(max_length)
    min_sides = int(min_sides)
    max_sides = int(max_sides)

    input_error = False
    '''else:
        print("All input must be integers greater than 0!")'''

"""
First we set the turtle speed equal to user's input. The for loop will take the number of shapes specified by the user
and loops through the loop that many number of times. Each time, the turtle's heading is set to a random direction,
the length of the shape is set to a random number between the min and max of the user's input, and the amount of sides
is set to a random number between the min and max of the user's input. The color of each shape (line and fill) is
randomized using the color_random() function defined at the start of the program. The turtle then draws the shape as
specified using a while loop. When the absolute position of the turtle is less than 1 or in other words, when the turtle
is back to its starting point, the while loop breaks and the for loop starts again. After all shapes have been drawn,
python waits for a user's click on the graphics window before exiting.
"""
t.speed(speed_turtle)

for n in range(0, num_shapes + 1):
    x = 0
    random_left = random.randrange(min_sides, max_sides + 1)
    heading = random.choice(random_heading)
    random_forward = random.randrange(min_length, max_length)
    t.setheading(heading)
    t.color(color_random(), color_random())
    t.begin_fill()

    while x < 1:
        t.forward(random_forward)
        t.left(random_left)
        if abs(t.pos()) < 1:
            x = 2
    t.end_fill()

win.mainloop()
