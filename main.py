import pygame
from sys import exit
from random import randint


pygame.init()
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('screen-saver')
clock = pygame.time.Clock()
list =[]

class Block:
    def __init__(self,num):
        self.rect = pygame.Rect(0,0,50,50)
        self.x_mov = num
        self.y_mov = 4-num
        self.num = num
        self.particles = []
    def movement(self):
        self.rect.x +=self.x_mov
        self.rect.y +=self.y_mov

    def wall(self):
        if self.rect.left <= 0 or self.rect.right >=width:
            self.x_mov = -1*self.x_mov
        if self.rect.top <=0 or self.rect.bottom >=height:
            self.y_mov = -1*self.y_mov
    def particles_(self):
        x = randint(-5,5)
        y = randint(-5,5)
        print(x,y)
        rect = pygame.Rect(0,0, 40,40)
        rect.center = (self.rect.centerx + y ,self.rect.centery + x)
        self.particles.append(rect)
        for i in self.particles:
            i.width -=0.25
            i.height -=0.25
            pygame.draw.rect(screen,(49*self.num,51*self.num,50*self.num),i)
        self.particles = [rect for rect in self.particles if rect.width != 0 and rect.height != 0]

    def draw(self):
        pygame.draw.rect(screen,(49*self.num,51*self.num,50*self.num),self.rect)

    def update(self):
        self.movement()
        self.wall()
        self.particles_()
        self.draw()
    
for i in range(5):
    list.append(Block(i))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    screen.fill("green")
    for i in list:
        i.update()

    pygame.display.update()
    clock.tick(60)