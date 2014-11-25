# -*- coding: utf-8 -*-
import pylab
import numpy as np

__author__ = 'jesuejunior'

def minimo_quadrado(x, y, n, al=0, a0=0, syx=0, r2=0):
	somax = somay = somaxy = somax2 = st = sr = 0

	for i in range(n):
		somax = somax + x[i]
		somay = somay + y[i]
		somaxy = somaxy + x[i] * y[i]
		somax2 = somax2 + x[i] * x[i]

	xm = somax/n
	ym = somay/n
	al = (n*somaxy - somax*somay)/(n*somax2 - somax*somax)
	a0 = ym - al*xm

	for i in range(n):
		st = st + ((y[i] - ym)**2)
		sr = sr + ((y[i] - al*x[i] - a0)**2)

	syx = (sr/(n-2))**0.5
	r2 = (st - sr)/st

	line = [0.9107142857142855, 1.7499999999999998, 2.589285714285714, 3.4285714285714284, 4.267857142857142, 5.107142857142857, 5.946428571428571]

	pylab.grid(True)
	pylab.plot(x, y, 'ks', line, line, 'r-', lw=2)
	pylab.scatter(x, y, s=20, marker='o', c='b')
	pylab.title('Minimos quadrados')
	pylab.xlabel('X')
	pylab.ylabel('Y')
	pylab.savefig('result.png')
	pylab.show()


def main():
	y = [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5]
	x = [1, 2, 3, 4, 5, 6, 7]

	minimo_quadrado(x, y, len(x))


if __name__ == '__main__':
	main()