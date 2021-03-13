import pygame
import sys
import math

pygame.init()

w,h = 720,400

#colors

white = [255,255,255]
black = [0,0,0]
red= [255,0,0]
green = [0,255,0]
blue = [0,0,255]

#screen
screen = pygame.display.set_mode((w,h))




class pendulum:

    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def make(self,_):
        pygame.draw.circle(_,red,(self.x,self.y),self.r)
        pygame.draw.line(_,green,(self.x,self.y-self.r),(w//2,0),5)

def get_ang():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Angle : '+str(round(math.degrees(theta))), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (100,20 )
    return text,textRect
#physics
run = False
l = 0
a=0
v=0
theta=0
ball = pendulum(w//2,300,10)

def get_anglength():
    l = math.sqrt((ball.x-w/2)**2 + (ball.y**2))
    theta= math.asin((ball.x-w/2)/l) #for some reason if we use acos to calculate the angle it only appears on the right side.
    return l,theta

def grid():
    for x in range(50, w, 50):
        pygame.draw.lines(screen, white, False, [[x, 0], [x, h]])
        for y in range(50, h, 50):
            pygame.draw.lines(screen, white, False, [[0, y], [w, y]])

def redisplay():
    screen.fill([60, 25, 60])
    text, textRect = get_ang()
    screen.blit(text, textRect)
    grid()
    ball.make(screen)
    pygame.display.update()

clock = pygame.time.Clock()
while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:

            c,d=pygame.mouse.get_pos()
            ball=pendulum(c,d,15)
            l,theta = get_anglength()


            run =True

    if run==True:
        a=-0.001*math.sin(theta)
        v+=a
        v*=0.99999 # damping factor
        theta+=v
        ball.x=(w/2+(l*math.sin(theta)))
        ball.y=(l*math.cos(theta))

    redisplay()

