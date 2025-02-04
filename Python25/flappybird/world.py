import pygame
from pipe import Pipe
from bird import Bird
from game import GameIndicator
from settings import WIDTH, HEIGHT, pipe_size, pipe_gap, pipe_pair_heights
import random

class World:
    def __init__(self, screen):
        self.screen = screen
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.current_pipe = None
        self.pipes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self._generate_world()
        self.playing = False
        self.game_over = False
        self.passed = True
        self.game = GameIndicator(screen)

    def _add_pipe(self):
        pipe_pair_height = random.choice(pipe_pair_heights)
        top_pipe_height, bottom_pipe_height = pipe_pair_height[0] * pipe_size, pipe_pair_height[1] * pipe_size
        pipe_top = Pipe((WIDTH, 0 - (bottom_pipe_height + pipe_gap)), pipe_size, HEIGHT, True)
        pipe_bottom = Pipe((WIDTH, top_pipe_height + pipe_gap), pipe_size, HEIGHT, False)

        self.pipes.add(pipe_top)
        self.pipes.add(pipe_bottom)
        self.current_pipe = pipe_top

    def _generate_world(self):
        self._add_pipe()
        bird = Bird((WIDTH // 2 - pipe_size, HEIGHT // 2 - pipe_size), 30)
        self.player.add(bird)

    #spillfysikk

    def _scroll_x(self):
        if self.playing:
            self.world_shift = -6
        else:
            self.world_shift = 0

    def _apply_gravity(self, player):
        if self.playing or self.game_over:
            player.direction.y += self.gravity
            player.rect.y += player.direction.y

    # begynte her 07.10

    def _handle_collisions(self):
        bird = self.player.sprite
        if pygame.sprite.groupcollide(self.player, self.pipes, False, False):
            self.playing = False
            self.game_over = True
        else:
            bird = self.player.sprite # sjekk om spillet funker uten senere
            if bird.rect.x >= self.current_pipe.rect.centerx:
                bird.score += 1
                self.passed = True

    def update(self, player_event = None):
        if self.current_pipe.rect.centerx <= (WIDTH // 2) - pipe_size:
            self._add_pipe()

        self.pipes.update(self.world_shift)
        self.pipes.draw(self.screen)

        self._apply_gravity(self.player.sprite)
        self._scroll_x()
        self._handle_collisions()

        if player_event == "jump" and not self.game_over:
            player_event = True

        elif player_event == "restart":
            self.game_over = False
            self.pipes.empty()
            self.player.empty()

            self.player.score = 0

            self._generate_world()

        else:
            player_event = False

        if not self.playing:
            self.game.instructions()

        self.player.update(player_event)
        self.player.draw(self.screen)
        self.game.show_score(self.player.sprite.score)

