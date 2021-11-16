import random
import pygame as pg
import class_Cell

pg.font.init()

score = 0
with open('max_score.txt', 'r') as mx:
    max_score = int(mx.read())

matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
r = [0, 86, 172, 258]


def game_over ():
    with open('max_score.txt', 'r') as mx:
        maxss = int(mx.read())
    if maxss < score:
        with open('max_score.txt', 'w') as mx:
            mx.write(str(score))

# Создание первых двух клеточек
def create_cell():
    while True:
        rx = random.randint(0, 3)
        ry = random.randint(0, 3)
        if matrix[ry][rx] == 0:
            matrix[ry][rx] = class_Cell.Cell(32 + r[rx], 134 + r[ry])
            break
create_cell()
create_cell()
print(*matrix, sep='\n', end='\n\n')

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
text_score = f4.render('Score:', True, (100, 100, 100))
text_max = f4.render('Max:', True, (100, 100, 100))

game = True
while game:
    movement = False
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game_over()
            game = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_DOWN:
                changes = True
                while changes:
                    changes = False
                    for x in range(4):
                        for y in range(3, -1, -1):
                            if matrix[y][x] != 0 and y != 3:
                                if matrix[y + 1][x] != 0:
                                    if matrix[y + 1][x].num == matrix[y][x].num:
                                        matrix[y + 1][x].double()
                                        score += matrix[y + 1][x].num
                                        matrix[y][x] = 0
                                        print(*matrix, sep='\n', end='\n\n')
                                        changes = True
                                        movement = True
                                else:
                                    matrix[y][x].move_DOWN()
                                    matrix[y + 1][x] = matrix[y][x]
                                    matrix[y][x] = 0
                                    print(*matrix, sep='\n', end='\n\n')
                                    changes = True
                                    movement = True
            if e.key == pg.K_UP:
                    changes = True
                    while changes:
                        changes = False
                        for x in range(4):
                            for y in range(4):
                                if matrix[y][x] != 0 and y != 0:
                                    if matrix[y - 1][x] != 0:
                                        if matrix[y - 1][x].num == matrix[y][x].num:
                                            matrix[y - 1][x].double()
                                            score += matrix[y - 1][x].num
                                            matrix[y][x] = 0
                                            print(*matrix, sep='\n', end='\n\n')
                                            changes = True
                                            movement = True
                                    else:
                                        matrix[y][x].move_UP()
                                        matrix[y - 1][x] = matrix[y][x]
                                        matrix[y][x] = 0
                                        print(*matrix, sep='\n', end='\n\n')
                                        changes = True
                                        movement = True
            if e.key == pg.K_RIGHT:
                    changes = True
                    while changes:
                        changes = False
                        for y in range(4):
                            for x in range(4):
                                if matrix[y][x] != 0 and x != 3:
                                    if matrix[y][x+1] != 0:
                                        if matrix[y][x+1].num == matrix[y][x].num:
                                            matrix[y][x+1].double()
                                            score += matrix[y][x+1].num
                                            matrix[y][x] = 0
                                            print(*matrix, sep='\n', end='\n\n')
                                            changes = True
                                            movement = True
                                    else:
                                        matrix[y][x].move_RIGHT()
                                        matrix[y][x+1] = matrix[y][x]
                                        matrix[y][x] = 0
                                        print(*matrix, sep='\n', end='\n\n')
                                        changes = True
                                        movement = True
            if e.key == pg.K_LEFT:
                    changes = True
                    while changes:
                        changes = False
                        for y in range(4):
                            for x in range(3, -1, -1):
                                if matrix[y][x] != 0 and x != 0:
                                    if matrix[y][x-1] != 0:
                                        if matrix[y][x-1].num == matrix[y][x].num:
                                            matrix[y][x-1].double()
                                            score += matrix[y][x-1].num
                                            matrix[y][x] = 0
                                            print(*matrix, sep='\n', end='\n\n')
                                            changes = True
                                            movement = True
                                    else:
                                        matrix[y][x].move_LEFT()
                                        matrix[y][x-1] = matrix[y][x]
                                        matrix[y][x] = 0
                                        print(*matrix, sep='\n', end='\n\n')
                                        changes = True
                                        movement = True

    if movement == True:
        create_cell()

    pg.draw.rect(main_display, (255, 255, 240), (150, 0, 250, 100))

    main_display.blit(main, pg.Rect((25, 125, 0, 0)))

    for y in [132, 219, 306, 393]:
        for x in [32, 118, 204, 290]:
            main_display.blit(base, pg.Rect((x, y, 0, 0)))

    #Score и max score
    text1 = f4.render(str(score), True, (100, 100, 100))
    text1_rect = text1.get_rect(right=390, top=6)
    main_display.blit(text1, text1_rect)
    text_score_rect =  text_score.get_rect(right=text1_rect.left-10, top=text1_rect.top-1)
    main_display.blit(text_score, text_score_rect)

    text_m = f4.render(str(max_score), True, (100, 100, 100))
    text_m_rect = text_m.get_rect(right=390, top=38)
    main_display.blit(text_m, text_m_rect)
    text_max_rect =  text_max.get_rect(right=text_m_rect.left-10, top=text_m_rect.top-1)
    main_display.blit(text_max, text_max_rect)


    for line in matrix:
        for cell in line:
            if cell != 0:
                main_display.blit(cell.image, cell.rect)

    pg.display.update()

# TODO кнопки
# TODO game over