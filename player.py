import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = None

    def play(self, archivo):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(base_dir, archivo)

        pygame.mixer.music.load("music/feel_special.mp3")
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song = None