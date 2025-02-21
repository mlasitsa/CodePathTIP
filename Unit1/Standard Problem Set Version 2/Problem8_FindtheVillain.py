'''

Problem 8: Find the Villain
Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.

def find_villain(crowd, villain):
	pass
Example Usage

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
Example Output:

[1, 4, 6]
'''

def find_villain(crowd, villain):
    indices = []  # List to store the indices where the villain is found
    
    # Iterate through the list with index tracking
    for index in range(len(crowd)):
        if crowd[index] == villain:  # Check if current element matches the villain
            indices.append(index)  # Store the index

    return indices  # Return the list of indices
