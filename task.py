#!/usr/bin/env python3

from matrix import Matrix

def test():
	matrix_1 = Matrix(4,5,6,7)
	matrix_2 = Matrix(2,2,2,1)

	matrix_3 = matrix_2.add(matrix_1)
	matrix_4 = matrix_3.prod(matrix_2)
	print(matrix_3)
	print(matrix_4)
	matrix_1[0][1] = 23
	print(matrix_1)

if __name__ == "__main__":
	test()