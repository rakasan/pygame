import pygame
import os

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


WIDTH, HEIGTH = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGTH))
WHITE = (255,255,255)
BLACK = (0,0,0)
BORDER = pygame.Rect((WIDTH - 10)/2,0,10,HEIGTH)
BULLET_VEL = 7

FPS = 60
VEL = 5
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
MAX_BULLETS = 3

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('first_game\Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('first_game\Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
pygame.display.set_caption("First PyGame")

def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #draw a surface ontop the previous surface
    WIN.blit(RED_SPACESHIP,(red.x,red.y)) #draw a surface ontop the previous surface
    pygame.display.update() #update the display

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+= BULLET_VEL
        if yellow.colliderect(bullet):
            yellow_bullets.remove(bullet)

def yellow_handle_movement(keys_pressed,yellow):
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
            yellow.x -=VEL
        if keys_pressed[pygame.K_d] and yellow.x + yellow.width + VEL < BORDER.x: #right
            yellow.x +=VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL  > 0: #down
            yellow.y -=VEL
        if keys_pressed[pygame.K_s]and yellow.y + VEL + yellow.height < HEIGTH - 15: #up
            yellow.y +=VEL

def red_handle_movement(keys_pressed,red):
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
            red.x -=VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < WIDTH: #right
            red.x +=VEL
        if keys_pressed[pygame.K_UP]and red.y - VEL > 0: #down
            red.y -=VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGTH - 15: #up
            red.y +=VEL

def main():

    red_bullets = []
    yellow_bullets = []

    red =pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow =pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #get a list of all python events
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height / 2 - 2,10,5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y + red.height / 2 - 2,10,5)
                    red_bullets.append(bullet)

        print(red_bullets,yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)

        handle_bullets(yellow_bullets,red_bullets,yellow,red)


        draw_window(red,yellow)

    pygame.quit()



if __name__ == "__main__":
   main() #verification and check if this file is run directly and not throw an import