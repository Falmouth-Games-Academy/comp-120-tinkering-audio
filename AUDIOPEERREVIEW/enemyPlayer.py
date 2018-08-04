import pygame
import math
import random
pygame.init()


class Enemy():
    def __init__ (self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.speed = 4

        self.rect.x = 900
        self.rect.y = 400

    """Vectors enemy units on to the bottom right hand corner of the main player
       """

    def stalkPlayer(self, player):
        xdiff = (player.rect.x + player.rect.width/2) - self.rect.x + self.rect.width/2
        ydiff = (player.rect.y + player.rect.height/2) - self.rect.y + self.rect.height/2

        mag = math.sqrt(float(xdiff **2 + ydiff **2))
        numFrames = int(mag / self.speed)

        if numFrames !=0:
            movex = xdiff / numFrames
            movey = ydiff / numFrames
        else:
            return

        self.rect.x += movex
        self.rect.y += movey

        self.image.blit(self.image, self.rect)

    def update(self, player):
        self.stalkPlayer(player)






