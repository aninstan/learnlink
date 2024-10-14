import pygame
from settings import HEIGHT, HEIGHT

pygame.font.init()

class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Bauhaus 93', 60)
        self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)
        self.color = pygame.Color("white")
        self.inst_color = pygame.Color("black")

    def show_score(self, int_score):
        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)
        self.screen.blit(score, (HEIGHT // 2, 50))

    def instructions(self):
        inst_text1 = "Press SPACE to Jump,"
        inst_text2 = "Press \"R\" to restart game."
        inst1 = self.inst_font.render(inst_text1, True, self.inst_color)
        inst2 = self.inst_font.render(inst_text2, True, self.inst_color)
        self.screen.blit(inst1, (95,400))
        self.screen.blit(inst2, (70,450))