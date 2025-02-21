'''
Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	pass
Example Usage

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
Example Output:

[0, 3]
[]
'''

def locate_thistles(items):
    # Create an empty list to store the indices of "thistle"
    thistle_indices = []
    
    # Iterate through the list using index tracking
    for index in range(len(items)):
        # Check if the current item is "thistle"
        if items[index] == "thistle":
            # Add the index to the result list
            thistle_indices.append(index)
    
    # Return the final list of indices
    return thistle_indices
