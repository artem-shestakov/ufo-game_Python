import turtle


def square(x, y, size=10, color='black'):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def draw_Ufo(ufo):
    square(ufo.x, ufo.y)
    square(ufo.x+10, ufo.y+10)
    square(ufo.x+20, ufo.y+10)
    square(ufo.x+10, ufo.y-10)
    square(ufo.x+20, ufo.y-10)
    square(ufo.x+30, ufo.y)


def splash_bullet(splash):
    square(splash.x, splash.y, color='red')
    square(splash.x + 10, splash.y + 10, color='yellow')
    square(splash.x - 10, splash.y + 10, color='yellow')
    square(splash.x + 10, splash.y - 10, color='yellow')
    square(splash.x - 10, splash.y - 10, color='yellow')


def splash_bomb(splash):
    square(splash.x, splash.y, color='red')
    square(splash.x+10, splash.y+10, color='yellow')
    square(splash.x-10, splash.y+10, color='yellow')
    square(splash.x, splash.y+20, color='yellow')
    square(splash.x+20, splash.y+20, color='yellow')
    square(splash.x-20, splash.y+20, color='yellow')


