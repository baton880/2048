import pygame as pg
import random
pg.init()
f4 = pg.font.Font('Volkswagen medium.ttf', 30)
class Cell:

    def __init__(self, x, y):
        self.image = pg.Surface((78, 78))
        self.image.fill((250, 250, 240))
        self.rect = self.image.get_rect(x=x, y=y)
        self.num = random.choice([2,4])
        text1 = f4.render(str(self.num), True, (100, 100, 100))
        self.image.blit(text1, (29, 19))

    # def update(self):
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_DOWN]:
    #         while self.rect.y < 309:
    #             self.rect.y += 87
    #     if keys[pg.K_UP]:
    #         while self.rect.y > 134:
    #             self.rect.y -= 87
    #     if keys[pg.K_LEFT]:
    #         while self.rect.x > 32:
    #             self.rect.x -= 86
    #     if keys[pg.K_RIGHT]:
    #         while self.rect.x < 290:
    #             self.rect.x += 86