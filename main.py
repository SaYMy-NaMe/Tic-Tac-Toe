from turtle import *
import turtle

bgcolor('black')
title("Tic Tac Toe Game Made by Ashraf")
pencolor('white')
turtle.speed(0)
WIDTH, HEIGHT = 600, 600
screen = turtle.Screen()
check_point = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_turn = 1


def draw_between(point1, point2):
    turtle.width(3)
    turtle.penup()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point2)


def set_box():
    draw_between([-175, 75], [125, 75])
    draw_between([-175, -25], [125, -25])
    draw_between([-75, 175], [-75, -125])
    draw_between([25, 175], [25, -125])


def terminate_func():
    pencolor('orange')
    pensize(5)
    if check_point[0] == check_point[3] == check_point[6] == 1:
        penup()
        goto(-125, 175)
        pendown()
        goto(-125, -125)
        turtle.exitonclick()
    elif check_point[1] == check_point[4] == check_point[7] == 1:
        penup()
        goto(-25, 175)
        pendown()
        goto(-25, -125)
        turtle.exitonclick()
    elif check_point[2] == check_point[5] == check_point[8] == 1:
        penup()
        goto(75, 175)
        pendown()
        goto(75, -125)
        turtle.exitonclick()
    elif check_point[0] == check_point[3] == check_point[6] == 1:
        penup()
        goto(-125, 175)
        pendown()
        goto(-125, -125)
        turtle.exitonclick()
    elif check_point[1] == check_point[4] == check_point[7] == 1:
        penup()
        goto(-25, 175)
        pendown()
        goto(-25, -125)
        turtle.exitonclick()
    elif check_point[2] == check_point[5] == check_point[8] == 1:
        penup()
        goto(75, 175)
        pendown()
        goto(75, -125)
        turtle.exitonclick()

    elif check_point[0] == check_point[3] == check_point[6] == 2:
        penup()
        goto(-125, 175)
        pendown()
        goto(-125, -125)
        turtle.exitonclick()
    elif check_point[1] == check_point[4] == check_point[7] == 2:
        penup()
        goto(-25, 175)
        pendown()
        goto(-25, -125)
        turtle.exitonclick()
    elif check_point[2] == check_point[5] == check_point[8] == 2:
        penup()
        goto(75, 175)
        pendown()
        goto(75, -125)
        turtle.exitonclick()
    elif check_point[0] == check_point[3] == check_point[6] == 2:
        penup()
        goto(-125, 175)
        pendown()
        goto(-125, -125)
        turtle.exitonclick()
    elif check_point[1] == check_point[4] == check_point[7] == 2:
        penup()
        goto(-25, 175)
        pendown()
        goto(-25, -125)
        turtle.exitonclick()
    elif check_point[2] == check_point[5] == check_point[8] == 2:
        penup()
        goto(75, 175)
        pendown()
        goto(75, -125)
        turtle.exitonclick()


