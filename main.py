from pixel import Pixel
from draw import square, draw_Ufo, splash_bomb, splash_bullet
from random import choice
import turtle



UFO_HEIGHT = [250, 210, 170, 130]
UFO_DISTANCE = [-390, -350, 300, 350]
UFO_SPEED = [(-5, 0), (-10, 0), (-15, 0), (-20, 0), (-25, 0), (-30, 0),
             (5, 0), (10, 0), (15, 0), (20, 0), (25, 0), (30, 0)]

level = 1
player_score = 0
tank = [Pixel(-20, -290), Pixel(-10, -290), Pixel(0, -290), Pixel(-10, -280)]
ufos = []
bullets = []
bombs = []
tank_speed = [Pixel(-10, 0), Pixel(10, 0)]
bomb_speed = Pixel(0, -10)
bullet_speed = (0, 40)

def draw():
    global player_score
    global level
    global bomb_speed
    turtle.clear()
    if len(ufos) < level:
        ufo_gen()
    for body in tank:
        square(body.x, body.y)
    for body in ufos:
        draw_Ufo(body[0])
        body[0] += body[1]
        if body[0].x > 360 or body[0].x < -390:
             ufos.remove(body)
        if body[0].x == tank[1].x:
            bombs.append(Pixel(body[0].x, body[0].y))
    for bullet in bullets:
        if bullet.y < 290:
            for ufo in ufos:
                if bullet.x >= ufo[0].x and bullet.x <= ufo[0].x + 30 and bullet.y >= ufo[0].y - 10 \
                   and bullet.y <= ufo[0].y:
                    splash_bullet(bullet)
                    ufos.remove(ufo)
                    bullets.remove(bullet)
                    player_score += 1
                    if player_score > 0 and player_score % 5 == 0:
                        level += 1
                        bomb_speed += Pixel(0, -5)
                else:
                    square(bullet.x, bullet.y)
            bullet += bullet_speed
        else:
            bullets.remove(bullet)
    for bomb in bombs:
        bomb.move(bomb_speed)
        if bomb.y <= -290:
            bomb.y = -290
        square(bomb.x, bomb.y, color="red")
        for tank_body in tank:
            if tank_body.x == bomb.x and tank_body.y == bomb.y:
                splash_bomb(tank_body)
                turtle.up()
                turtle.goto(0, 0)
                turtle.down()
                turtle.hideturtle()
                turtle.color('black')
                turtle.write("*** Game Over *** You destroyed {} UFO".format(player_score), align='center',
                             font=('Courier', 24, 'bold'))
                return
        if bomb.y <= -290:
            bombs.remove(bomb)
    turtle.update()
    turtle.ontimer(draw, 100)
    

def move(somethink, value):
    if -300 < somethink[0].x < 280:
        for body in somethink:
            body.move(value)


def shooting():
    if len(bullets) < 100:
        bullets.append(Pixel(tank[-1].x, tank[-1].y))


def ufo_gen():
    height = choice(UFO_HEIGHT)
    distance = choice(UFO_DISTANCE)
    if level <= 2:
        if distance > 0:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[0:2])])
        else:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[6:8])])
    elif 2 < level <= 4:
        if distance > 0:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[0:4])])
        else:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[6:10])])
    elif 4 < level <= 6:
        if distance > 0:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[:6])])
        else:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[6:])])
    elif 6 < level:
        if distance > 0:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[2:6])])
        else:
            ufos.append([Pixel(distance, height), choice(UFO_SPEED[8:])])


turtle.setup(600, 600, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: move(tank, tank_speed[0]), 'Left')
turtle.onkey(lambda: move(tank, tank_speed[1]), 'Right')
turtle.onkey(lambda: shooting(), 'space')
draw()
turtle.done()
