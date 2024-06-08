#CET313 Codie Heaney - bh97rt

import random as rand

class Matrix:
    #create a matrix with a set of rows and cols provided filled with 0s
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for x in range(cols)] for y in range(rows)]

    #transfer matrix array into matrix object
    @staticmethod
    def matrixToMatrixObj_return(inp, rows, cols):
        result = Matrix(cols, rows)
        for i in range(0, result.rows):
            for j in range(0, result.cols):
                result.data[j][i] = inp[j][i];
        return result

    #transpose matrix, move values in columns to rows and rows to columns
    @staticmethod
    def transpose_return(matrix):
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(0, matrix.rows):
            for j in range(0, matrix.cols):
                result.data[j][i] = matrix.data[i][j];
        return result

    #transpose this matrix, move values in columns to rows and rows to columns
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                result.data[j][i] = self.data[i][j]
        self.data = result.data

    #turn array/list into a matrix object with array/lists values
    @staticmethod
    def fromArray_return(arr):
        matrix = Matrix(len(arr), 1)
        for i in range(0, len(arr)):
            matrix.data[i][0] = arr[i]
        return matrix

    #turn this matrix into a 1D array with all its values
    def toArray(self):
        arr=[]
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                arr.append(self.data[i][j])
        return arr

    #return the subtraction matrix of two matrixes
    @staticmethod
    def subtract_return(matrix_a, matrix_b):
        result = Matrix(matrix_a.rows, matrix_a.cols)
        for i in range(0,result.rows):
            for j in range(0,result.cols):
                result.data[i][j]= matrix_a.data[i][j] - matrix_b.data[i][j]
        return result

    #return the multiplaction matrix of two matrixes
    @staticmethod
    def multiply_return(matrix_a, matrix_b):
        result = Matrix(matrix_a.rows, matrix_b.cols)
        for i in range(0, result.rows):
            for j in range(0, result.cols):
                total = 0
                for k in range(0, matrix_a.cols):
                    total += matrix_a.data[i][k] * matrix_b.data[k][j]
                result.data[i][j] = total
        return result

    #multiply this matrix with another matrix, or multiply every value in this matrix by a single number
    def multiply(self, num):
        if(isinstance(num, Matrix)):
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.data[i][j] *= num.data[i][j]
        else:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.data[i][j] *= num

    #perform a given function to every value on this matrix
    def map_func(self, func):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                val = self.data[i][j]
                self.data[i][j] = func(val);

    #return a matrix with values of a provided martix after performing a given function to every value on the provided matrix  
    @staticmethod
    def map_func_return(matrix, func):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(0, matrix.rows):
            for j in range(0, matrix.cols):
                val = matrix.data[i][j]
                result.data[i][j] = func(val)
        return result

    #add the values of a matrix to this matrix, or add a single number to each value of this matrix
    def add(self, num):
        if(isinstance(num, Matrix)):
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.data[i][j] += num.data[i][j]
        else:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.data[i][j] += num

    #fill this matrix with a random float number between -1 and 1
    def randomise(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.data[i][j] = rand.uniform(-1, 1)

    #print all matrix data to console
    def show(self):
        print(self.data)
