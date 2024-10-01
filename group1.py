import random
from copy import deepcopy

# Randomized partition function
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

# Partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized quick sort function
def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Modified group2 function
def group2(self, board):
    possible_moves = self.getPossibleMoves(board)
    if not possible_moves:
        self.game.end_turn()
        return
    
    # Sort the possible moves using randomized quick sort
    randomized_quick_sort(possible_moves, 0, len(possible_moves) - 1)
    
    # Select a random move from the sorted list
    random_move = random.choice(possible_moves)
    rand_choice = random.choice(random_move[2])
    
    return random_move, rand_choice
