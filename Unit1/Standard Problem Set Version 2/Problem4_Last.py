'''
Problem 4: Last
Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.

def get_last(items):
	pass
Example Usage

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
Example Output:

"black adam"
None
'''

def get_last(items):
    if items:  # Checks if the list is not empty
        return items[-1]  # Returns the last item in the list
    else:
        return None  # Returns None if the list is empty


