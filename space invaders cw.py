import math
import random
import pygame
screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x_=4
enemy_speed_y_=40
bullet_speed_y=10
collision_distance=27
pygame.init()    #initialistion of pygame
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load("background space.jpeg")
pygame.display.set_caption("space invader")
icon=pygame.image.load("ufo.jpg")
pygame.display.set_icon(icon)
playerImg=pygame.image.load("rocket.png")
playerX=player_start_x
playerY=player_start_y
playerx_change=0
enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load)
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x_)
    enemyy_change.append(enemy_speed_y_)
bulletImage=pygame.image.load("bullet-removebg-preview.png")
bulletX=0
bulletY=player_start_y
bullet_X_change=0
bullet_y_change=bullet_speed_y
bullet_state="ready"
score_value=0
font=pygame.font.SysFont("Times New Roman",32)
textx=10
texty=10
overfont=pygame.font.SysFont("Times New Roman",50)
def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(225,225,225))
    screen.blit(score(x,y))
def game_over_text():
    over_text=overfont.render("GAME OVER"),True,(225,225,225)
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
     global bullet_state
     bullet_state="fire"
     screen.blit(bulletImage,(x+16,y+10))
def isCollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance<collision_distance
running=True
while running:
    screen.fill((0,125,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get:
        if event.type==pygame.QUIT:
            running=False
        if event.pygame==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
            if event.type==pygame.KEYUP and event.key in[pygame.K_LEFT,pygame.K_RIGHT]:
                playerx_change=0
            playerX+=playerx_change
            playerX=max(0,min(playerX,screen_width-64))
            for i in range(num_of_enemies):
                if enemyy[i]>340:
                    for j in range(num_of_enemies):
                        enemyy[j]=2000
                    game_over_text
                    break
                enemyx[i]+=enemyx_change[i]
                if enemyx[i]<=0 or enemyx[i]>=screen_width-64:
                    enemyx_change[i] *=-1
                    enemyy_change[i] +=enemyy_change[i]
                if isCollision(enemyx[i],enemy[i],bulletX,bulletY):
                    bulletY=player_start_y
                    bullet_state="ready"
                    score_value +=1
                    enemyx[i]=random.randint(0,screen_width-64)
                    enemyy[i]=random.randint(enemy_start_y_min,enemy_start_y_max)
                enemy(enemyx[i],enemyy[i])
                if bulletY<=0:
                    bulletY=player_start_y
                    bullet_state="ready"
                elif bullet_state=="fire":
                    fire_bullet(bulletX,bulletY)
                    bulletY-=bullet_y_change
                player(playerX,playerY)
                show_score(textx,texty)
                pygame.display.update()