'''
Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
	pass
Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
Example Output:

"nananananana batman!"
"batman!"
'''

def nanana_batman(x):
    na_string = ""  # Start with an empty string

    for _ in range(x):  # Loop x times
        na_string += "na"  # Append "na" in each iteration
    
    print(na_string + " batman!")  # Concatenate " batman!" and print the result

x = 6
nanana_batman(x)
