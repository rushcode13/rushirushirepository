import pygame
pygame.init()
sw, sh = 500, 500
ds = pygame.display.set_mode((sw, sh))
pygame.display.set_caption('Indipendence day salute')
background_image = pygame.transform.scale(pygame.image.load("sun rise .jpg").convert(), (sw, sh))
my_image = pygame.transform.scale(pygame.image.load("salute.jpg").convert(), (200, 200))
def game_loop():
    clock = pygame.time.Clock()
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
        ds.blit(background_image, (0, 0))
        ds.blit(my_image, (200, 200))
        pygame.draw.circle(ds, (0, 0, 128), (105, 160), 9)  # chakra
        pygame.draw.rect(ds, (244, 196, 48), pygame.Rect(40,160, 124, 22))  # orange
        pygame.draw.rect(ds, (255, 255, 255), pygame.Rect(40,180, 124, 22))  # white
        pygame.draw.rect(ds, (76, 175, 80), pygame.Rect(40,200,124,22))  # green
        pygame.draw.rect(ds, (0, 0, 0), pygame.Rect(40,160,2,250))# flag pole
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    game_loop()







