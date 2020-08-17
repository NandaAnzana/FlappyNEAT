import pygame
import random


class Pipe:

    def __init__(self, top=False):
        self.x = 1200
        self.image = pygame.transform.scale(pygame.image.load('src/images/pipe/pipe0.png'), (100,1024))
        self.top = top
        if self.top:
            self.image = pygame.transform.flip(self.image, False, True)

    def draw(self, screen, rect):
        self.rect = rect
        screen.blit(self.image, self.rect)
        self.rect.centerx -= 1

    @property
    def update_rect(self):
        return self.rect

def create_pipe(pipe_bottom, pipe_top):
    height = random.choice(range(250,600))
    rect_bot= pipe_bottom.image.get_rect(midtop=(pipe_bottom.x, height))
    rect_top = pipe_top.image.get_rect(midbottom=(pipe_top.x, height - 250))
    return [rect_bot, rect_top]