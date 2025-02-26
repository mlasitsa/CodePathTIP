'''
Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
	pass
Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
Example Output:

2
4
'''

def final_value_after_operations(operations):
    tigger = 1  # Initialize tigger to 1
    
    # Iterate through each operation in the list
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1  # Increment tigger by 1
        elif operation == "trouncy" or operation == "pouncy":
            tigger -= 1  # Decrement tigger by 1
    
    return tigger  # Return the final value of tigger
    