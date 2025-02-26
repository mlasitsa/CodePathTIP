'''
Problem 4: Good Samaritan
Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. He wants to distribute meals in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes.

def minimum_boxes(meals, capacity):
	pass
Example Usage:

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)
Example Output:

2
4
'''

def minimum_boxes(meals, capacity):
    meals.sort(reverse=True)  # Sort meals in descending order
    capacity.sort(reverse=True)  # Sort boxes in descending order

    boxes_used = 0
    i, j = 0, 0  # Pointers for meals and boxes

    while i < len(meals):
        meal = meals[i]
        while meal > 0 and j < len(capacity):
            if capacity[j] > 0:  # Only use non-empty boxes
                used = min(meal, capacity[j])
                meal -= used
                capacity[j] -= used
                if capacity[j] == 0:  # Move to the next box if full
                    boxes_used += 1
                    j += 1
        if meal > 0:  # If meal couldn't be fully placed, use a new box
            return -1  # Not possible to distribute meals
        i += 1

    return boxes_used

