import random
import pygame as pg

pg.font.init()

xx = 32
yy = 132
r = [0, 86, 172, 258]
num1 = [2, 4]
xx = 32 + random.choice(r)
yy = 134 + random.choice(r)
num = str(random.choice(num1))
score = 0
max_score = 0

main_display = pg.display.set_mode((400, 550))
main_display.fill((255, 255, 240))
pg.display.set_caption("2048 GAME")

f1 = pg.font.Font('Volkswagen medium.ttf', 18)
text1 = f1.render('Use arrow keys to move. ''2+2=4. Reach 2048', True, (100, 100, 100))
main_display.blit(text1, (27, 485))

f2 = pg.font.Font('Volkswagen medium.ttf', 50)
text1 = f2.render('2048', True, (100, 100, 100))
main_display.blit(text1, (30, 15))

f4 = pg.font.Font('Volkswagen medium.ttf', 30)
text1 = f4.render('Score:', True, (100, 100, 100))
main_display.blit(text1, (190, 5))

text1 = f4.render('Max score:', True, (100, 100, 100))
main_display.blit(text1, (190, 38))

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_LEFT:
                while xx > 32:
                    xx -= 86
            elif e.key == pg.K_RIGHT:
                while xx < 290:
                    xx += 86
            elif e.key == pg.K_DOWN:
                while yy < 308:
                    yy += 87
            elif e.key == pg.K_UP:
                while yy > 133:
                    yy -= 87

    surf1 = pg.Surface((350, 353))
    surf1.fill((200, 200, 200))
    main_display.blit(surf1, pg.Rect((25, 125, 0, 0)))
    surf1 = pg.Surface((78, 78))
    surf1.fill((220, 220, 220))
    for y in [132, 219, 306, 393]:
        for x in [32, 118, 204, 290]:
            main_display.blit(surf1, pg.Rect((x, y, 0, 0)))

    text1 = f4.render(str(score), True, (100, 100, 100))
    main_display.blit(text1, (273, 6))
    main_display.blit(text1, (338, 39))

    surf1 = pg.Surface((78, 78))
    surf1.fill((250, 250, 240))
    main_display.blit(surf1, pg.Rect((xx, yy, 0, 0)))
    text1 = f4.render(num, True, (100, 100, 100))
    main_display.blit(text1, (xx + 29, yy + 19))

    pg.display.update()
