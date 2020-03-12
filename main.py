from pixel import Pixel
from draw import square, draw_Ufo, splash
from random import choice
import turtle


UFO_HEIGHT = [250, 210, 170, 130]
UFO_DISTANCE = [300, 350]

player_score = 0
tank = [Pixel(-20, -290), Pixel(-10, -290), Pixel(0, -290), Pixel(-10, -280)]
ufos = []
bullets = []
bullet_speed = (0, 20)

def draw():
    turtle.clear()
    if ufos == []:
        ufo_gen()
    for body in tank:
        square(body.x, body.y)
    for body in ufos:
        draw_Ufo(body[0])
        body[0] += body[1]
        if body[0].x > 360 or body[0].x < -390:
             del ufos[0:1]
    for bullet in bullets:
        if bullet.y < 290:
            for ufo in ufos:
                if bullet.x >= ufo[0].x and bullet.x <= ufo[0].x + 30 and bullet.y >= ufo[0].y - 10 and bullet.y <= ufo[0].y:
                    splash(bullet)
                    ufos.remove(ufo)
                else:
                    square(bullet.x, bullet.y)
            bullet += bullet_speed
        else:
            bullets.remove(bullet)
    turtle.update()
    turtle.ontimer(draw, 100)
    

def move(somethink, value):
    for body in somethink:
        body.x += value

def shooting():
    if len(bullets) < 100:
        bullets.append(Pixel(tank[-1].x, tank[-1].y))

def ufo_gen():
    while len(ufos) < 3:
        height = choice(UFO_HEIGHT)
        distance = choice(UFO_DISTANCE)
        ufos.append([Pixel(distance, height),(-10, 0)])

            



turtle.setup(600, 600, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: move(tank, -10), 'Left')
turtle.onkey(lambda: move(tank, 10), 'Right')
turtle.onkey(lambda : shooting(), 'space')
draw()
turtle.done()