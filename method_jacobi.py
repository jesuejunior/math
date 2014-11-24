# _*_ coding: utf-8 _*_
__author__ = 'jesuejunior'

import numpy as np

LIMIT = 1000


def jacobi(A, B):

    answer = np.zeros_like(B)
    for c in range(LIMIT):
        spare = np.zeros_like(answer) # Criando uma matriz de zeros do mesmo tamanho que answer
        if line_criterion(A):
            print "Problemas com criterio das linhas"
            break
        for i in range(A.shape[0]): #interando pelo tamanho das colunas
            s1 = np.dot(A[i, :i], answer[:i]) # multiplicando linha matriz de entrada com linha da matrix transversal
            s2 = np.dot(A[i, i + 1:], answer[i + 1:])
            spare[i] = (B[i] - s1 - s2) / A[i, i]
        if np.allclose(answer, spare, rtol=1e-10):
            break
        answer = spare
    return answer


def line_criterion(matrix):
    i, j = 0, 0
    while i < len(matrix):
        soma = 0
        while j <= matrix.shape[0]:
            if i != j:
                soma += matrix[i][j]
            j += 1
        if matrix[i][i] < soma:
            return False
        i += 1
    return True


def main():
    A = np.array([[3., 1., 2., -1.],
                  [1., 1., 0., 0.],
                  [2., 2., -1., 1.]])

    B = np.array([])

    print u"Conjunto solução S: {0}".format(jacobi(A, B))

if __name__ == '__main__':
    main()

# Choose an initial guess x^{(0)} to the solution
#  k = 0
# while convergence not reached do
# for i := 1 step until n do
#  \sigma = 0
# for j := 1 step until n do
# if j ≠ i then
#  \sigma  = \sigma  + a_{ij} x_j^{(k)}
# end if
# end (j-loop)
#   x_i^{(k+1)}  = {{\left( {b_i  - \sigma } \right)} \over {a_{ii} }}
# end (i-loop)
# check if convergence is reached
# k = k + 1
# loop (while convergence condition not reached)
