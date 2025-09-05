import pygame
import random
sw,sh=500,400
ms=5
fs=72
pygame.init()
back_img=pygame.transform.scale(pygame.image.load("galaxy.jpg"),(sw,sh))
f=pygame.font.SysFont("Times New Roman",fs)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color('blue'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(
            min(self.rect.x+x_change,sw-self.rect.width,0)
        )
        self.rect.y=max(
            min(self.rect.y+y_change,sw-self.rect.width,0)
        )
screen=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("sprite collision")
all_sprites=pygame.sprite.Group()
sprite1=Sprite(pygame.Color("red"),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0,sw-sprite1.rect.width),random.randint(
        0,sh-sprite1.rect.height)
all_sprites.add(sprite1)
sprite2=Sprite(pygame.Color('black'),20,30)
sprite2.rect.x,sprite1.rect.y=random.randint(
    0,sw-sprite1.rect.width),random.randint(
        0,sh-sprite2.rect.height)
all_sprites.add(sprite2)
running,won=True,False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or(event.type==pygame.KEYDOWN
                                      and event.key==pygame.K_x):
            running=False
        if not won:
            keys=pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * ms
            y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * ms
            sprite1.move(x_change,y_change)
            sprite1.move(x_change,y_change)
            if sprite1.rect.colliderect(sprite2.rect):
                all_sprites.remove(sprite2)
                won=True
        screen.blit(back_img,(0,0))
        all_sprites.draw(screen)
        if won:
            wt=f.render("you win!",True,pygame.Color('black'))
            screen.blit(wt,((sw-wt.get_width())//2,(sh-wt.get_height())//2))
        pygame.display.flip()
        clock.tick(90)
pygame.quit()

