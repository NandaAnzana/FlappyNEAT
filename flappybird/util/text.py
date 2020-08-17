import pygame


pygame.font.init()

score_font = pygame.font.Font('flappybird/util/pricedown bl.ttf', 30)
font = pygame.font.Font('flappybird/util/pricedown bl.ttf', 14)
press = pygame.font.Font('flappybird/util/pricedown bl.ttf', 45)


def by_nanda(screen):
    created_by = font.render("Created by Nanda Anzana", True, (25,25,25))
    rect = created_by.get_rect(bottomright=(1060,700))
    return screen.blit(created_by, rect)


def for_neat(screen):
    created_by = font.render("For NEAT Learning", True, (0,0,0))
    rect = created_by.get_rect(bottomright=(1060,714))
    return screen.blit(created_by, rect)

def high_score(screen, high_score):
    created_by = score_font.render("High score: {}".format(high_score), True, (0,0,0))
    rect = created_by.get_rect(center=(540,400))
    return screen.blit(created_by, rect)

def your_score(screen, score):
    created_by = score_font.render("Your score: {}".format(score), True, (0,0,0))
    rect = created_by.get_rect(center=(540,350))
    return screen.blit(created_by, rect)

def count_score(screen, score):
    created_by = score_font.render("Score: {}".format(score), True, (0,0,0))
    rect = created_by.get_rect(topright=(1060,10))
    return screen.blit(created_by, rect)

def press_to_start(screen):
    created_by = press.render("Press ; to start", True, (200,100,100))
    rect = created_by.get_rect(center=(540,300))
    return screen.blit(created_by, rect)

def press_to_jump(screen):
    created_by = press.render("Press space to jump", True, (200,100,100))
    rect = created_by.get_rect(center=(540,250))
    return screen.blit(created_by, rect)