import pygame
import random
import pygame.sndarray


# picks a random number and then plays the sound tied to that number
def play_sound():
    pick_a_number = random.randrange(0, 6)
    if pick_a_number == 1:
        pygame.mixer.music.load('test.mp3')
        pygame.mixer.music.play(0, 0)
    if pick_a_number == 2:
        pygame.mixer.music.load('idiots.mp3')
        pygame.mixer.music.play(0, 0)
    if pick_a_number == 3:
        pygame.mixer.music.load('test.mp3')
        pygame.mixer.music.play(0, 0)
    if pick_a_number == 4:
        pygame.mixer.music.load('no.mp3')
        pygame.mixer.music.play(0, 0)
    if pick_a_number == 5:
        pygame.mixer.music.load('no.mp3')
        pygame.mixer.music.play(0, 0)
