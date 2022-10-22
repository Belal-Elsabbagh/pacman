def breadthFirstSearch(problem):
    "Search the shallowest node in the search tree first."
    # node <- a node with STATE = problem.INTITIAL-STATE, PATH-COST = 0
    # if problem.GOAL-TEST(node. STATE ) then return SOLUTION( node )
    # frontier <- a FIFO queue with node as the only element
    # explored <- an empty set
    # loop do
    #     if EMPTY?( frontier ) then return failure
    # node <- POP( frontier ) /* chooses the shallowest node in frontier */
    # add node.STATE to explored
    # for each action in problem.ACTIONS( node.STATE ) do
    #     child <- CHILD-NODE( problem, node, action )
    #     if child.STATE is not in explored or frontier then
    #         if problem.GOAL-TEST ( child.STATE ) then return SOLUTION(child)
    #         fronteir <- INSERT( child, fronteir )
