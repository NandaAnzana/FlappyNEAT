import neat
import os
import pickle


def config_neat(eval):
    config_file = os.path.join(os.path.dirname(__file__),"config.txt")
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, 
								neat.DefaultStagnation, config_file)
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    end = pop.run(eval,50)
    with open("src/config/NEATmodel.pkl", "wb") as f:
    	pickle.dump(end, f)