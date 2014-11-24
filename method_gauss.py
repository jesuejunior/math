# _*_ coding: utf-8 _*_
__author__ = 'jesuejunior'
import numpy as np
#Metodo de resoluçõa do sistemas de Gauss

def gauss(m):

    #Criando lista de acordo com o tamanho da matrix de entrada
    rows = m.shape[0]
    columns = m.shape[1]

    answer = np.zeros(rows) # Populando com zeros a matrix de resposta

    # print "Matrix de entrada"
    # print m
    # print "-----------------------------------------"

    for i in np.arange(0,columns):
        for j in np.arange(i+1,rows):
            tmp = m[i] * (-m[j][i] / m[i][i])
            m[j] = tmp + m[j]

    for i in (np.arange(rows).shape[0] - np.arange(rows) -1):

        if i < columns-2:
            m[i][columns-1] = m[i][columns-1] - (sum(m[i]) - m[i][i] - m[i][columns-1])

        answer[i] = m[i][columns-1] / (m[i][i])
        for j in np.arange(0,i):
            m[j][i] = m[j][i]*answer[i]

    #reposta
    return answer


def main():
    m = np.array([[1, -1., -1., 0.],
                  [4., 1., 0., 8.],
                  [0., -1., 4., 16.]])

    # m = np.array([[5., 5., 0., 15.],
    #               [2., 4., 1., 10.],
    #               [3., 4., 0., 11.]])
    print gauss(m)


if __name__ == "__main__":
    main()
