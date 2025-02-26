'''
Problem 5: Heist
The legendary outlaw Robin Hood is looking for the target of his next heist. Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

def wealthiest_customer(accounts):
	pass
Example Usage:

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)
Example Output:

[0, 6]
[1, 10]
[0, 17]
'''

def wealthiest_customer(accounts):
    max_wealth = 0
    max_index = 0

    for i in range(len(accounts)):
        wealth = 0  # Initialize wealth inside the outer loop
        
        for j in range(len(accounts[i])):  # Iterate through each bank account
            wealth += accounts[i][j]
        
        if wealth > max_wealth:  # Update max wealth and customer index
            max_wealth = wealth
            max_index = i
    
    return [max_index, max_wealth]

        