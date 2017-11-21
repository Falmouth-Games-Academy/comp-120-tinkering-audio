from SoundEffectGeneration import *

pygame.init()

# Setting out the screen
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

play_sound()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
#       if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
