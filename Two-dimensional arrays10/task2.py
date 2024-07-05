
import numpy as np

# matrix = np.array([
#     [1, 5, 9, 13],
#     [2, 6, 10, 14],
#     [3, 7, 11, 15],
#     [4, 8, 12, 16]
# ])

matrix = np.array([
    [1,4,7],
    [2,5,8],
    [3,6,9]
])

# matrix = np.array([
#     [1, 6, 11, 16, 21],
#     [2, 7, 12, 17, 22],
#     [3, 8, 13, 18, 23],
#     [4, 9, 14, 19, 24],
#     [5, 10, 15, 20, 25]
# ])


dimensions = matrix.shape

rows, columns = dimensions

rowMIN = 0;
rowMAX = rows-1;

columnMIN = 0;
columnMAX = columns-1;

i = rowMIN
j = columnMIN
k = rowMAX
l = columnMAX

isItStillPrinting = True

while isItStillPrinting:

    isItStillPrinting = False

    i = rowMIN
    while i <= rowMAX:
        print(matrix[i, columnMIN])
        isItStillPrinting = True
        i+=1
    else:
        columnMIN = columnMIN + 1

    j = columnMIN
    while j <= columnMAX:
        print(matrix[columnMAX,j])
        isItStillPrinting = True
        j+=1
    else:
        rowMAX = rowMAX - 1
    
    k = rowMAX
    while k >= rowMIN:
        print(matrix[k,columnMAX])
        isItStillPrinting = True
        k-=1
    else:
        columnMAX = columnMAX - 1
    
    l = columnMAX
    while l >= columnMIN:
        print(matrix[rowMIN,l])
        isItStillPrinting = True
        l-=1
    else:
        rowMIN = rowMIN + 1