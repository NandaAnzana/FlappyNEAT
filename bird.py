import pygame

class Bird:
    
    def __init__(self):
        self.i = 0
        self.delta = 1
        self.x = 150
        self.y = 300
        self.gravity = 0.2
        self.jumping = -7
        self.movement = 0
        self.images = [pygame.transform.scale(pygame.image.load("images/bird/bird0.png").convert_alpha() , (int(1090/11),int(750/11))),
                      pygame.transform.scale(pygame.image.load("images/bird/bird1.png").convert_alpha(), (int(1090/11),int(750/11))),
                      pygame.transform.scale(pygame.image.load("images/bird/bird0.png").convert_alpha(),(int(1090/11),int(750/11)))]
        self.image = self.images[self.i]
        self.rect = self.image.get_rect(center=(self.x,self.y))

    def update_delta(self):
        if self.i>2:
            self.delta = -1
        elif self.i<0:
            self.delta = 1

    def update(self, screen):
        screen.blit(pygame.transform.rotozoom(self.image, -(self.movement*2), 1), self.rect)
        self.movement += self.gravity
        self.rect.centery += self.movement
        self.i += self.delta
        if self.i>2:
            self.update_delta()
            self.i = 1
        elif self.i<0:
            self.update_delta()
            self.i = 1
        self.image = self.images[self.i]

    def jump(self):
        self.movement = 0
        self.movement += self.jumping
        self.rect.centery += self.movement
