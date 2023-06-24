import pygame
import winsound
from tkinter import simpledialog
import time

pygame.init()
tamanho = (1000,563)
branco = (255,255,255)
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
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            if item == None:
                item = "Desconhecido"+str(pos)
            estrelas[item] = pos
    


    #TELA
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    pygame.display.update()
    clock.tick(60)