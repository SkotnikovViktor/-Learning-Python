import random
import pygame

pygame.init()
pygame.mixer.init()
def music():
    c = ['Aria.mp3', 'basta.mp3']
    a = random.choice(c)
    pygame.mixer.music.load(a)
    pygame.mixer.music.play(0)
    while True:
        pygame.time.delay(100)


music()