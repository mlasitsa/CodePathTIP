'''
Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

def get_item(items, x):
	pass
Example Usage

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
Example Output:

"roo"
None
'''

def get_item(items, x):
    if x < len(items):
        return items[x]
    else:
        return None

def get_itemNOTEFFICIENT(items, x):
    if x > len(items) - 1 or x < 0:
        return None
    for i in range(len(items)):
        if i == x:
            return items[i]
    return None