'''
Problem 3: T-I-Double Guh-Er II
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass
Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"Choir"
'''

def tiggerfy(word):
    # Define the set of substrings that Tigger removes
    removed_substrings = {'t', 'i', 'gg', 'er'}
    
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a variable to keep track of the current index in the input word
    i = 0
    
    # Loop through the input word
    while i < len(word):
        # Check if the current substring matches any of the removed substrings
        if word[i:i+1].lower() in removed_substrings:
            # Skip the substring by incrementing the index
            i += 1
        elif word[i:i+2].lower() in removed_substrings:
            # Skip the substring by incrementing the index
            i += 2
        elif word[i:i+3].lower() in removed_substrings:
            # Skip the substring by incrementing the index
            i += 3
        else:
            # Add the current character to the result
            result += word[i]
            i += 1
    
    # Return the final modified string