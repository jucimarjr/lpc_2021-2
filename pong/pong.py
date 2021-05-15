import functools
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


def move_player_down(key):
    player_map_control = {'s': turtle_player_one_pen,
                          'Down': turtle_player_two_pen}
    player_position = player_map_control[key].ycor()
    if player_position > -325:
        player_position -= 25
    else:
        player_position = -325
    player_map_control[key].sety(player_position)


def move_player_up(key):
    player_map_control = {'w': turtle_player_one_pen,
                          'Up': turtle_player_two_pen}
    player_position = player_map_control[key].ycor()
    if player_position < 325:
        player_position += 25
    else:
        player_position = 325
    player_map_control[key].sety(player_position)


def setup_players_control():
    screen.listen()
    screen.onkeypress(functools.partial(move_player_up, "w"), key="w")
    screen.onkeypress(functools.partial(move_player_down, "s"), key="s")
    screen.onkeypress(functools.partial(move_player_up, "Up"), key="Up")
    screen.onkeypress(functools.partial(move_player_down, "Down"), key="Down")


def ball_touched_player_two_horizontally():
    return 425 < turtle_ball.xcor() < 435


def ball_touched_player_two_vertically():
    return turtle_player_two_pen.ycor() + 60 > turtle_ball.ycor() > turtle_player_two_pen.ycor() - 60


def ball_touched_player_two_top():
    return turtle_player_two_pen.ycor() + 60 > turtle_ball.ycor() > turtle_player_two_pen.ycor()


def ball_touched_player_one_horizontally():
    return -425 > turtle_ball.xcor() > - 435


def ball_touched_player_one_vertically():
    return turtle_player_one_pen.ycor() + 60 > turtle_ball.ycor() > turtle_player_one_pen.ycor() - 60


def ball_hit_player_vertically_on_top(turtle_player):
    return turtle_player.ycor() + 60 > turtle_ball.ycor() > turtle_player.ycor()


def ball_hit_player_vertically_on_bottom(turtle_player):
    return turtle_player.ycor() > turtle_ball.ycor() > turtle_player.ycor() - 60


def ball_hit_player_on_center(turtle_player):
    return turtle_player.ycor() + 10 > turtle_ball.ycor() > turtle_player.ycor() - 10


if __name__ == '__main__':
    screen = turtle.Screen()

    turtle_border_pen = turtle.Turtle()
    turtle_hud_pen = turtle.Turtle()

    turtle_player_one_pen = turtle.Turtle()
    turtle_player_two_pen = turtle.Turtle()
    turtle_ball = turtle.Turtle()

    player_one_score = 0
    player_two_score = 0
    turtle_ball_x_velocity = 5
    turtle_ball_y_velocity = 0

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

    while True:
        turtle_ball.setx(turtle_ball.xcor() + turtle_ball_x_velocity)
        turtle_ball.sety(turtle_ball.ycor() + turtle_ball_y_velocity)

        if ball_touched_player_two_horizontally() and ball_touched_player_two_vertically():
            turtle_ball_x_velocity *= -1
            if ball_hit_player_vertically_on_top(turtle_player_two_pen):
                turtle_ball_y_velocity += 10
            elif ball_hit_player_vertically_on_bottom(turtle_player_two_pen):
                turtle_ball_y_velocity -= 10
            elif ball_hit_player_on_center(turtle_player_two_pen):
                turtle_ball_y_velocity = 0

        if ball_touched_player_one_horizontally() and ball_touched_player_one_vertically():
            turtle_ball_x_velocity *= -1
            if ball_hit_player_vertically_on_top(turtle_player_one_pen):
                turtle_ball_y_velocity += 10
            elif ball_hit_player_vertically_on_bottom(turtle_player_one_pen):
                turtle_ball_y_velocity -= 10
            elif ball_hit_player_on_center(turtle_player_one_pen):
                turtle_ball_y_velocity = 0

        if turtle_ball.ycor() > 365:
            turtle_ball.sety(365)
            turtle_ball_y_velocity *= -1

        if turtle_ball.ycor() < -365:
            turtle_ball.sety(-365)
            turtle_ball_y_velocity *= -1

        if turtle_ball.xcor() > 490:
            player_one_score += 1
            turtle_hud_pen.clear()
            turtle_hud_pen.write("{} : {}".format(player_one_score, player_two_score), align="center",
                                 font=("Press Start 2P", 24, "normal"))
            turtle_ball.setposition(0, 0)
            turtle_ball_y_velocity = 0

        if turtle_ball.xcor() < -490:
            player_two_score += 1
            turtle_hud_pen.clear()
            turtle_hud_pen.write("{} : {}".format(player_one_score, player_two_score), align="center",
                                 font=("Press Start 2P", 24, "normal"))
            turtle_ball.setposition(0, 0)
            turtle_ball_y_velocity = 0
