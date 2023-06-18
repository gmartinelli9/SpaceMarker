import pygame
import winsound
pygame.init()

tamanho = (1000,563)
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("SPACE MARKER")
clock = pygame.time.Clock()
space = pygame.image.load("space.png")
pygame.display.set_icon(space)
from tkinter import simpledialog

def jogo():
    