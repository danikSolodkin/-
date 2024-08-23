#создай игру "Лабиринт"!
from pygame import *
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self,imagne_player,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(imagne_player),(65,65))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed  

class Enemy1(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x < 470:
            self.direction = 'right'
        if self.rect.x > 620:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.y < 70:
            self.direction = 'up'
        if self.rect.y > 220:
            self.direction = 'down'

        if self.direction == 'up':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_wight,wall_height):
        super().__init__()
        self.image = Surface((wall_wight,wall_height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        walls.add(self)
    def draw(self):
        mw.blit(self.image,self.rect) 


#создай окно игры
mw = display.set_mode((700,500))
display.set_caption('maze')

bg = transform.scale(image.load('background.jpg'),(800,600))


mixer.music.load('jungles.ogg')
mixer.music.play(-1)     
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN',True,(0,255,0))
lose = font.render('YOU Lose',True,(255,0,0))


player = Player('hero.png',5,420,4)
vrag1 = Enemy1('cyborg.png',605,320,4)
vrag2 = Enemy2('cyborg.png',305,220,4)
chest = GameSprite('treasure.png',605,440,4)
walls = sprite.Group()


w1 = Wall(200,100,100,100,40,580,10)
w2 = Wall(200,100,100,100,40,10,330)
w3 = Wall(200,100,100,100,480,200,10)
w4 = Wall(200,100,100,300,180,10,310)
w5 = Wall(200,100,100,300,180,280,10)
w6 = Wall(200,100,100,580,180,10,300)
#задай фон сцены
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        mw.blit(bg,(0,0))
        player.reset()
        player.update()
        vrag1.reset()
        vrag2.reset()
        chest.reset()
        
         
        vrag1.update()
        vrag2.update()
        walls.draw(mw)
        if sprite.collide_rect(player, chest):
            mw.blit(win,(200,200))
            money.play()
            finish  = True
        if sprite.spritecollide(player, walls, False) or sprite.collide_rect(player, vrag1) or sprite.collide_rect(player, vrag2):
            mw.blit(lose,(200,200))
            kick.play()
            finish  = True


    display.update()
    time.Clock().tick(100)