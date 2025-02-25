'''
Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
	pass
Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4
'''

def up_and_down(lst):
    odd_count = 0  # Counter for odd numbers
    even_count = 0  # Counter for even numbers
    
    # Iterate through each number in the list
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
        else:  # Otherwise, it's odd
            odd_count += 1
    
    # Return the difference (odd count - even count)
    return odd_count - even_count
