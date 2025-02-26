'''
Problem 5: Concatenate
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

def concatenate(words):
	pass
Example Usage

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
Example Output:

"vengeancedarknessbatman"
""
'''

def concatenate(words):
    return "".join(words)

words = ["vengeance", "darkness", "batman"]
print(concatenate(words))