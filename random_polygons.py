"""
Name(s): Zekarias Asaminew and Yonatan Wakie
CSC 201
Lab 3

This program draws random triangles and quadrilaterals in a window with random colors.

Did you complete this lab file during the class period (yes or no)?

If no, leave the one that applies. If yes, delete this entire section!
    I completed random_polygons.py with my partner from class.

    Document any assistance you get if you complete the lab after the class period:
    
    No assistance was given outside the classrrom. 


"""
from graphics2 import *
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BORDER = 10

def main():
    shape = int(input('Should I draw triangles(1) or a quads(2)? '))
    num_shape = int(input('How many should I draw? '))
    
    window = GraphWin('Shapes', WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    
    num_sides = 0
    if shape == 1:
        num_sides = 3
    elif shape == 2:
        num_sides = 4
    else:
        print('')
        exit(-1)
    
    for num in range(num_shape):
        vertex_list = []
        
        for count in range(num_sides):
            x = random.randrange(BORDER, WINDOW_WIDTH - (BORDER+1))
            y = random.randrange(BORDER, WINDOW_HEIGHT- (BORDER+1))
            vertex = Point(x,y)
            vertex_list.append(vertex)
        
        red = random.randrange(0, 256)
        green = random.randrange(0, 256)
        blue = random.randrange(0, 256)
        color = color_rgb(red, green, blue)
        
        polygon = Polygon(vertex_list)
        
        polygon.setFill(color)
        polygon.draw(window)

main()