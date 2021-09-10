def neighbourStatus(left, right):
    # Returns 1 (HOME) if household are either away or both home
    # and returns 0 (AWAY) if one neighbour is away and other is home
    if left == right:
        return 1
    else:
        return 0


def leftHouse(initial, pos):
    # Returns the state of the left neighbour
    # Returns 0 (AWAY) when its the first house
    if pos == 0:
        return 0
    else:
        return initial[pos - 1]


def rightHouse(initial, pos):
    # Returns the state of the right neighbour
    # Returns 0 (AWAY) when its the last house
    if pos == len(initial) - 1:
        return 0
    else:
        return initial[pos + 1]


def calculateOccupancy(initial_state, num_of_weeks):
    final_state = []
    for week in range(0, num_of_weeks):
        final_state = []                                        # Reset the final state each week
        for house in range(0, len(initial_state)):
            left_house = leftHouse(initial_state, house)        # Check state of left house
            right_house = rightHouse(initial_state, house)      # Check state of right house
            if neighbourStatus(left_house, right_house) == 1:
                final_state.append(1)                           # Set house to be home if both are home
            else:
                final_state.append(0)
        initial_state = final_state                             # Set initial state to be the one from the week before
    return final_state


# INPUT 1
# initialOccupancy = [0,0,1,0,1]
# numOfWeeks = 1

# INPUT 2
initialOccupancy = [1, 1, 0, 0, 1, 0, 1]
numOfWeeks = 3

finalOccupancy = calculateOccupancy(initialOccupancy, numOfWeeks)
print(finalOccupancy)
