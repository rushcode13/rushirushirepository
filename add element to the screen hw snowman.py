import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(225,102,0),pygame.Rect(180,83,40,8))
    ##########################color#######position#radius#border#if no border,filled.
    pygame.draw.circle(screen,(225,225,225),(217,60),8)#eye
    pygame.draw.circle(screen,(225,225,225),(183,60),8)#eye
    pygame.draw.circle(screen,(225,225,225),(199,69),45,4)#top
    pygame.draw.circle(screen,(225,225,225),(199,183),75,4)#middle
    pygame.draw.circle(screen,(225,225,225),(199,355),105,4)#bottom
    pygame.display.flip()