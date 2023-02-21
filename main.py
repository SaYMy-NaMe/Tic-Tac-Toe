from turtle import *
import turtle

bgcolor('black')
title("Tic Tac Toe Game Made by Ashraf")
pencolor('green')
turtle.speed(0)
WIDTH, HEIGHT = 600, 600
screen = turtle.Screen()
check_point = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def draw_between(point1, point2):
    turtle.width(3)
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


def draw_cross(x, y):
    pencolor('red')
    if (-175 < x < -75) and (75 < y < 175) and (check_point[0] == 0):
        turtle.width(3)
        draw_between([-155, 155], [-95, 95])
        draw_between([-155, 95], [-95, 155])
        check_point[0] = 1
        print(check_point)
    if (-75 < x < 25) and (75 < y < 175) and (check_point[1] == 0):
        turtle.width(3)
        draw_between([-55, 155], [5, 95])
        draw_between([-55, 95], [5, 155])
        check_point[1] = 1
        print(check_point)
    if (25 < x < 125) and (75 < y < 175) and (check_point[2] == 0):
        turtle.width(3)
        draw_between([45, 155], [105, 95])
        draw_between([45, 95], [105, 155])
        check_point[2] = 1
        print(check_point)
    if (-175 < x < -75) and (-25 < y < 75) and (check_point[3] == 0):
        turtle.width(3)
        draw_between([-155, 55], [-95, -5])
        draw_between([-155, -5], [-95, 55])
        check_point[3] = 1
        print(check_point)
    if (-75 < x < 25) and (-25 < y < 75) and (check_point[4] == 0):
        turtle.width(3)
        draw_between([-55, 55], [5, -5])
        draw_between([-55, -5], [5, 55])
        check_point[4] = 1
        print(check_point)
    if (25 < x < 125) and (-25 < y < 75) and (check_point[5] == 0):
        turtle.width(3)
        draw_between([45, 55], [105, -5])
        draw_between([45, -5], [105, 55])
        check_point[5] = 1
        print(check_point)
    if (-175 < x < -75) and (-125 < y < -25) and (check_point[6] == 0):
        turtle.width(3)
        draw_between([-155, -45], [-95, -105])
        draw_between([-155, -105], [-95, -45])
        check_point[6] = 1
        print(check_point)
    if (-75 < x < 25) and (-125 < y < 25) and (check_point[7] == 0):
        turtle.width(3)
        draw_between([-55, -45], [5, -105])
        draw_between([-55, -105], [5, -45])
        check_point[7] = 1
        print(check_point)
    if (25 < x < 125) and (-125 < y < -25) and (check_point[8] == 0):
        turtle.width(3)
        draw_between([45, -45], [105, -105])
        draw_between([45, -105], [105, -45])
        check_point[8] = 1
        print(check_point)


def get_mouse_click_coordinate(x, y):
    if (-175 < x < 125) and (-125 < y < 175):
        draw_cross(x, y)


if __name__ == '__main__':
    turtle.hideturtle()
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    set_box()
    turtle.onscreenclick(get_mouse_click_coordinate)
    turtle.mainloop()
