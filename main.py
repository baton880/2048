import pygame as pg
pg.font.init()

score = 0
max_score = 0
main_display = pg.display.set_mode((400,550))
main_display.fill((255, 255, 240))
pg.display.set_caption("2048 GAME")


game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    surf1 = pg.Surface((350, 353))
    surf1.fill((200, 200, 200))
    main_display.blit(surf1, pg.Rect((25, 125, 0, 0)))
    x = 32
    for i in range(4):
        surf1 = pg.Surface((78, 78))
        surf1.fill((220, 220, 220))
        main_display.blit(surf1, pg.Rect((x, 132, 0, 0)))
        x += 86
    x = 32
    for i in range(4):
        surf1 = pg.Surface((78, 78))
        surf1.fill((220, 220, 220))
        main_display.blit(surf1, pg.Rect((x, 219, 0, 0)))
        x += 86
    x = 32
    for i in range(4):
        surf1 = pg.Surface((78, 78))
        surf1.fill((220, 220, 220))
        main_display.blit(surf1, pg.Rect((x, 306, 0, 0)))
        x += 86
    x = 32
    for i in range(4):
        surf1 = pg.Surface((78, 78))
        surf1.fill((220, 220, 220))
        main_display.blit(surf1, pg.Rect((x, 393, 0, 0)))
        x += 86

    f1 = pg.font.Font('Volkswagen medium.ttf', 18)
    text1 = f1.render('Use arrow keys to move. ''2+2=4. Reach 2048', True, (100, 100, 100))
    main_display.blit(text1, (27, 485))

    f2 = pg.font.Font('Volkswagen medium.ttf', 50)
    text1 = f2.render('2048', True, (100, 100, 100))
    main_display.blit(text1, (30, 15))

    f4 = pg.font.Font('Volkswagen medium.ttf', 30)
    text1 = f4.render('Score:', True, (100, 100, 100))
    main_display.blit(text1, (190, 5))

    f6 = pg.font.Font('Volkswagen medium.ttf', 30)
    text1 = f6.render('Max score:', True, (100, 100, 100))
    main_display.blit(text1, (190, 38))

    f3 = pg.font.Font('Volkswagen medium.ttf', 30)
    text1 = f3.render(str(score), True, (100, 100, 100))
    main_display.blit(text1, (273, 6))

    f5 = pg.font.Font('Volkswagen medium.ttf', 30)
    text1 = f5.render(str(max_score), True, (100, 100, 100))
    main_display.blit(text1, (338, 39))


    pg.display.update()