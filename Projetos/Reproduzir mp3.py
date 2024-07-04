import pygame

print('Escolha o arquivo mp3:')
pygame.init()
escolher_musica = pygame.mixer.music.load('musica.mp3')
inicia = pygame.mixer.music.play()

