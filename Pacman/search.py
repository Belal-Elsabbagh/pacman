# search.py
# ---------
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Queue, Stack, PriorityQueue


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def push_to_frontier(frontier, _object, priority=None):
    if priority is None:
        frontier.push(_object)
        return
    frontier.push(_object, priority)


def search_engine(_problem, _open_list, ignore_cost=False, blind_search=False, heuristic=nullHeuristic):
    """Runs a search on the given problem with the given data structure to store the frontiers."""
    problem = _problem
    open_list = _open_list
    visited_list = []
    path = []
    start_position = problem.getStartState()
    priority = None if blind_search else 0
    push_to_frontier(open_list, (start_position, path), priority)
    while not open_list.isEmpty():
        position, path = open_list.pop()
        if position in visited_list:
            continue
        visited_list.append(position)
        if problem.isGoalState(position):
            print(f'Directions: {path}')
            return path
        successors = problem.getSuccessors(position)
        for next_node, action, _ in successors:
            if next_node in visited_list:
                continue
            pos, path, priority = get_next_state(action, blind_search, heuristic, ignore_cost, next_node, path, problem)
            push_to_frontier(open_list, (pos, path), priority)


def get_next_state(action, blind_search, heuristic, ignore_cost, next_node, path, problem):
    new_position = next_node
    new_path = path + [action]
    cost_of_path = problem.getCostOfActions(new_path) if not ignore_cost else 0
    new_priority = (cost_of_path + heuristic(new_position, problem)) if not blind_search else None
    return new_position, new_path, new_priority


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    return search_engine(problem, Stack(), ignore_cost=True, blind_search=True)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return search_engine(problem, Queue(), ignore_cost=True, blind_search=True)


def aStarSearch(problem, heuristic=nullHeuristic, ignore_cost=False):
    """Search the node that has the lowest combined cost and heuristic first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), heuristic=heuristic)


def uniformCostSearch(problem):
    """Search the node of the least total cost first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), ignore_cost=True, blind_search=True)


def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), ignore_cost=True, heuristic=heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
