import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('side_scroller/images','bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join('side_scroller/images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('side_scroller/images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('side_scroller/images', 'S1.png')),pygame.image.load(os.path.join('side_scroller/images', 'S2.png')),pygame.image.load(os.path.join('side_scroller/images', 'S2.png')),pygame.image.load(os.path.join('side_scroller/images', 'S2.png')), pygame.image.load(os.path.join('side_scroller/images', 'S2.png')),pygame.image.load(os.path.join('side_scroller/images', 'S2.png')), pygame.image.load(os.path.join('side_scroller/images', 'S2.png')), pygame.image.load(os.path.join('side_scroller/images', 'S2.png')), pygame.image.load(os.path.join('side_scroller/images', 'S3.png')), pygame.image.load(os.path.join('side_scroller/images', 'S4.png')), pygame.image.load(os.path.join('side_scroller/images', 'S5.png'))]
    fall = pygame.image.load(os.path.join('side_scroller/images', '0.png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
        self.falling = False

    def draw(self, win):
        if self.falling:
            win.blit(self.fall,(self.x,self.y + 30))
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4,self.y,self.width - 24,self.height - 10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x,self.y + 3,self.width - 8,self.height - 35)
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
                self.hitbox = (self.x + 4,self.y,self.width - 24,self.height - 10)
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4,self.y,self.width - 24, self.height-10)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)


def redrawWindow():
    win.blit(bg,(bgX,0))
    win.blit(bg,(bgX2,0))
    runner.draw(win)
    for objectt  in objects:
        objectt.draw(win)
    pygame.display.update()

def endScreen():
    global pause,objects,speed
    pause = 0
    objects = []
    speed = 0
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        win.blit(bg,(0,0))
        large_font = pygame.font.SysFont('commicsans',80)
        previous_score = large_font.render('Previous score',1,(255,255,255))
        win.blit(previous_score,(W/2 - previous_score.get_width()/2),200)
        new_score = large_font.render('Previous score',1,(255,255,255))
        win.blit(new_score,(W/2 - new_score.get_width()/2),320)

class saw(object):
    img = [pygame.image.load(os.path.join('side_scroller/images', 'SAW0.png')),pygame.image.load(os.path.join('side_scroller/images', 'SAW1.png')),pygame.image.load(os.path.join('side_scroller/images', 'SAW2.png')),pygame.image.load(os.path.join('side_scroller/images', 'SAW3.png'))]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = height
        self.hitbox = (x,y,width,height)
        self.count = 0

    def draw(self, win):
        self.hitbox  = (self.x + 5,self.y + 5,self.width -10, self.heigh)
        if self.count >= 8:
            self.count = 0
        win.blit(pygame.transform.scale(self.img[self.count//2],(64,64)),(self.x,self.y) )
        self.count +=1
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    
    def collide(self,rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1] : 
                return True
        return False

class spike(saw):
    img = pygame.image.load(os.path.join('side_scroller/images', 'spike.png'))
    def draw(self, win):
        self.hitbox = (self.x + 10,self.y,28,315)
        win.blit(self.img,(self.x,self.y))
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    
    def collide(self,rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[1] : 
                return True
        return False


runner = player(200,313,64,64)
pygame.time.set_timer(USEREVENT+1,500)
pygame.time.set_timer(USEREVENT+2,random.randrange(3000,5000))
speed = 30
pause = 0
fallSpeed = 0
objects = []
run = True
while run:
    if pause >0:
        pause +=1
        if pause > fallSpeed * 2:
            endScreen()

    for objectt in objects:
        if objectt.collide(runner.hitbox):
            runner.falling = True
            if pause == 0:
                fallSpeed = speed
                pause =1
        objectt.x -= 1.4
        if objectt.x < objectt.width * -1:
            objects.pop(objects.index(objectt))
    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT+1:
            speed+=1
        if event.type == pygame.USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0:
                objects.append(saw(810,310,64,64))
            else :
                objects.append(spike(810,310,48,320))

        
    keys = pygame.key.get_pressed()

    if(keys[pygame.K_SPACE] or keys[pygame.K_UP]):
        if not (runner.jumping):
            runner.jumping  = True
    if keys[pygame.K_DOWN]:
        if not (runner.sliding):
            runner.sliding = True
    clock.tick(speed)
    redrawWindow()
    