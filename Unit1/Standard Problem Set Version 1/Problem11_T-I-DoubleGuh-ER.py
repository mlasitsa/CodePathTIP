'''
Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
	pass
Example Usage

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
Example Output:

"suspcous"
""
"Hunny"
'''

def tiggerfy(s):
    # Define the set of letters that Tigger steals
    stolen_letters = {'t', 'i', 'g', 'e', 'r'}
    
    # Initialize an empty string to store the result
    result = ""
    
    # Loop through each character in the input string
    for char in s:
        # Convert the character to lowercase to check case-insensitively
        lower_char = char.lower()

        # If the character is NOT in the stolen letters, add it to result
        if lower_char not in stolen_letters:
            result += char  # Preserve original case
        
    # Return the final modified string
    return result
