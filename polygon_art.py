import turtle
import random


class Polygon:
    def __init__(self, num_sides, color, speedx, speedy, locationx, locationy):
        self.num_sides = num_sides
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.locationx = locationx
        self.locationy = locationy

    def draw_polygon(num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)
        turtle.penup()

    def get_new_color(colors):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        colors.append(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # draw a polygon at a random location, orientation, color, and border line thickness
    def initilizing(num_sides, size, orientation, location, color, border_size):
        num_sides.append(random.randint(3, 5))  # triangle, square, or pentagon
        size.appned(random.randint(50, 150))
        orientation.append(random.randint(0, 90))
        location.append([random.randint(-300, 300), random.randint(-200, 200)])
        color.append(get_new_color())
        border_size.append(random.randint(1, 10))
        draw_polygon(num_sides, size, orientation, location, color, border_size)


# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
def move_polygon(location, size):
    size *= reduction_ratio
    turtle.penup()
    turtle.forward(size * (1 - reduction_ratio) / 2)
    turtle.left(90)
    turtle.forward(size * (1 - reduction_ratio) / 2)
    turtle.right(90)
    location[0] = turtle.pos()[0]
    location[1] = turtle.pos()[1]


# adjust the size according to the reduction ratio


# draw the second polygon embedded inside the original 


num_sides = int(input("Number of sides to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
turtle.colormode(255)
color_list = []
size = []
orientation = []
location = []
border_size = []
ball_color = []
Polygon.initilizing(num_sides, size, orientation, location, color, border_size)
while True:
    turtle.clear()
    for i in range(num_sides):
        num_sides.draw_polygon(num_sides, size, orientation, location, color, border_size)
        num_sides.move_polygon(location, size)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
