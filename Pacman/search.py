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
    open_list, path, priority, position, visited_list = init_search_engine(_open_list, _problem, blind_search)
    push_to_frontier(open_list, (position, path), priority)
    while not open_list.isEmpty():
        position, path = open_list.pop()
        if position in visited_list:
            continue
        visited_list.append(position)
        if _problem.isGoalState(position):
            print(f'Directions: {path}')
            return path
        successors = _problem.getSuccessors(position)
        for next_node, action, _ in successors:
            new_path = path + [action]
            new_priority = calculate_priority(blind_search, heuristic, ignore_cost, new_path, next_node, _problem)
            push_to_frontier(open_list, (next_node, new_path), new_priority)


def calculate_priority(blind_search, heuristic, ignore_cost, new_path, next_node, problem):
    cost_of_path = problem.getCostOfActions(new_path) if not ignore_cost else 0
    return (cost_of_path + heuristic(next_node, problem)) if not blind_search else None


def init_search_engine(_open_list, _problem, blind_search):
    problem = _problem
    open_list = _open_list
    visited_list = []
    path = []
    start_position = problem.getStartState()
    priority = None if blind_search else 0
    return open_list, path, priority, start_position, visited_list


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
    return search_engine(_problem=problem, _open_list=PriorityQueue(), ignore_cost=True, blind_search=False)


def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), ignore_cost=True, heuristic=heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
