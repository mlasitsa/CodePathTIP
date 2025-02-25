'''
Problem 3: Trilogy
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."

def trilogy(year):
	pass
Example Usage:

year = 2008
trilogy(year)

year = 1998
trilogy(year)
Example Output:

"The Dark Knight"
"Christopher Nolan did not release a Batman movie in 1998."
'''

def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print("Christopher Nolan did not release a Batman movie in " + str(year) + ".")

year = 2008
trilogy(year)