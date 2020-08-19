import pygame, sys
from src.obj.bird import Bird
from src.obj.floor import Floor
from src.obj.pipe import *
from src.util.collision import check_collision, check_collision_neat
from src.util.text import *
from src.config.config_neat import config_neat
import neat
import pickle



def eval(genomes, config):

	
	pygame.init()
	res = (1080,720)
	pygame.display.set_caption("FlappyBirdNEAT")
	screen = pygame.display.set_mode(res)
	icon = pygame.image.load('src/images/icon/flappyneat.ico').convert_alpha()
	pygame.display.set_icon(icon)
	bg = pygame.image.load('src/images/background/background0.png').convert()
	bg = pygame.transform.scale(bg,res)
	clock = pygame.time.Clock()

	game_start = False
	frame_count = 0
	score = 0
	pip_ind = 0
	floor = Floor()
	pipe_bottom = Pipe()
	pipe_top = Pipe(True)
	list_pipe = []
	list_pipe.extend(create_pipe(pipe_bottom, pipe_top))
	nets = []
	birds = []
	ge = []
	for _, g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g, config)
		nets.append(net)
		bird_ai = Bird()
		bird_ai.rect.center = (150,300)
		birds.append(bird_ai)
		g.fitness = 0
		ge.append(g)
	score = 0
	train = True

	while train:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()


	    screen.blit(bg, (0,0))
	    frame_count += 1
	    if len(birds) < 1:
	    	train = False
	    	break
	    if frame_count%360 == 0:
	    	frame_count = 0
	    	list_pipe.extend(create_pipe(pipe_bottom, pipe_top))
	    for i, rect in enumerate(list_pipe):
	    	if i%2 == 0:
	    		pipe_bottom.draw(screen, rect)
	    		rect = pipe_bottom.update_rect
	    		if (i == 0) and (rect.midright[0] == 100):
	    			pip_ind = 2
	    		if (i == 0) and (rect.center[0] <= -100):
	    			list_pipe = list_pipe[2:]
	    			pip_ind = 0
	    		if (i == 0) and (rect.center[0] == 100):
	    			for i, bird in enumerate(birds):
	    				ge[i].fitness += 10
	    			score += 1
	    	else:
	    		pipe_top.draw(screen, rect)
	    		rect = pipe_top.update_rect
	    for i,bird in enumerate(birds):
	    	pygame.draw.line(screen, (255,0,0), bird.rect.center, list_pipe[pip_ind].midtop)
	    	pygame.draw.line(screen, (255,0,0), bird.rect.center, list_pipe[pip_ind+1].midbottom)
	    	bird.update(screen)
	    	ge[i].fitness += 0.1
	    	output = nets[i].activate((bird.rect.centery, bird.rect.centery - list_pipe[pip_ind].midtop[1],
										bird.rect.centery - list_pipe[pip_ind+1].midbottom[1]))
	    	if output[0] > 0.5:
	    		bird.jump()
	    if score == 100:
	    	for i, bird in enumerate(birds):
	    				ge[i].fitness = 100000
	    birds, ge, nets = check_collision_neat(list_pipe, birds, ge, nets)
	    count_score(screen, score)
	    floor.draw(screen)
	    by_nanda(screen)
	    for_neat(screen)
	    pygame.display.update()
	    clock.tick(120)


def main():
	config_neat(eval)