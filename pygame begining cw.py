import pygame
pygame.init()
sw,sh=500,500
ds=pygame.display.set_mode((sw,sh))
pygame.display.set_caption('rushika is a very NOT naughty girl')
background_image=pygame.transform.scale(pygame.image.load("backdrop.jpg").convert(),(sw,sh))
my_image=pygame.transform.scale(pygame.image.load("cute-kid.jpg").convert(),(200,200))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ds.blit(background_image,(0,0))
        ds.blit(my_image,(50,50))
        pygame.display.flip()
        pygame.time.wait(50)
    pygame.quit
if __name__=="__main__":
    game_loop
