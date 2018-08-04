import pygame

screen = pygame.display.set_mode((800, 600))


def DupImage(image_path):
    image = pygame.image.load(image_path)
    Dup1 = image.copy()
    Dup2 = image.copy()

    height = image.get_height()
    width = image.get_width()

    screen.blit(image, (0, 0))

    screen.blit(Dup1, (0 + width, 0))

    screen.blit(Dup1, (0 + width*2, 0))


DupImage("smallimage.jpg")

def color_fill

pygame.display.flip()


done = False

while not done:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         done = True

         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
             done = True


