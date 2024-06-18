import numpy as np

# Define the matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Sum of each row
row_sums = np.sum(matrix, axis=1)

# Sum of each column
column_sums = np.sum(matrix, axis=0)

print("Sum of each row:", row_sums)
print("Sum of each column:", column_sums)
