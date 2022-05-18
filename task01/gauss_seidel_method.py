from task01.method import IterativeMethod
from utils.utils import diagonally_dominant, vector_euclidean_norm, vector_subtraction

class Gauss_Seidel_Method(IterativeMethod):
    def solve(self):
        if(not diagonally_dominant(self.matrix_A)):
            raise Exception("ERROR: Solução não converge, matriz não é diagonal dominante.")
        
        initial_solution = [1.0] * self.order
        next_solution = [0.0] * self.order
        residues = []

        residue = 1
        iteration = 0

        while(residue > self.maxTolerance):

            for i in range(self.order):
                summation = 0.0

                for j in range(self.order):
                    if(j>i):
                        summation += (-1)*self.matrix_A[i][j]*initial_solution[j]
                    if(j<i):
                        summation += (-1)*self.matrix_A[i][j]*next_solution[j]
        
                next_solution[i] = (self.vector_B[i] + summation)/self.matrix_A[i][i]

            iteration += 1
            residue = vector_euclidean_norm(vector_subtraction(next_solution, initial_solution))\
                    /vector_euclidean_norm(next_solution)
            
            for i in range(len(next_solution)):
                initial_solution[i] = next_solution[i]
            
            residues.append(residue)

        return {
        'vector': next_solution,
        'residues': residues,
        'numberofIterations': iteration
        }
