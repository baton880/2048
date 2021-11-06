import pygame as pg
import random
pg.init()
f4 = pg.font.Font('Volkswagen medium.ttf', 30)
colors = {2:(250, 250, 240),
          4:'#EDDEC7',
          8:'#F2B07A',
          16:'#F29261',
          32:'#F57A5E',
          64:'#F65E3E',
          128:'#EDCE73',
          256:'#ECCA5F',
          512:'#EFC851',
          1024:'#EDC541',
          2048:'#EABD2C'}
class Cell:

    def __init__(self, x, y):
        self.num = random.choice([2,4])
        self.image = pg.Surface((78, 77))
        self.image.fill(colors[self.num])
        self.rect = self.image.get_rect(x=x, y=y)
        text1 = f4.render(str(self.num), True, (100, 100, 100))
        self.image.blit(text1, (29, 19))

    def move_UP(self):
        self.rect.y -= 87

    def move_DOWN(self):
        self.rect.y += 87

    def move_RIGHT(self):
        self.rect.x += 87

    def move_LEFT(self):
        self.rect.x -= 87

    def double(self):
        self.num *= 2
        if self.num > 2048:
            self.image.fill(colors[64])
        else:
            self.image.fill(colors[self.num])
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