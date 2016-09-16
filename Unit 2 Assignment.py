# Angle.py
# Ryan Ge
# September 15, 2016
# Draw an angle

# print out the purpose of this program
print('This program draws an angle with given coordnates and calculates the degree of the angle.')
print('Input two sets of coordinates, and the angle defined by them and the origin will be drawn.')
print('The degree of the angle will be printed, too.')
print('Note: the first point you input is the vertex of the angle.')

# input
first_x = int(input('Input the x coordinate of the first point:'))
first_y = int(input('Input the y coordinate of the first point:'))

second_x = int(input('Input the x coordinate of the second point:'))
second_y = int(input('Input the y coordinate of the second point:'))

# In order to calculate the degree of the angle
first_slope = first_y / first_x
second_slope = (second_y - first_y) / (second_x - first_x)

import math
angle = math.atan(abs(first_slope - second_slope) / (1 + first_slope * second_slope))
angle = angle * 180 / math.pi
angle = int(angle)

# print the angle
print('Degrees of the angle: ', angle)

# Finally draw the angle
import turtle
turtle.goto(first_x, first_y)
turtle.goto(second_x, second_y)
turtle.write(str(angle) + 'degree', False, 'left', ('Ariel', 18, 'normal'))
turtle.done()