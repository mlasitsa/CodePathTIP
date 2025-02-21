'''
Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
	pass
Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
Example Output:

['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]
'''

def shuffle(cards):
    n = len(cards) // 2  # Determine the midpoint
    shuffled = []  # List to store shuffled elements

    # Iterate through the first half (x1, x2, ..., xn)
    for i in range(n):
        shuffled.append(cards[i])       # Append from first half (x1, x2, ..., xn)
        shuffled.append(cards[i + n])   # Append from second half (y1, y2, ..., yn)

    return shuffled
