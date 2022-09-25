# O código ficou um pouco diferente devido a atualiazções
# recentes do Pygame
from pygame import init, mixer, event

mixer.init()
init()
mixer.music.load("qualidade.mp3")
mixer.music.play(loops=0, start=0)
input('"Enter" para finalizar')
event.wait()