import numpy as np
from PIL import Image
from shapes import Square, Rectangle
from canvas import Canvas

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))
canvas_color = input("Enter canvas color (white or black): ")

if canvas_color == 'white':
    canvas_color = [255, 255, 255]
else:
    canvas_color = [0, 0, 0]

canvas = Canvas(canvas_width, canvas_height, canvas_color)

while True:
    shape = input("What do you want to draw? Enter quit to quit.")
    if shape == 'quit':
        break
    else:
        if shape == 'rectangle':
            # Rectangle dimensions
            rect_x = int(input("Enter x of the rectangle: "))
            rect_y = int(input("Enter y of the rectangle: "))
            rect_width = int(input("Enter width of the rectangle: "))
            rect_height = int(input("Enter height of the rectangle: "))

            # Rectangle color
            rect_red = int(input("How much red should the rectangle have: "))
            rect_green = int(input("How much green should the rectangle have: "))
            rect_blue = int(input("How much blue should the rectangle have: "))
            rect_color = [rect_red, rect_green, rect_blue]

            rect = Rectangle(rect_x, rect_y, rect_width, rect_height, rect_color)
            rect.draw(canvas)
        elif shape == 'square':
            # Square dimensions
            square_x = int(input("Enter x of the square: "))
            square_y = int(input("Enter y of the square: "))
            square_side = int(input("Enter side length of the square: "))

            # Square color
            square_red = int(input("How much red should the square have: "))
            square_green = int(input("How much green should the square have: "))
            square_blue = int(input("How much blue should the square have: "))
            square_color = [square_red, square_green, square_blue]

            square = Square(square_x, square_y, square_side, square_color)
            square.draw(canvas)

canvas.make("canvas.png")