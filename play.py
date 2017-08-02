import time
import pygame
import numpy as np
num=str(np.random.randint(1,4))
file=r'yinpin/'+num+'.mp3'
pygame.mixer.init()
print("播放音乐")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.stop()
