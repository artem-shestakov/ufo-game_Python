import turtle

def square(x, y, size = 10, collor = 'black'):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(collor)
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

def splash(splash):
    square(splash.x, splash.y, collor='red')
    square(splash.x+10, splash.y+10, collor='yellow')
    square(splash.x-10, splash.y+10, collor='yellow')
    square(splash.x+10, splash.y-10, collor='yellow')
    square(splash.x-10, splash.y-10, collor='yellow')


