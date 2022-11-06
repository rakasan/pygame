import pygame
import os

WIDTH, HEIGTH = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGTH))
WHITE = (255,255,255)
FPS = 60
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('first_game\Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('first_game\Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
pygame.display.set_caption("First PyGame")

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(300,100)) #draw a surface ontop the previous surface
    WIN.blit(RED_SPACESHIP,(700,100)) #draw a surface ontop the previous surface
    pygame.display.update() #update the display

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #get a list of all python events
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()



if __name__ == "__main__":
   main() #verification and check if this file is run directly and not throw an import