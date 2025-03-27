import model
import copy

GENERATED = 0

#Implementing minimax algorithm
def minimax(node, depth, maximizingPlayer):
    global GENERATED

    if depth == 0 or len(node.available_tiles())==0:
        return None, node.getHeuristic()
    
    if maximizingPlayer:
        maxChild, maxEval = None, float('-inf')

        for kid in node.getChildren():
            GENERATED += 1
            child = copy.deepcopy(node)
            child.move(kid)
            child.addTile()
            _, value = minimax(child, depth-1, False)
            if value > maxEval:
                maxChild, maxEval = child, value

        return maxChild, maxEval
    
    if not maximizingPlayer:
        GENERATED += 1
        minChild, minEval = None, float('inf')

        for kid in node.getChildren():
            child = copy.deepcopy(node)
            child.move(kid)
            child.addTile()
            _, value = minimax(child, depth-1, True)
            if value < minEval:
                minChild, minEval = child, value

        return minChild, minEval

#function to get the next best move from minimax algorithm
def getOptimalMove(initial_board, depth):
    node_copy = copy.deepcopy(initial_board)
    child, _ = minimax(node_copy, depth, True)
    return initial_board.getMoveTo(node_copy, child)


if __name__ == '__main__':
    board = model.Board()
    nodes_expanded = 1

    while True:
        if len(board.available_tiles()) == 0:
            print("game over :( ")
            print("generated tiles:")
            print(GENERATED)
            break
        dir = getOptimalMove(board, 3)
        board.move(dir)
        board.addTile()
        print(dir)
        print(board)
        print("nodes expanded: " + str(nodes_expanded))
        nodes_expanded+=1
        