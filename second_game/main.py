import pygame


FPS = 60
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
WIDTH,HEIGHT = 800,600



win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Just a brick breaker")

class Paddle:
    VEL = 5

    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

    def move(self,direction = 1):
        self.x = self.x + (self.VEL * direction)

class Ball:
    VEL = 5

    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -self.VEL

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self,x_vel,y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel
    def draw(self, win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

def draw(win,paddle,ball):
    win.fill("white")
    ball.draw(win)
    paddle.draw(win)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    center_x = WIDTH/2  -PADDLE_WIDTH/2
    paddle_y = HEIGHT - PADDLE_HEIGHT - 5
    paddle = Paddle(center_x,paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT,"black" )
    ball = Ball(center_x - BALL_RADIUS,paddle_y- BALL_RADIUS,BALL_RADIUS,"black")
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.x  - paddle.VEL >= 0:
            paddle.move(-1)
        if keys[pygame.K_RIGHT] and paddle.x +paddle.VEL < (WIDTH - paddle.width) :
            paddle.move(1)
        
        ball.move()
        draw(win,paddle,ball)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()