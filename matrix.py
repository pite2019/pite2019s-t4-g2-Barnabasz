#!/usr/bin/env python3

class Matrix:

	def __init__(self, *a):
		self.contener = [list(a[:2]),list(a[2:])]

	def __getitem__(self, key):
		return self.contener[key]
	def __len__(self):
		return len(self.contener)

	def getList(self):
		return [var for el in self for var in el ]

	def trans(self):
		prod = [var for el in zip(*self) for var in el]
		return Matrix(*prod)

	def add_number(self, number):
		prod = [val + number for val in self.getList()]
		return Matrix(*prod)

	def add_matrix(self, second):
		prod = [val1 + val2 for val1, val2 in zip(self.getList(), second.getList())]
		return Matrix(*prod)
	
	def sub_number(self, number):
		return self.add_number(-number)

	def sub_matrix(self, second):
		prod = [val1 - val2 for val1, val2 in zip(self.getList(), second.getList())]
		return Matrix(*prod)

	def mul_number(self, number):
		prod = [val * number for val in self.getList()]
		return Matrix(*prod)

	def cros_prod(self, second):
		prod = []
		for i, _ in enumerate(self):
			for j, _ in enumerate(second[i]):
				tmp = 0
				for k, a in enumerate(self[i]):
					tmp += a * second[k][j]
				prod.append(tmp)
		return Matrix(*prod)

	def dot_prod(self, second):
		prod = []
		for i, A in enumerate(self):
			for j, _ in enumerate(second[i]):
				val = 0
				for k, B in enumerate(second):
					val += A[k]*B[j]
				prod.append(val)
		return Matrix(*prod)

	def __str__(self):
		return "[{}, {}]\n[{}, {}]\n".format(self[0][0], self[0][1], self[1][0], self[1][1])
	
	def __add__(self, second):
		if isinstance(second, (Matrix)):
			return self.add_matrix(second)
		elif isinstance(second, (int, float)):
			return self.add_number(second)

	def __sub__(self, second):
		if isinstance(second, (Matrix)):
			return self.sub_matrix(second)
		elif isinstance(second, (int, float)):
			return self.sub_number(second)

	def __mul__(self, second):
		if isinstance(second, (Matrix)):
			return self.cros_prod(second)
		elif isinstance(second, (int, float)):
			return self.mul_number(second)

	def __and__(self, second):
		return self.dot_prod(second)

	def __iadd__(self, second):
		return self.__add__(second)

	def __isub__(self, second):
		return self.__sub__(second)

	def __imul__(self, second):
		return self.__mul__(second)


	__radd__ = __add__
	__rsub__ = __sub__
	__rmul__ = __mul__

def test():
	matrix_1 = Matrix(1,2,3,4)
	matrix_2 = Matrix(5,6,7,8)
	print(matrix_1)
	print(matrix_2)
	# matrix_3 = matrix_2.add_matrix(matrix_1)
	# matrix_4 = matrix_3.cros_prod(matrix_2)
	# print(matrix_3)
	# print(matrix_4)
	# matrix_1[0][1] = 23
	# print(matrix_1)
	# matrix_1 += matrix_1
	print(matrix_1*matrix_2)
	

if __name__ == "__main__":
	test()