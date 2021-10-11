import pygame as pg


main_display = pg.display.set_mode((400,550))
main_display.fill((255, 255, 240))

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

pg.display.update()

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False