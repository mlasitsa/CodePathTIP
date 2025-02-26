'''
Problem 8: Local Maximums
Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
'''




def local_maximums(grid):
    n = len(grid)
    row_max = [[0] * (n - 2) for _ in range(n)]  # Store row-wise max values
    result = [[0] * (n - 2) for _ in range(n - 2)]  # Final result matrix

    # Compute row-wise max values
    for i in range(n):
        for j in range(n - 2):
            row_max[i][j] = max(grid[i][j], grid[i][j + 1], grid[i][j + 2])

    # Compute final 3x3 max using precomputed row max values
    for i in range(n - 2):
        for j in range(n - 2):
            result[i][j] = max(row_max[i][j], row_max[i + 1][j], row_max[i + 2][j])

    return result
    

    
	