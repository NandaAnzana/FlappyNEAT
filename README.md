## Flappy Bird

Flappy Bird is a mobile game developed by Vietnamese video game artist and programmer [Dong Nguyen](https://www.google.com/search?safe=strict&client=firefox-b-d&sxsrf=ALeKk02J6fK3I7gpq4Q6QQFHunudeee0Og%3A1597861005967&ei=jWw9X_-1OqPEz7sP0MSWoAc&q=dong+nguyen&oq=dong+nguyen&gs_lcp=CgZwc3ktYWIQAzIFCC4QkwIyAggAMgIIADICCAAyAggAMgcIABAUEIcCMgIIADICCAAyAggAMgIIADoHCAAQRxCwAzoECCMQJzoFCAAQkQI6BQguEJECOgQIABBDOggIABCxAxCDAToLCAAQsQMQgwEQiwM6CAgAELEDEIsDOgoIABAUEIcCEIsDOggILhCRAhCTAjoFCC4QsQM6BAguEEM6CAguELEDEIsDOgcIABCxAxBDOgoIABCxAxBDEIsDOgsILhCxAxCDARCLAzoHCC4QQxCTAjoCCC46BQgAEIsDOgUILhCLAzoOCC4QiwMQqAMQmAMQmgM6BAguEApQzYiAAVipo4ABYIOngAFoAXAAeACAAd8BiAGZDZIBBTAuOC4zmAEAoAEBqgEHZ3dzLXdpergBAsABAQ&sclient=psy-ab&ved=0ahUKEwi_sKSN8KfrAhUj4nMBHVCiBXQQ4dUDCAs&uact=5). Nguyen created the game over the period of several days, using a bird protagonist that he had designed for a cancelled game in 2012.

Flappy Bird is an arcade-style game in which the player controls the bird Faby, which moves persistently to the right. The player is tasked with navigating Faby through pairs of pipes that have equally sized gaps placed at random heights. Faby automatically descends and only ascends when the player taps the touchscreen. Each successful pass through a pair of pipes awards the player one point. Colliding with a pipe or the ground ends the gameplay.
<br></p>
<p align="center">
  <img src="images\Flappy_Bird_gameplay.png" alt="Original flappy bird">
</p>
<br>
Flappy bird made me interested to build a replica for desktop version. Because the original version makes me wanna throw pizza to the window, so i made my version much more difficult. So, enjoy it.

First you must make sure your python version is 3.x and pygame already installed in your environment. Then you change your working directory to the folder you want to put this flappyNEAT.
```
cd your_path_name
```
Then clone this repository.
```
git clone https://github.com/NandaAnzana/FlappyNEAT.git
```
Change your directory to FlappyNEAT folder.
```
cd FlappyNEAT
```
Then run playable FlappyNEAT.
```
python flappy.py
```
<p align="center">
  <img src="images\FlappyNEAT.gif" alt="FlappyNEAT">
</p>

## NEAT for Flappy Bird Problem

NEAT is a method developed by [Kenneth O. Stanley](https://www.cs.ucf.edu/~kstanley/) for evolving arbitrary neural networks. This method based on [Evolving Neural Networks through Augmenting Topologie](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.28.5457&rep=rep1&type=pdf) paper. NEAT-Python is a pure Python implementation of NEAT, with no dependencies other than the Python standard library.

One of the trickiest part when build this, is to set how the bird see the pipe. When the bird too early change the attention to another pipe, the bird always fail even for large generation. When the bird too late change the attention to another pipe, the bird late take the action and fail to keep up the height.
<p align="center">
  <img src="images\FlappyAI.gif" alt="FlappyNEAT">
</p>
First you must make sure your python version is 3.X, pygame and neat-python already installed in your environment. Then you change your working directory to the folder you want to put this flappyNEAT.
```
cd your_path_name
```
Then clone this repository.
```
git clone https://github.com/NandaAnzana/FlappyNEAT.git
```
Change your directory to FlappyNEAT folder.
```
cd FlappyNEAT
```
Then run FlappyNEAT that use NEAT model.
```
python flappyNEAT.py
```
You can change the hyperparameter in this txt file.
```
../FlappyNEAT/src/config/config.txt
```

## References

<p><ul>
<li>Youtube:<ul>
<li><a href="https://www.youtube.com/watch?v=UZg49z76cLw" title="Clear Code">Learning pygame by making Flappy Bird </a>by Clear Code</li>
<li><a href="https://www.youtube.com/watch?v=FfWpgLFMI7w&t=192s" title="freeCodeCamp.org">Pygame Tutorial for Beginners - Python Game Development Course </a>by  freeCodeCamp.org</li>
<li><a href="https://www.youtube.com/watch?v=OGHA-elMrxI&t=141s" title="Tech with Tim">AI Teaches Itself to Play Flappy Bird - Using NEAT Python! </a>by Tech with Tim</li>
<li><a href="https://www.youtube.com/watch?v=2o-jMhXmmxA" title="Cheesy AI">Simple AI Tutorial with NEAT-python </a>by Cheesy AI</li></ul></li></ul>

That's all. Keep learning!</p>