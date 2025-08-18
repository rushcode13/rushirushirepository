import pygame
pygame.init()
sw,sh=500,500
ds=pygame.display.set_mode((sw,sh))
pygame.display.set_caption('Rushikas game screen')
background_image=pygame.transform.scale(pygame.image.load("snow.jpg").convert(),(sw,sh))
my_image=pygame.transform.scale(pygame.image.load("girl_in_snow-removebg-preview.png").convert(),(200,200))
def game_loop():
    clock = pygame.time.Clock()
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
        ds.blit(background_image,(0,0))
        ds.blit(my_image,(200,200))
        pygame.display.flip()
        pygame.time.wait(50)
    pygame.quit
if __name__=="__main__":
    game_loop()