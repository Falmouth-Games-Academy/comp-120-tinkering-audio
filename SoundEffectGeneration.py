import pygame
import random
import pygame.sndarray

pygame.init()
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# plays a sound between 1 and 5 times randomly
def play_sound():
    pygame.mixer.music.load('test.mp3')
    pygame.mixer.music.play(0,random.randrange(1,5))

play_sound()
done = False
while not done:




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
#        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
