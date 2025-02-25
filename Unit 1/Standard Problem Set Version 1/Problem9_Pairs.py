'''
Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
	pass
Example Usage

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
Example Output:

True
False
True
'''

def can_pair(item_quantities):
    # If the list is empty, Rabbit has nothing to worry about, so return True
    if not item_quantities:
        return True
    
    # Check each quantity in the list
    for qty in item_quantities:
        # If any quantity is odd, return False immediately
        if qty % 2 != 0:
            return False
    
    # If all quantities are even, return True
    return True
