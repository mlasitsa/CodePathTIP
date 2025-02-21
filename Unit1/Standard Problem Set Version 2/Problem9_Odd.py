'''
Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

def get_odds(nums):
	pass
Example Usage

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
Example Output:

[1, 3]
[]
'''

def get_odds(nums):
    odd_numbers = []  # List to store odd numbers
    
    # Iterate through each number in the list
    for num in nums:
        if num % 2 != 0:  # Check if the number is odd
            odd_numbers.append(num)  # Add to the result list
    
    return odd_numbers  # Return the list of odd numbers
