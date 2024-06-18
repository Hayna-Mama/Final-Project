def transpose_matrix(matrix):
    # Initialize an empty matrix for the transposed result
    transposed = []

    # Loop through columns of the original matrix
    for col in range(len(matrix[0])):
        # Create a new row for the transposed matrix
        new_row = []
        for row in range(len(matrix)):
            # Append the element from the original matrix to the new row
            new_row.append(matrix[row][col])
        # Append the new row to the transposed matrix
        transposed.append(new_row)
    
    return transposed

# Example input matrix (3x4)
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix
output_matrix = transpose_matrix(input_matrix)

# Print the transposed matrix
print("Transposed Matrix:")
for row in output_matrix:
    print(row)
