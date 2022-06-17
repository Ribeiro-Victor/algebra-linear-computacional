from P1.task03.method import Method
from P1.task01.lu_method import LU_Method
class Regression(Method):
	def solve(self):
		matrix_A = [[0.0] * 2 for _ in range(2)]
		vector_C = [0.0, 0.0]

		matrix_A[0][0] = self.n
		for i in range(self.n):
			matrix_A[0][1] += self.points[i][0]
			matrix_A[1][0] += self.points[i][0]
			matrix_A[1][1] += self.points[i][0] ** 2
			vector_C[0] += self.points[i][1]
			vector_C[1] += self.points[i][0] * self.points[i][1]

		solution = LU_Method(
			order=2,
			determinant_calc=False,
			matrix_A=matrix_A,
			vector_B=vector_C
		).solve()
		vector_X = solution["vector"]
		
		return (self.x * vector_X[1]) + vector_X[0]