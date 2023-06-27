import pygame
import winsound
from tkinter import simpledialog, messagebox, Tk
import pickle

pygame.init()
tamanho = (1000,563)
branco = (255,255,255)
raiodocirculo = 10
marcacoes = {}
fonte = pygame.font.SysFont("Georgia", 10)
tela =  pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
fonte = pygame.font.Font(None,20)
pygame.display.set_caption("Space Maker")
space = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
som = pygame.mixer.Sound("Space_Machine_Power.mp3")
pygame.mixer.music.set_volume(0.3) 
som.play(-1)
pygame.display.set_icon(space)

def save_marks():
    try:
        with open('stars.pkl', 'wb') as f:
            pickle.dump(marcacoes, f)
    except IOError:
        print("Erro ao salvar as marcações.")


def load_marks():
    global marcacoes
    try:
        with open('stars.pkl', 'rb') as f:
            marcacoes = pickle.load(f)
    except FileNotFoundError:
        print("Arquivo de marcações não encontrado.")
        marcacoes = {}


def clear_marks():
    global marcacoes
    marcacoes = {}

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_marks()
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save_marks()
                pygame.quit()
            elif event.key == pygame.K_F10:
                save_marks()
            elif event.key == pygame.K_F11:
                load_marks()
            elif event.key == pygame.K_F12:
                clear_marks()


        if event.type == pygame.MOUSEBUTTONUP:
            posicaomouse = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            marcacoes[item] = posicaomouse
            if item == "":
                item = "Desconhecido"+str(posicaomouse)
            marcacoes[item] = posicaomouse
    
    tela.blit(fundo,(0,0))

    for item,posicao in marcacoes.items():
        pygame.draw.circle(tela,branco,posicao,raiodocirculo)
        pygame.draw.line(tela,branco,list(marcacoes.values())[0], posicao)
        texto = fonte.render(item,True,(255,255,255)) 
        tela.blit(texto,(posicao[0]+10, posicao[1]+ 10))

    escritanatela()

    #TELA
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)