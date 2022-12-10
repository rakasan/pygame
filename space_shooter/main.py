import pygame
import os

pygame.font.init()
pygame.mixer.init()

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


WIDTH, HEIGTH = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGTH))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)


HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

BORDER = pygame.Rect((WIDTH - 10)//2,0,10,HEIGTH)
BULLET_VEL = 7

FPS = 60
VEL = 5
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
MAX_BULLETS = 3


BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('first_game\Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('first_game\Assets','Gun+Silencer.mp3'))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('first_game\Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('first_game\Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

SPACE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('first_game\Assets','space.png')), (WIDTH,HEIGTH))
pygame.display.set_caption("First PyGame")

def draw_winner(text):
    draw_text =  WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH//2 - draw_text.get_width()//2,HEIGTH//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(1000)

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    # WIN.fill(WHITE)
    WIN.blit(SPACE_IMG,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    red_health_text = HEALTH_FONT.render("Health: "+ str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: "+ str(yellow_health),1,WHITE)
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10,10))
    WIN.blit(yellow_health_text,(10,10))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #draw a surface ontop the previous surface
    WIN.blit(RED_SPACESHIP,(red.x,red.y)) #draw a surface ontop the previous surface



    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)


    pygame.display.update() #update the display

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

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

    red_health = 2
    yellow_health = 2

    red =pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow =pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #get a list of all python events
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height // 2 - 2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y + red.height // 2 - 2,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                
            if event.type == RED_HIT:
                red_health-=1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health-=1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins"
        if yellow_health <=0:
            winner_text = "Red wins"   

        if winner_text != "":
            draw_winner(winner_text)   
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)

        handle_bullets(yellow_bullets,red_bullets,yellow,red)


        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)

    main()
   # pygame.quit()



if __name__ == "__main__":
   main() #verification and check if this file is run directly and not throw an import