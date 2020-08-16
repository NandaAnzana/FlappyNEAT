import pygame, sys

def check_collision(list_pipes, bird):
    for pipe in list_pipes:
        if  bird.rect.colliderect(pipe):
            return False
    
    if (bird.rect.top <= - 10) or (bird.rect.bottom >= 650):
        return False
    
    return True
