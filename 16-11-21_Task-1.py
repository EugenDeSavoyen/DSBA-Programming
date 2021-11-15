matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

flattened = [row[i] for row in matrix for i in range(len(matrix[0]))]
print(flattened)