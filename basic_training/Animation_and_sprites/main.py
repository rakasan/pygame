import pygame

pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Sprites test")

walkRight = [pygame.image.load('basic_training/Animation_and_sprites/R1.png'), pygame.image.load('basic_training/Animation_and_sprites/R2.png'), pygame.image.load('basic_training/Animation_and_sprites/R3.png'), pygame.image.load('basic_training/Animation_and_sprites/R4.png'), pygame.image.load('basic_training/Animation_and_sprites/R5.png'), pygame.image.load('basic_training/Animation_and_sprites/R6.png'), pygame.image.load('basic_training/Animation_and_sprites/R7.png'), pygame.image.load('basic_training/Animation_and_sprites/R8.png'), pygame.image.load('basic_training/Animation_and_sprites/R9.png')]
walkLeft = [pygame.image.load('basic_training/Animation_and_sprites/L1.png'), pygame.image.load('basic_training/Animation_and_sprites/L2.png'), pygame.image.load('basic_training/Animation_and_sprites/L3.png'), pygame.image.load('basic_training/Animation_and_sprites/L4.png'), pygame.image.load('basic_training/Animation_and_sprites/L5.png'), pygame.image.load('basic_training/Animation_and_sprites/L6.png'), pygame.image.load('basic_training/Animation_and_sprites/L7.png'), pygame.image.load('basic_training/Animation_and_sprites/L8.png'), pygame.image.load('basic_training/Animation_and_sprites/L9.png')]
bg = pygame.image.load('basic_training/Animation_and_sprites/bg.jpg')
char = pygame.image.load('basic_training/Animation_and_sprites/standing.png')

clock = pygame.time.Clock()
FPS = 27
x = 50
y = 400

width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))   
    if walkCount  + 1 >= 27 : 
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount+=1
    else:
        win.blit(char,(x,y))
   # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

run  = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >=vel:
        x -=vel
        left = True
        right = False   
    elif keys[pygame.K_RIGHT] and x < 500 - width:    
        x+=vel
        right = True
        left = False
    else:
        right = False
        left  =False
        walkCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left  = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -=(jumpCount ** 2) * 0.5 * neg
            jumpCount -=1
        else:
            isJump = False
            jumpCount = 10
    redrawGameWindow()

pygame.quit()