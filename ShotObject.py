import pygame
import random
import math

pygame.init()

#display size
display_width = 1000
display_height = 600
FPS = 30

#calls a surface (window) called gameDisplay where I will run the game

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BOX ATTACK')
clock = pygame.time.Clock()
pygame.mixer.music.load("C:\Sound effects\destrukt.wav")
pygame.mixer.music.play(-1,0.0)
#Variables/lists

charList = " *  _  * ".split()
charList1 = ['S', 'H', 'O', 'O', 'T']
bullets = []

effect = pygame.mixer.Sound("Flash-laser-10.wav")


def getFont(name = "courier new", size = 30, style = ''):
    return pygame.font.SysFont(name, size, style)

class Bullet:
    movex = 1
    movey = 1

    def __init__(self):
        self.image = getFont(size=10, style='bold').render(random.choice(charList), True, (255,255,255))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(5, 76)
        self.rect.y = random.randint(5, 76)

        self.movex = random.choice([-1, 1])
        self.movey = random.choice([-1, 1])
        self.speed = 20.0


    def target(self):
        cur = pygame.mouse.get_pos()

        xdiff = cur[0] - self.rect.x
        ydiff = cur[1] - self.rect.y

        mag = math.sqrt(float(xdiff **2 + ydiff ** 2))
        numFrames = mag / self.speed


        self.movex = xdiff / numFrames
        self.movey = ydiff / numFrames

    def travel(self):
        self.rect.x += self.movex
        self.rect.y += self.movey


class mainPlayer:
    def __init__(self):
        self.image = pygame.Surface((100,100))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 45

        self.speed = 9

        self.ammo = []
        self.coolDown = 0
        self.coolDownMax = 10


    def move(self, xdir, ydir):
        self.rect.x += xdir*self.speed
        self.rect.y += ydir*self.speed

    def spawnAmmo(self):
        self.ammo.append(Bullet())

    def moveAmmo(self):
        self.image.fill((0,0,255))

        for object in self.ammo:
            if object.rect.x + object.rect.width >= self.rect.width:
                object.movex *= -1
            elif object.rect.y + object.rect.width >= self.rect.width:
                object.movey *= -1
            if object.rect.x <= 0:
                object.movex *= -1
            elif object.rect.y <= 0:
                object.movey *= -1

            object.rect.x += object.movex
            object.rect.y += object.movey

            self.image.blit(object.image, object.rect)


    def Shoot(self):
        if self.coolDown <= 0 and self.ammo:
            self.coolDown = self.coolDownMax
            bullet = self.ammo.pop()

            bullet.rect.x = self.rect.x + self.rect.width/2 - bullet.rect.width/2
            bullet.rect.y = self.rect.y + self.rect.height/2 - bullet.rect.height/2

            bullet.target()
            bullets.append(bullet)


    def update(self):
        self.coolDown -= 1

player = mainPlayer()


spawnDelay = 0
spawnDelayMax = 20
#game loop
done = False

while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

    activeKey = pygame.key.get_pressed()

    if activeKey[pygame.K_d]:
        player.move(1,0)
    if activeKey[pygame.K_a]:
        player.move(-1,0)
    if activeKey[pygame.K_w]:
        player.move(0,-1)
    if activeKey[pygame.K_s]:
        player.move(0,1)

    #updates
    player.update()
    gameDisplay.fill((0,0,0))

    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        player.Shoot()
        #pygame.mixer.sound.load("C:\Sound effects\Flash-laser-10.wav")
        #pygame.mixer.Sound.play("C:\Sound effects\Flash-laser-10.wav")
        effect.play(0,0,0)

    spawnDelay -= 1
    if spawnDelay <= 0:
        player.spawnAmmo()
        spawnDelay = spawnDelayMax

    player.moveAmmo()
    for object in bullets:
        object.travel()
        gameDisplay.blit(object.image, object.rect)

#alterative box draw method
       #if event.type == pygame.KEYDOWN:
           #if event.key == pygame.K_RIGHT:
              # player.rect.x += 30


    #gameDisplay.fill((0, 0, 0))

#draw stuff

    gameDisplay.blit(player.image, player.rect)

#end stuff
    pygame.display.update()
    clock.tick(FPS)
#finish
    #gameDisplay.fill((0,0,0))
    #pygame.display.update()

pygame.quit()
quit()
