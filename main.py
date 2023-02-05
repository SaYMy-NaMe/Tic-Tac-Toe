from turtle import *
import turtle

WIDTH, HEIGHT = 600, 600
screen = turtle.Screen()


def draw_between(point1, point2):
    turtle.width(7)
    turtle.penup()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point2)


def draw_box(x, y, change):
    draw_between([x, y], [x + change, y])
    draw_between([x + change, y], [x + change, y - change])
    draw_between([x + change, y - change], [x, y - change])
    draw_between([x, y - change], [x, y])


def set_box():
    x, y, change = - 175, 175, 100
    for i in range(3):
        draw_box(x, y, change)
        x, y = x + change, y
    x, y, change = - 175, 75, 100
    for i in range(3):
        draw_box(x, y, change)
        x, y = x + change, y
    x, y, change = - 175, -25, 100
    for i in range(3):
        draw_box(x, y, change)
        x, y = x + change, y


def get_mouse_click_coordinate(x, y):
    turtle.onscreenclick(None)
    draw_between([x, y],[x+2, y+2])


if __name__ == '__main__':
    turtle.hideturtle()
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    set_box()
    turtle.onscreenclick(get_mouse_click_coordinate)
    turtle.mainloop()