def draw_cross(x, y):
    global number_of_turn
    pencolor('red')
    if (-175 < x < -75) and (75 < y < 175) and (check_point[0] == 0):
        turtle.width(3)
        draw_between([-155, 155], [-95, 95])
        draw_between([-155, 95], [-95, 155])
        check_point[0] = 1
        number_of_turn = number_of_turn + 1
        print(check_point)
    if (-75 < x < 25) and (75 < y < 175) and (check_point[1] == 0):
        turtle.width(3)
        draw_between([-55, 155], [5, 95])
        draw_between([-55, 95], [5, 155])
        check_point[1] = 1
        number_of_turn = number_of_turn + 1
        print(check_point)
    if (25 < x < 125) and (75 < y < 175) and (check_point[2] == 0):
        turtle.width(3)
        draw_between([45, 155], [105, 95])
        draw_between([45, 95], [105, 155])
        number_of_turn = number_of_turn + 1
        check_point[2] = 1
        print(check_point)
    if (-175 < x < -75) and (-25 < y < 75) and (check_point[3] == 0):
        turtle.width(3)
        draw_between([-155, 55], [-95, -5])
        draw_between([-155, -5], [-95, 55])
        number_of_turn = number_of_turn + 1
        check_point[3] = 1
        print(check_point)
    if (-75 < x < 25) and (-25 < y < 75) and (check_point[4] == 0):
        turtle.width(3)
        draw_between([-55, 55], [5, -5])
        draw_between([-55, -5], [5, 55])
        number_of_turn = number_of_turn + 1
        check_point[4] = 1
        print(check_point)
    if (25 < x < 125) and (-25 < y < 75) and (check_point[5] == 0):
        turtle.width(3)
        draw_between([45, 55], [105, -5])
        draw_between([45, -5], [105, 55])
        number_of_turn = number_of_turn + 1
        check_point[5] = 1
        print(check_point)
    if (-175 < x < -75) and (-125 < y < -25) and (check_point[6] == 0):
        turtle.width(3)
        draw_between([-155, -45], [-95, -105])
        draw_between([-155, -105], [-95, -45])
        number_of_turn = number_of_turn + 1
        check_point[6] = 1
        print(check_point)
    if (-75 < x < 25) and (-125 < y < 25) and (check_point[7] == 0):
        turtle.width(3)
        draw_between([-55, -45], [5, -105])
        draw_between([-55, -105], [5, -45])
        number_of_turn = number_of_turn + 1
        check_point[7] = 1
        print(check_point)
    if (25 < x < 125) and (-125 < y < -25) and (check_point[8] == 0):
        turtle.width(3)
        draw_between([45, -45], [105, -105])
        draw_between([45, -105], [105, -45])
        number_of_turn = number_of_turn + 1
        check_point[8] = 1
        print(check_point)
    terminate_func()


def draw_circle(x, y):
    global number_of_turn
    pencolor('yellow')
    if (-175 < x < -75) and (75 < y < 175) and (check_point[0] == 0):
        turtle.width(3)
        turtle.penup()
        goto(-125, 95)
        pendown()
        turtle.circle(30)
        check_point[0] = 2
        number_of_turn = number_of_turn + 1
        print(check_point)
    if (-75 < x < 25) and (75 < y < 175) and (check_point[1] == 0):
        turtle.width(3)
        turtle.penup()
        goto(-25, 95)
        pendown()
        turtle.circle(30)
        check_point[1] = 2
        number_of_turn = number_of_turn + 1
        print(check_point)
    if (25 < x < 125) and (75 < y < 175) and (check_point[2] == 0):
        turtle.width(3)
        turtle.penup()
        goto(75, 95)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[2] = 2
        print(check_point)
    if (-175 < x < -75) and (-25 < y < 75) and (check_point[3] == 0):
        turtle.width(3)
        turtle.penup()
        goto(-125, -5)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[3] = 2
        print(check_point)
    if (-75 < x < 25) and (-25 < y < 75) and (check_point[4] == 0):
        turtle.width(3)
        turtle.penup()
        goto(-25, -5)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[4] = 2
        print(check_point)
    if (25 < x < 125) and (-25 < y < 75) and (check_point[5] == 0):
        turtle.width(3)
        turtle.penup()
        goto(75, -5)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[5] = 2
        print(check_point)
    if (-175 < x < -75) and (-125 < y < -25) and (check_point[6] == 0):
        turtle.width(3)
        turtle.penup()
        goto(-125, -105)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[6] = 2
        print(check_point)
    if (-75 < x < 25) and (-125 < y < 25) and (check_point[7] == 0):
        turtle.width(3)
        turtle.penup()
        goto(-25, -105)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[7] = 2
        print(check_point)
    if (25 < x < 125) and (-125 < y < -25) and (check_point[8] == 0):
        turtle.width(3)
        turtle.penup()
        goto(75, -105)
        pendown()
        turtle.circle(30)
        number_of_turn = number_of_turn + 1
        check_point[8] = 2
        print(check_point)
    terminate_func()


def get_mouse_click_coordinate(x, y):
    global number_of_turn
    if (-175 < x < 125) and (-125 < y < 175):
        if number_of_turn % 2 != 0:
            draw_cross(x, y)
        else:
            draw_circle(x, y)


if __name__ == '__main__':
    turtle.hideturtle()
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    turtle.penup()
    setposition(-187, -175)
    turtle.pendown()
    turtle.write("Hey! Welcome to Ashraf's Tic Tac Toe", font=('monaco', 15, 'bold'), align='left')
    set_box()
    turtle.onscreenclick(get_mouse_click_coordinate)
    turtle.mainloop()
