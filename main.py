import turtle
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def get_racers():
    turtles = []
    start_x = -300
    start_y = -150

    for color in COLORS:
        t = turtle.Turtle()
        t.penup()
        t.shape('turtle')
        t.shapesize(2)
        t.color(color)
        t.speed(0)
        t.goto(start_x, start_y)
        turtles.append(t)
        start_y += 60

    return turtles


if __name__ == '__main__':
    s = turtle.getscreen()
    s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    bet = s.textinput("Place your bets", "Which turtle do you think will win?")
    
    s.tracer(False)
    racers = get_racers()
    s.tracer(True)
    
    winner = ""
    finished = False

    while not finished:
        for number, racer in enumerate(racers):
            speed = random.randint(1, 15)
            racer.forward(speed)

            if racer.xcor() > 300:
                finished = True
                winner = COLORS[number]

    if bet == winner:
        print(f'You Win! The {winner} turtle was the winner')
    else:
        print(f'You Lost! The {winner} turtle was the winner')

    turtle.bye()
