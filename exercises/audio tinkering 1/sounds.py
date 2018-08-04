#import pygame
import pygame
pygame.init()
pygame.mixer.init()
#set window dimensions and caption
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jungle run")

#load music, show file path
music = "C:\sprites\jungle-run-01."
#load pygame mixer
pygame.mixer.music.load("C:\sprites\jungle-run-01.MP3")
pygame.mixer.music.play(-1,0.0)#make this is a key press


done = False

while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()

    #activeKey = pygame.key.get_pressed()

    #if activeKey[pygame.K_s]:
        #pygame.mixer.music.stop()
    #if activeKey[pygame.K_p]:
        #pygame.mixer.play()


pygame.display.update
pygame.quit()
