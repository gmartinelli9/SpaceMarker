import pygame
import winsound
from tkinter import simpledialog, messagebox
import time

pygame.init()
tamanho = (1000,563)
branco = (255,255,255)
fonte = pygame.font.SysFont("Georgia", 1)
estrelas= {}
marcacoes = []
raiodocirculo = 10
tela =  pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
pygame.display.set_caption("SPACE MARKER")
space = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
som = pygame.mixer.Sound("Space_Machine_Power.mp3")
som.play(-1)
pygame.display.set_icon(space)

def salvarmark():
    with open('Estrelas Marcadas.txt', 'w') as arquivo:
        for posicao, nome in marcacoes:
            arquivo.write(f"{posicao[0]}, {posicao[1]}, {nome}\n ")

def carregarmark():
    marcacoes.clear()
    try:
        with open('Estrelas Marcadas.txt', 'r') as arquivo:
            for linha in arquivo:
                x,y,nome = linha.strip().split(",")
                posicao = (int(x), int(y))
                marcacoes.append((posicao,nome))
    except FileNotFoundError:
        messagebox.showinfo("Erro", "As últimas marcações não foram encontradas")

def excluirmark():
    marcacoes.clear()

def escritanatela():
    opcoes = fonte.render("Opções:", True, branco)
    salvar = fonte.render("F10 - Para salvar as marcações", True, branco)
    carregar = fonte.render("F11 - Para carregar as últimas marcações", True, branco)
    excluir = fonte.render("F12 - Para excluir todas as marcações", True, branco)
    tela.blit (opcoes,(10,10))
    tela.blit (salvar,(10,40))
    tela.blit (carregar,(10,70))
    tela.blit (excluir,(10,100))

while True:
    escritanatela()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_F10:
                salvarmark
            elif event.key == pygame.K_F11:
                carregarmark
            elif event.key == pygame.K_F12:
                excluirmark


        if event.type == pygame.MOUSEBUTTONUP:
            posicaomouse = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            estrelas[item] = posicaomouse
            if item == "":
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
    tela.blit(fundo,(0,0))
    pygame.display.update()