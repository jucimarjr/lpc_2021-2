import turtle


def create_screen():
    # draw screen

    screen.title("My Pong")
    screen.bgcolor("black")
    screen.setup(width=1000, height=750)


def setup_turtle_border_pen():
    turtle_border_pen.color("white")
    turtle_border_pen.pensize(3)
    turtle_border_pen.speed(6)


def move_turtle_border_pen_to_bottom_left():
    turtle_border_pen.penup()
    turtle_border_pen.hideturtle()
    turtle_border_pen.goto(-500, -375)
    turtle_border_pen.showturtle()
    turtle_border_pen.pendown()


def draw_canvas_border():
    turtle_border_pen.forward(1000)
    turtle_border_pen.left(90)
    turtle_border_pen.forward(750)
    turtle_border_pen.left(90)
    turtle_border_pen.forward(1000)
    turtle_border_pen.left(90)
    turtle_border_pen.forward(750)
    turtle_border_pen.hideturtle()


def setup_turtle_hud_pen():
    turtle_hud_pen.speed(0)
    turtle_hud_pen.shape("square")
    turtle_hud_pen.color("white")


def move_turtle_hud_pen_and_draw_score():
    turtle_hud_pen.penup()
    turtle_hud_pen.hideturtle()
    turtle_hud_pen.goto(0, 260)
    turtle_hud_pen.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def draw_player_one():
    turtle_player_one_pen.hideturtle()
    turtle_player_one_pen.speed(0)
    turtle_player_one_pen.shape("square")
    turtle_player_one_pen.color("white")
    turtle_player_one_pen.shapesize(stretch_wid=5, stretch_len=1)
    turtle_player_one_pen.penup()
    turtle_player_one_pen.goto(-450, 0)
    turtle_player_one_pen.showturtle()


def draw_player_two():
    turtle_player_two_pen.hideturtle()
    turtle_player_two_pen.speed(0)
    turtle_player_two_pen.shape("square")
    turtle_player_two_pen.color("white")
    turtle_player_two_pen.shapesize(stretch_wid=5, stretch_len=1)
    turtle_player_two_pen.penup()
    turtle_player_two_pen.goto(450, 0)
    turtle_player_two_pen.showturtle()


def draw_ball():
    turtle_ball.speed(0)
    turtle_ball.shape("square")
    turtle_ball.color("white")
    turtle_ball.penup()
    turtle_ball.goto(0, 0)
    turtle_ball.dx = 1
    turtle_ball.dy = 1


def move_player_one_up():
    player_one_y_position = turtle_player_one_pen.ycor()
    if player_one_y_position < 325:
        player_one_y_position += 25
    else:
        player_one_y_position = 325
    turtle_player_one_pen.sety(player_one_y_position)


def move_player_one_down():
    print("Move player 1 down")


def move_player_two_up():
    print("Move player 2 up")


def move_player_two_down():
    print("Move player 2 down")


def setup_players_control():
    screen.listen()
    screen.onkeypress(move_player_one_up, "w")
    screen.onkeypress(move_player_one_down, "s")
    screen.onkeypress(move_player_two_up, "Up")
    screen.onkeypress(move_player_two_down, "Down")


if __name__ == '__main__':
    screen = turtle.Screen()

    turtle_border_pen = turtle.Turtle()
    turtle_hud_pen = turtle.Turtle()

    turtle_player_one_pen = turtle.Turtle()
    turtle_player_two_pen = turtle.Turtle()
    turtle_ball = turtle.Turtle()

    player_one_score = 0
    player_two_score = 0

    create_screen()
    setup_turtle_border_pen()
    move_turtle_border_pen_to_bottom_left()
    draw_canvas_border()

    # head-up display
    setup_turtle_hud_pen()
    move_turtle_hud_pen_and_draw_score()

    # draw paddle 1
    draw_player_one()

    # draw paddle 2
    draw_player_two()

    # draw ball
    draw_ball()

    setup_players_control()

    turtle.done()
