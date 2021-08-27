# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import time
import pygame

pygame.init()
pygame.mixer.music.load('TopGear.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#ou while(pygame.mixer.music.get_busy()):pass como sugerido nos comentários. ## leia a documentação, preguiçoso!
input('DALE!')
