# Pacman Searching Agent

- Belal Adel `2020/11213`
- Habiba Amr `2020/08121`

## About The Project

Pacman is a game where Pacman (the yellow circle with a mouth in the above figure) moves around in a maze and tries to eat as many food pellets (the small white dots) as possible, while avoiding the ghosts (the other two agents with eyes in the above figure). If Pacman eats all the food in a maze, it wins.

The project's structure is based upon the skeleton code in the UC Berkeley "Intro to AI" course which provides basic code for a command line tool, an GUI, and entity controllers for entities in the game.
___
## Project Structure

### Folders

- **layouts** - Layout files with different maps.
- **test_cases** - Predefined test cases to evaluate the project.
___
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
___ 

## Commands line tools

### Command line arguments 
- Show this help message and exit by typing `python pacman.py --help`
    ```commandline
      -h, --help                                    show this help message and exit
      -n GAMES, --numGames=GAMES                    the number of GAMES to play [Default: 1]
      -l LAYOUT_FILE, --layout=LAYOUT_FILE          the LAYOUT_FILE from which to load the map layout [Default: mediumClassic]
      -p TYPE, --pacman=TYPE                        the agent TYPE in the pacmanAgents module to use [Default: KeyboardAgent]
      -t, --textGraphics                            Display output as text only
      -q, --quietTextGraphics                       Generate minimal output and no graphics
      -g TYPE, --ghosts=TYPE                        the ghost agent TYPE in the ghostAgents module to use [Default: RandomGhost]
      -k NUMGHOSTS, --numghosts=NUMGHOST            The maximum number of ghosts to use [Default: 4]
      -z ZOOM, --zoom=ZOOM                          Zoom the size of the graphics window [Default: 1.0]
      -f, --fixRandomSeed                           Fixes the random seed to always play the same game
      -r, --recordActions                           Writes game histories to a file (named by the time they were played)
      --replay=GAMETOREPLAY                         A recorded game file (pickle) to replay
      -a AGENTARGS, --agentArgs=AGENTARGS           Comma separated values sent to agent. e.g."opt1=val1,opt2,opt3=val3"
      -x NUMTRAINING, --numTraining=NUMTRAINING     How many episodes are training (suppresses output) [Default: 0]
      --frameTime=FRAMETIME                         Time to delay between frames; <0 means keyboard [Default: 0.1]
      -c, --catchExceptions                         Turns on exception handling and timeouts during games
      --timeout=TIMEOUT                             Maximum length of time an agent can spend computing in a single game [Default: 30]
    ``` 


### Example commands

- You are able to start the game by typing the following commands in the command line:
   ```commandline
   pyhton pacman.py
   ```
- You can see the list of all options and their default values via:

   ```
   python pacman.py -h
   ```
- You can make pacman move west in a simple path to the west:
   ```
  python pacman.py --layout testMaze --pacman GoWestAgent
  ```
- You can make pacman move west in a simple tiny maze:
   ```
  python pacman.py --layout tinyMaze --pacman GoWestAgent
  ```
- You can see pacman move in a tiny maze layout using a search agent that uses the default search algorithm (DFS) using this command:
   ```
   python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
   ```


### Scenario 1: Finding a fixed food dot using Depth First Search:

- Pacman moves in the layout of a tiny maze and uses the DFS (Depth First Search) algorithm to find the food dot.
    ```
    python pacman.py -l tinyMaze -p SearchAgent
    ```
- Pacman moves in the layout of a medium maze and uses the DFS (Depth First Search) algorithm to find the food dot.
   ```
    python pacman.py -l mediumMaze -p SearchAgent
   ```
- Pacman moves in the layout of a big maze and uses the DFS (Depth First Search) algorithm to find the food dot.
   ```
    python pacman.py -l bigMaze -p SearchAgent
   ```

### Scenario 2: Finding a fixed food dot using Breadth First Search:
- Pacman moves in the layout of a medium maze using a search agent that uses the BFS (Breadth First Search) in a function to find the food dot:
   ```
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  ```
- Pacman moves in the layout of a big maze using a search agent that uses the BFS (Breadth First Search) in a function to find the food dot:
   ```
  python pacman.py -l bigMaze -p SearchAgent -a fn=bfs
  ```


### Scenario 3: Finding the best path using Uniform Cost Search:
- Pacman moves in the layout of a medium maze using a search agent that uses the UCS (Uniform Cost Search) in a function to find the food dot:
   ```
  python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
  ```
- Pacman moves in the layout of a medium-sized maze using a search agent that uses the UCS (Uniform Cost Search) in a function to find food dots in the maze in the eastern side of the maze first:
   ```
   python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
  ```
- Pacman moves in the layout of a medium-sized maze that has obstacles called ghosts using a search agent that uses the UCS (Uniform Cost Search) in a function to find the fixed food dot in the maze by moving in the western side of the maze first:
   ```
   python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
   ```


### Scenario 4: Finding the best path using A* search algorithm:
- Pacman moves in the layout of a big maze and uses a search agent that uses the A* search algorithm in a function to find the fixed food dot:
   ```
   python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
   ```


### Scenario 5: Finding all the corners:
- Pacman will move in the layout of tiny maze, and will use a search agent the uses the BFS algorithm in a function to solve the corners problem and find all the food dots located in the corners of the maze:
   ```
  python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
  ```
- Pacman will move in the layout of medium maze, and will use a search agent the uses the BFS algorithm in a function to solve the corners problem and find all the food dots located in the corners of the maze:
   ```
  python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
  ```


### Scenario 6: Corners Problem - Admissible and Consistent Heuristic:
- Pacman will move in the layout of medium maze to try to find fixed food dots in the corners using a non-trivial non-negative consistent heuristic function that returns 0 at every goal state and never returns a negative value:
   ```
  python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
  ```


### Scenario 7: Eating all the dots:
- Pacman will move in a tricky medium-sized maze layout using a search agent that uses a heuristic function (A*) that helps it eat all the food dots in as few steps as possible:
   ```
   python pacman.py -l trickySearch -p AStarFoodSearchAgent
  ```
- Pacman will move in a tiny maze layout to test a heuristic function that helps it reach the food dot:
   ```
  python pacman.py -l testSearch -p AStarFoodSearchAgent
  ```


### Scenario 8: Suboptimal Search:
- Pacman moves in a big maze layout and uses the "ClosestDotSearchAgent" search agent to find a path to the closest food dot:
   ```
   python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
   ```
___

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