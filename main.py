import random
import pygame as pg
import class_Cell

pg.font.init()

score = 0
max_score = 0
a = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
r = [0, 86, 172, 258]
rx = random.randint(0, 3)
x = r[rx]
ry = random.randint(0, 3)
y = r[ry]
a[random.randint(0, 3)][rx] = class_Cell.Cell(32 + x, 134 + y)
rx = random.randint(0, 3)
x = r[rx]
ry = random.randint(0, 3)
y = r[ry]
a[random.randint(0, 3)][rx] = class_Cell.Cell(32 + x, 134 + y)
print(*a, sep='\n', end='\n\n')


main = pg.Surface((350, 353))
main.fill((200, 200, 200))
base = pg.Surface((78, 78))
base.fill((220, 220, 220))

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
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_DOWN:
                changes = True
                while changes:
                    changes = False
                    for x in range(4):
                        for y in range(3, -1, -1):
                            if a[y][x] != 0 and y != 3:
                                if a[y+1][x] != 0:
                                    if a[y+1][x].num == a[y][x].num:
                                        a[y + 1][x].num *= 2
                                        a[y][x] = 0
                                        print(*a, sep='\n', end='\n\n')
                                        changes = True
                                else:
                                    a[y][x].rect.y += 87
                                    a[y + 1][x] = a[y][x]
                                    a[y][x] = 0
                                    print(*a, sep='\n', end='\n\n')
                                    changes = True
            if e.key == pg.K_UP:
                changes = True
                while changes:
                    changes = False
                    for x in range(4):
                        for y in range(4):
                            if a[y][x] != 0 and y != 0:
                                if a[y-1][x] != 0:
                                    if a[y-1][x] == a[y][x]:
                                        a[y - 1][x] = a[y-1][x] + a[y][x]
                                        a[y][x] = 0
                                        print(*a, sep='\n', end='\n\n')
                                        changes = True
                                else:
                                    a[y - 1][x] = a[y][x]
                                    a[y][x] = 0
                                    print(*a, sep='\n', end='\n\n')
                                    changes = True


    main_display.blit(main, pg.Rect((25, 125, 0, 0)))
    for y in [132, 219, 306, 393]:
        for x in [32, 118, 204, 290]:
            main_display.blit(base, pg.Rect((x, y, 0, 0)))

    text1 = f4.render(str(score), True, (100, 100, 100))
    main_display.blit(text1, (273, 6))
    main_display.blit(text1, (338, 39))

    for line in a:
        for cell in line:
            if cell != 0:
                main_display.blit(cell.image, cell.rect)

    pg.display.update()
