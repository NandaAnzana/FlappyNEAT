import pygame, sys

def check_collision(list_pipes, bird):
    for pipe in list_pipes:
        if  bird.rect.colliderect(pipe):
            return False
    
    if (bird.rect.top <= - 20) or (bird.rect.bottom >= 700):
        return False
    
    return True


def check_collision_neat(list_pipes, birds, genome_list, nets):
    for pipe in list_pipes:
        for i, bird in enumerate(birds):
            if  bird.rect.colliderect(pipe):
                genome_list[i].fitness -=1
                birds.pop(i)
                nets.pop(i)
                genome_list.pop(i)
    
            if (bird.rect.top <= - 10) or (bird.rect.bottom >= 650):
                genome_list[i].fitness -=1
                birds.pop(i)
                nets.pop(i)
                genome_list.pop(i)

            else:
                pass

    return birds, genome_list, nets