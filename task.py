#!/usr/bin/env python3

class Matrix:

	def __init__(self, a, b, c, d):
		self.contener = [[a,b],[c,d]]
		self.a, self.b, self.c, self.d = a, b, c, d

	def __getitem__(self, key):
		return self.contener[key]
	def add(self, second):
		a = self.contener[0][0] + second.contener[0][0]
		b = self.contener[0][1] + second.contener[0][1]
		c = self.contener[1][0] + second.contener[1][0]
		d = self.contener[1][1] + second.contener[1][1]
		return Matrix(a, b, c, d)

	def __repr__(self):
		return "[{}, {}]\n[{}, {}]".format(self.contener[0][0], self.contener[0][1], self.contener[1][0], self.contener[1][1])
	
	def prod(self, second):
		a = self.contener[0][0] * second.contener[0][0] + self.contener[0][1] * second.contener[1][0]
		b = self.contener[0][0] * second.contener[0][1] + self.contener[0][1] * second.contener[1][1]
		c = self.contener[1][0] * second.contener[0][0] + self.contener[1][1] * second.contener[1][0]
		d = self.contener[1][0] * second.contener[0][1] + self.contener[1][1] * second.contener[1][1]
		return Matrix(a, b, c, d)


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