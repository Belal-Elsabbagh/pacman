# Pacman Searching Agent

## About The Project

Pacman is a game where Pacman (the yellow circle with a mouth in the above figure) moves around in a maze and tries to eat as many food pellets (the small white dots) as possible, while avoiding the ghosts (the other two agents with eyes in the above figure). If Pacman eats all the food in a maze, it wins.

The project's structure is based upon the skeleton code in the UC Berkeley "Intro to AI" course which provides basic code for a command line tool, an GUI, and entity controllers for entities in the game.

## Project Structure

### Folders

- **layouts** - Layout files with different maps.
- **test_cases** - Predefined test cases to evaluate the project.

### Files

#### Configurations & Utility

- **pacman.py** - The main file and the game state configuration.
- **layout.py** - The map layout files parser.
- **util.py** - The data structures and algorithms supporting the searching algorithms' implementation.

#### Game Rules

- **game.py** - The game logic of pacman.

#### Game Rendering

- **graphicsDisplay.py** - The game graphics renderer.
- **graphicsUtil.py** - Helping module for graphicsDisplay.
- **textDisplay.py** - ASCII graphics for Pacman.

#### Entity Controllers

- **ghostAgents.py** - The Agents that control the ghosts.
- **keyboardAgents.py** - Helping module for graphicsDisplay.
- **searchAgents.py** - The search based agents that control entities.
- **search.py** - The searching algorithms that run search-based agents.

#### Testing

- **autograder.py** - The project grading script.
- **testParser.py** - Parses the test case files.
- **testClasses.py** - General auto grading test classes.
- **searchTestClasses.py** - Searching algorithms auto grading test classes.

## Process of running Searching Algorithms

1. The python interpreter starts at pacman.py.
2. The command line arguments given are parsed and processed. 
3. The given configuration is loaded into the script and the game starts running with the given arguments.
4. The pacman agent is initialized by:
   1. The map layout.
   2. The searching algorithm (with optional heuristic function) 
   3. The starting state.
   4. The goal state.
   5. The cost calculation function.
5. Pacman agent is notified that the game has started.
6. While the game is not over
   1. The agent checks if it had reached the goal
      1. If true, the agent updates the game state to over.
      2. Results are displayed and the game exits.
   2. The agent runs the searching function for the given game layout.
   3. The agent decides on its next move using 
      1. The cost calculation function
      2. the next position choice function.
   4. The agent executes the action to go to the next position.
   5. The interface engine updates the frame with the new state.

## References
http://ai.berkeley.edu/project_overview.html