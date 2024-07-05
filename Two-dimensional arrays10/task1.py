# 4. Try it yourself
# Given a matrix:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# Print the matrix
# Print the transposed matrix. The result should be:

# 1 4 7 
# 2 5 8 
# 3 6 9 



import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

dimensions = matrix.shape

rows, columns = dimensions

for i in range(0,rows):
    for j in range(0,columns):
        print("{number} ".format(number=matrix[i,j]),end="")
    print()



# Print the matrix in a spiral 1, 2, 3, 6, 9, 8, 7, 4, 5

print("---------------------")

