# Разработай свою игру в этом файле!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))



        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset (self):
        windom.blit(self.image, (self.rect.x, self.rekt.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_x)


        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x_speed  += self.x_speed

            platforms_touched = sprite.spritecollide(self, barriers, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed < 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)
            if self.y_speed > 0:
                for p in platforms_touched:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
            elif self.y_speed < 0:
                for p in platforms_touched:
                    self.rect.top = max(self.rect.top, p.rect.bottom)



win_width = 700
win_height = 500
display.set_caption("Лабиринт")
windom = display.set_mode((win_width, win_height))
black = (119, 210, 223)




w1 = GameSprite('lol.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('lol.png', 370, 100, 50, 400)


barriars.add(w1)
barriars.add(w2)


packman = Player('sigma.jpeg', s, win_haight - 80, 80, 80, 0, 0)
final_sprite = GameSprite('ponpon.jpg', win_width - 85, win_height - 100, 80, 80)


monster1 = Enemy('moon.jpg', win_width - 80, 150, 80, 80, 5)
monster2 = Enemy('moon.jpg', win_width - 80, 150, 80, 80, 5)


monsters.add(monster1)
monsters.add(monster2)


finish = False
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                pakman.x_speed = -5
            elif e.key == K_RIGHT:
                pakman.x_speed = 5
            elif e.key == K_UP:
                pakman.x_speed = -5
            elif e.key == K_DOWN:
                pakman.x_speed = 5
            elif e.key == K_SPACE:
                packman.fire()


        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.speed = 0
            elif e.key == K_RIGHT:
                packman.speed = 0
            elif e.key == K_UP:
                packman.speed = 0
            elif e.key == K_DOWN:
                packman.speed = 0


    if not finish:

        windom.fill(back)


        packman.update()
        bullets.update()



        packman.reset()
        bullets.draw(windom)
        barriars.draw(windom)
        final_sprite.reset()


        sprite.groupcollide(monster, bullets, True, True)
        monster.update()
        sprite.groupcollide(bullets, barriars, True, False)


        if sprite.spritecollide(packman, mosters, False):
            finish = True
            img = image.load('galaxy_1.jpg')
            d = img.get_width() // img.get_height()
            windom.fill((255, 255, 255))
            windom.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))
        

        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = image.load('galaxy_1.jpg')
            windom.fill((255, 255, 255))
            windom.blit(transform.scale(img, (win_width, win_height)), (0, 0))
