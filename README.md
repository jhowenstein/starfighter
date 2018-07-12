# starfighter

Computer Game based on the classic video game Space Invaders with expanded features.

This project was initially started to practice implementing object oriented software design patterns while working through the book: http://www.gameprogrammingpatterns.com/

Game Dependencies:
* Python 3
* PyGame (https://www.pygame.org/wiki/GettingStarted)
* Numpy (https://www.scipy.org/scipylib/download.html)

Supported Platforms:
* Raspberry Pi (Raspberian)
* Linux
* Windows (Not fully tested but should work with dependencies installed)
* Note: Mac currently not functional due to bug preventing PyGame from correctly capturing user input

This game was developed with the Raspberry Pi (Running the Raspberian Linux distrubition) as the target platform.

All code is written in Python 3.

Game Modes:
* Single Player
  * Survival: Main single player game mode. The game continues forever until the user is eliminated. Time survived, enemies destroy, and rounds completed are tracked displayed at the end of the game.
  * Campaign: Currently under development. Campaign is intended to be 10 levels that are completed sequentially.
* Two Player:
  * Player vs. Player: Players can choose thier ship type of choice (heavy, medium, light) and duel with a friend. 

Instructions to Run:
* Download all files into a local directory
* Ensure depencies have been installed
* From the terminal, Run "starship_main.py" using the python3 interpreter (ex. python3 starship_main.py)

Future Development:
* Complete Campaign Mode
* Add additional weapon types to be unlocked or purchased as the game progresses
* Additional options for ship functionality and performance customization
* Add unlockable power-ups such as shields, temporary boosted damage or speed
