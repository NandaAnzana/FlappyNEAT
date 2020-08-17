import pygame

class Floor:

    def __init__(self):
        self.x = 0
        self.y = 650
        self.image = pygame.image.load('flappybird/images/background/floor0.png').convert()

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
        screen.blit(self.image, (self.x+1065,self.y))
        self.x -= 1
        if self.x <= -1065:
            self.x = 0