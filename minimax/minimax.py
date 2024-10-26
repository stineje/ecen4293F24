import math


def minimax(depth, nodeIndex, isMaximizingPlayer, scores, targetDepth):
    # Base case: If we have reached the target depth (leaf node level)
    if depth == targetDepth:
        return scores[nodeIndex]

    # If it's the Maximizing player's turn
    if isMaximizingPlayer:
        return max(minimax(depth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(depth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

    # If it's the Minimizing player's turn
    else:
        return min(minimax(depth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(depth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


# Example scores for the leaf nodes of a binary tree
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Calculate the depth of the tree (log base 2 of number of leaf nodes)
tree_depth = int(math.log2(len(scores)))

# Start the minimax algorithm from the root node (index 0) and depth 0 with the maximizing player
result = minimax(0, 0, False, scores, tree_depth)

# Output the optimal value according to the Minimax algorithm
print("The optimal value is:", result)
