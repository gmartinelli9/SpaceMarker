import pygame
import winsound
from tkinter import simpledialog
import time

pygame.init()
tamanho = (1000,563)
branco = (255,255,255)
estrelas= {}
raiodocirculo = 10
tela =  pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
pygame.display.set_caption("SPACE MARKER")
space = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
pygame.display.set_icon(space)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            posicaomouse = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            estrelas[item] = posicaomouse
            if item == None:
                item = "Desconhecido"+str(posicaomouse)
            estrelas[item] = posicaomouse

    for item,posicao in estrelas.items():
        pygame.draw.circle(tela,branco,posicao,raiodocirculo)
        pygame.draw.line(tela,branco,list(estrelas.values())[0], posicao)
        fonte = pygame.font.Font(None,20)
        texto = fonte.render(item,True,(255,255,255)) 
        tela.blit(texto,(posicao[0]+10, posicao[1]+ 10))


    #TELA
    pygame.display.flip()
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    pygame.display.update()
    clock.tick(60)