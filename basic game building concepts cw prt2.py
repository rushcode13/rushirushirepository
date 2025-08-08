import pygame
def main():
    pygame.init()
    sw,sh=(500,500)
    screen=pygame.display.set_mode((sw,sh))
    colors={"red":pygame.Color("red"),
            "blue":pygame.Color("blue"),
            "green":pygame.Color("green"),
            "yellow":pygame.Color("yellow"),
            "white":pygame.Color("white"),
           }
    current_color=colors["white"]
    x,y=30,30
    spw,sph=60,60
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():  #to get the event and to capture the movement(ex.if any buttons are pressed)
            if event.type==pygame.quit:#if the user presses the 'X' button then,clase the program and screen
                done=True
        pressed=pygame.key.get_pressed()#whichever key pressed it recognisind it.
        if pressed[pygame.K_LEFT]:x -=3
        if pressed[pygame.K_LEFT]:x +=3
        if pressed[pygame.K_LEFT]:y -=3
        if pressed[pygame.K_LEFT]:y +=3
        x=min(max(0,x),sw-spw)
        y=min(max(0,y),sh-sph)
        if x==0: current_color=colors['blue']
        elif x==sw-sw: current_color=colors['yellow']
        elif y==0: current_color=colors['red']
        elif y==sh-sw:
            current_color=colors['green']
        else:
            current_color=colors['white']
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color,(x,y,spw,sph))
        pygame.display.flip()        
        clock.tick(90)
    pygame.quit()
if __name__=="__main__":
    main()