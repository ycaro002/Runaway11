import pygame
from pygame import KEYDOWN, KEYUP
from pygame import QUIT,K_DOWN,K_UP,K_RIGHT,K_LEFT,K_RETURN,K_ESCAPE,K_a,K_s,K_d,K_w
import sys
pygame.init()

pygame.mixer.init()

largura=800
altura=600
resolucao = largura,altura



fixo= True
selecionar= True

screen= pygame.display.set_mode((resolucao), 0, 32)
screen_menu= pygame.Surface((resolucao), 0, 32)
menu = pygame.image.load('backgrounds/kappa.png')
menu = pygame.transform.scale(menu,(resolucao))
background = pygame.image.load('backgrounds/qq.jpg')
background = pygame.transform.scale(background,(resolucao))

def exibir_imagem(imagem, superficie, posicao):
    superficie.blit(imagem,(posicao))

pygame.display.set_caption('Runaway')

def txt2string(file_dialogo):
    arquivo = open(file_dialogo,'r')
    list_a = []
    for linha in arquivo:
        list_a.append(linha)
        print(linha)
    return list_a[0]
def jogo():
    screen_menu.fill((255,255,255))
    screen_menu.blit(screen,(0,0))
    screen.blit(background,(0,0))
    arq = 'dialogo.txt'
    x = txt2string(arq)
    fonte = pygame.font.SysFont('Agency FB', 30,False,False)
    iniciar= fonte.render(x, True,(255,0,0))
    screen_menu.blit(iniciar, ((largura/2) - 30, (altura/2) + 130))


def selecionar():
    global menu_selecao

    if (menu_selecao == 1):
        screen_menu.fill((255,255,255))
        exibir_imagem(menu,screen_menu,(0,0))
        fonte = pygame.font.SysFont('Agency FB', 30,False,False)
        iniciar= fonte.render('Play', True,(255,0,0))
        screen_menu.blit(iniciar, ((largura/2) - 30, (altura/2) + 130))
        fonte= pygame.font.SysFont('Agency FB', 20,False,False)
        configuracoes= fonte.render('Configurações', True,(255,255,255))
        screen_menu.blit(configuracoes, ((largura/2) - 30, (altura/2) + 165))
        fonte = pygame.font.SysFont('Agency FB', 20,False,False)
        creditos= fonte.render('Créditos', True,(255,255,255))
        screen_menu.blit(creditos, ((largura/2) - 30, (altura/2) + 200))
        fonte= pygame.font.SysFont('Agency FB', 20,False,False)
        sair= fonte.render('Sair', True,(255,255,255))
        screen_menu.blit(sair, ((largura/2) - 30, (altura/2) + 235))

    if (menu_selecao== 2) :
        screen_menu.fill((255,255,255))
        exibir_imagem(menu,screen_menu,(0,0))
        fonte = pygame.font.SysFont('Agency FB', 20,False,False)
        iniciar= fonte.render('Play', True,(255,255,255))
        screen_menu.blit(iniciar, ((largura/2) - 30, (altura/2) + 130))
        fonte= pygame.font.SysFont('Agency FB', 30,False,False)
        configuracoes= fonte.render('Configurações', True,(255,0,0))
        screen_menu.blit(configuracoes, ((largura/2) - 30, (altura/2) + 165))
        fonte = pygame.font.SysFont('Agency FB', 20,False,False)
        creditos= fonte.render('Créditos', True,(255,255,255))
        screen_menu.blit(creditos, ((largura/2) - 30, (altura/2) + 200))
        fonte= pygame.font.SysFont('Agency FB', 20,False,False)
        sair= fonte.render('Sair', True,(255,255,255))
        screen_menu.blit(sair, ((largura/2) - 30, (altura/2) + 235))

    if (menu_selecao == 3):        
        screen_menu.fill((255,255,255))
        exibir_imagem(menu,screen_menu,(0,0))
        fonte = pygame.font.SysFont('Agency FB', 20,False,False)
        iniciar= fonte.render('Play', True,(255,255,255))
        screen_menu.blit(iniciar, ((largura/2) - 30, (altura/2) +130))

        fonte= pygame.font.SysFont('Agency FB', 20,False,False)
        configuracoes= fonte.render('Configurações', True,(255,255,255))
        screen_menu.blit(configuracoes, ((largura/2) - 30, (altura/2) + 165))
        fonte = pygame.font.SysFont('Agency FB', 30,False,False)
        creditos= fonte.render('Créditos', True,(255,0,0))
        screen_menu.blit(creditos, ((largura/2) - 30, (altura/2) + 200))
        fonte= pygame.font.SysFont('Agency FB', 20,False,False)
        sair= fonte.render('Sair', True,(255,255,255))
        screen_menu.blit(sair, ((largura/2) - 30, (altura/2) + 235))

    if (menu_selecao == 4) :
        screen_menu.fill((255,255,255))
        exibir_imagem(menu,screen_menu,(0,0))
        fonte = pygame.font.SysFont('Agency FB', 20,False,False)
        iniciar= fonte.render('Play', True,(255,255,255))
        screen_menu.blit(iniciar, ((largura/2) - 30, (altura/2) + 130))

        fonte= pygame.font.SysFont('Agency FB', 20,False,False)
        configuracoes= fonte.render('Configurações', True,(255,255,255))
        screen_menu.blit(configuracoes, ((largura/2) - 30 , (altura/2) + 165))
        fonte = pygame.font.SysFont('Agency FB', 20,False,False)
        creditos= fonte.render('Créditos', True,(255,255,255))
        screen_menu.blit(creditos, ((largura/2) - 30, (altura/2) + 200))
        fonte= pygame.font.SysFont('Agency FB', 30,False,False)
        sair= fonte.render('Sair', True,(255,0,0))
        screen_menu.blit(sair, ((largura/2) - 30, (altura/2) + 235))
    if (menu_selecao == 11):
        jogo()
    if menu_selecao == 5:
         menu_selecao = 4
    if menu_selecao <= 0:
        menu_selecao = 1
    if menu_selecao == 6:
        menu_selecao = 1
    if menu_selecao == 96:
        menu_selecao = 1
    if menu_selecao == 95: 
        menu_selecao = 1
    if menu_selecao == 94:
        menu_selecao = 1
    if menu_selecao == 93:
        menu_selecao = 1
    if menu_selecao == 92:
        menu_selecao = 1
    if menu_selecao == 91:
        menu_selecao = 1
menu_selecao = 1    


    

while(True):
    selecionar()
    screen.blit(screen_menu, (0,0))
    pygame.display.update()
    pygame.display.flip()
    for e in pygame.event.get():
        if (e.type == QUIT):
            pygame.quit()
        if (e.type == KEYDOWN):
            if (e.key == K_DOWN):
                menu_selecao = menu_selecao + 1
            if (e.key == K_UP):
                menu_selecao = menu_selecao - 1
            if (e.key == K_RETURN):
                menu_selecao = menu_selecao + 10
            if (e.key == K_ESCAPE):
                menu_selecao = menu_selecao - 10
        if menu_selecao == 11:
            jogo()
    print(menu_selecao)                
    

 


while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        print(event)
    pygame.display.update()

pygame.quit()
quit()

