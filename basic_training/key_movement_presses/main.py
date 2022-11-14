import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first tutorial")

x = 50
y = 50

width = 40
height = 60
vel = 5

run  = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -=1    
    if keys[pygame.K_RIGHT]:    
        x+=1
    if keys[pygame.K_UP]: 
        y-=1   
    if keys[pygame.K_DOWN]:  
        y+=1  

    win.fill("black")    
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()