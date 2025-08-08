import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,189,205),pygame.Rect(30,30,60,40))
    pygame.draw.circle(screen,(0,149,156),(350,30),49,9)
    pygame.draw.circle(screen,(0,130,116),(169,30),16)
    pygame.display.flip()