import pygame
pygame.init()

largura=800
altura=600

screen = pygame.display.set_mode((largura, altura), 0, 0)

screen.fill((255,0,0))

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        print(event)
    pygame.display.update()


pygame.quit()
