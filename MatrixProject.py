#  File: MatrixProject.py

#  Description: Performs row reduction with partial pivoting to reduce a matrix to echelon form. Also counts FLOPs.

#  Student Name: Carlos Vazquez

#  Student UT EID: czv72

#  Course Name: M340L

import random
import numpy.matlib

def gaussian_elim(matrix, m, n):
    # Counts the floating point operations
    global flops
    flops = 0

    # Represents the current place along the diagonal
    i = 0

    # Repeats until the diagonal reaches the limiting value
    while(i < n):

        # Performs partial pivoting, swaps the current row with the row that has the largest value
        for q in range(i + 1, m):
            if(abs(matrix[i, i]) < abs(matrix[q, i])):
                matrix[[q, i]] = matrix[[i, q]]

        # Eliminates values below the pivot
        for j in range(i + 1, m):
            if(matrix[i,i] != 0.0):
                flops += 1 # Division of two single values
                scaling = matrix[j, i] / matrix[i, i]
                flops += 2 * n # Multiplication of each value in row, then subtracting two rows
                matrix[j] = matrix[j] - (scaling * matrix[i])

        i += 1
            



def main():
#Question 1
    # Determine the m x n size of matrix
    m = 100
    n = 10
    
    # Create an m x n matrix with random entries all between 0 and 1
    matrix = numpy.matlib.rand(m,n)

    # Print the matrix prior to row reduction
    print(matrix)

    # Perform Gaussian Elimination
    gaussian_elim(matrix, m, n)

    # Print the matrix after row reduction
    print()
    print(matrix)


# Question 2
    # Create random 5x5 matrix and count the FLOPs
    matrix_1 = numpy.matlib.rand(5,5)
    gaussian_elim(matrix_1, 5, 5)
    print(flops)
    
    # Create random 50x50 matrix and count the FLOPs
    matrix_2 = numpy.matlib.rand(50,50)
    gaussian_elim(matrix_2, 50, 50)
    print(flops)

    # Create random 500x500 matrix and count the FLOPs
    matrix_3 = numpy.matlib.rand(500,500)
    gaussian_elim(matrix_3, 500, 500)
    print(flops)


    

if __name__ == "__main__":
    main()
