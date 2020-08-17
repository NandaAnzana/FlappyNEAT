import pygame, sys
from src.obj.bird import Bird
from src.obj.floor import Floor
from src.obj.pipe import *
from src.util.collision import check_collision
from src.util.text import *
import pickle



def main():

	pygame.init()
	res = (1080,720)
	pygame.display.set_caption("FlappyBirdNEAT")
	screen = pygame.display.set_mode(res)
	bg = pygame.image.load('src/images/background/background0.png').convert()
	bg = pygame.transform.scale(bg,res)
	clock = pygame.time.Clock()
	# SPAWNPIPE = pygame.USEREVENT
	#pygame.time.set_timer(SPAWNPIPE, 3000)

	game_start = False
	frame_count = 0
	score = 0

	bird = Bird()
	floor = Floor()
	pipe_bottom = Pipe()
	pipe_top = Pipe(True)
	list_pipe = []


	try:
	    with open("src/high score.pkl", "rb") as f:
	        high_score_all_time = pickle.load(f)
	except:
	    high_score_all_time = 0

	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            with open("src/high score.pkl", "wb") as f:
	                pickle.dump(high_score_all_time, f)
	            pygame.quit()
	            sys.exit()
	        elif event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_SPACE and game_start:
	                bird.jump()
	            if event.key == pygame.K_SEMICOLON and game_start == False:
	                game_start = True
	                list_pipe.clear()
	                bird.rect.center = (150,300)
	                bird.movement = 0
	                score = 0

	    screen.blit(bg, (0,0))
	    if game_start:
	        frame_count += 1
	        if frame_count%360 == 0:
	            frame_count = 0
	            list_pipe.extend(create_pipe(pipe_bottom, pipe_top))
	        for i, rect in enumerate(list_pipe):
	            if i%2 == 0:
	                pipe_bottom.draw(screen, rect)
	                rect = pipe_bottom.update_rect
	                if (i == 0) and (rect.center[0] <= -100):
	                    list_pipe = list_pipe[2:]
	                if (i == 0) and (rect.center[0] == 100):
	                    score += 1
	            else:
	                pipe_top.draw(screen, rect)
	                rect = pipe_top.update_rect

	        bird.update(screen)
	        game_start = check_collision(list_pipe, bird)
	        count_score(screen, score)
	                    
	    else:
	        if high_score_all_time < score:
	            high_score_all_time = score
	        press_to_start(screen)
	        press_to_jump(screen)
	        your_score(screen, score)
	        high_score(screen, high_score_all_time)
	    floor.draw(screen)
	    by_nanda(screen)
	    for_neat(screen)
	    pygame.display.update()
	    clock.tick(120)