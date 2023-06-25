import pygame
import sys

pygame.init()

# Configurações da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Estrelas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Lista de estrelas
estrelas = []

# Variáveis do clique
clique = False
posicao_clique = (0, 0)

# Variáveis de texto
fonte = pygame.font.Font(None, 36)
nome = ""

def exibir_tela():
    tela.fill(BRANCO)
    
    for estrela in estrelas:
        posicao, nome = estrela
        pygame.draw.circle(tela, VERMELHO, posicao, 10)
        texto = fonte.render(nome, True, PRETO)
        retangulo_texto = texto.get_rect(center=posicao)
        tela.blit(texto, retangulo_texto)
    
    pygame.display.flip()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clique = True
            posicao_clique = pygame.mouse.get_pos()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if nome == "":
                    nome = "Desconhecido"
                estrelas.append((posicao_clique, nome))
                clique = False
                nome = ""
    
    exibir_tela()

