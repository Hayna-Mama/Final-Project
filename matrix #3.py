# Define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize sums
main_diagonal_sum = 0
secondary_diagonal_sum = 0

# Calculate sums of diagonal elements
for i in range(len(matrix)):
    main_diagonal_sum += matrix[i][i] 
    
# Sum of main diagonal
    secondary_diagonal_sum += matrix[i][len(matrix) - 1 - i]  
    
# Sum of secondary diagonal
print("Sum of main diagonal elements:", main_diagonal_sum)
print("Sum of secondary diagonal elements:", secondary_diagonal_sum)
