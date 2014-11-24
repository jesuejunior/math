from math import exp, pow

__author__ = 'jesuejunior'


def raizEx():

	xi1,xi,erro = 0., 0.5, 15.

	while(abs(erro) > pow(10.0, -8.0)):
		xi1 = xi - func(xi)/derivada(xi)

		erro = xi1 - xi

		print "{0} {1}   {2} ".format(xi, xi1, erro)

		xi = xi1


def derivada(xi):
	#Return e**x - 1
	return -(exp(-xi)) -1


def func(xi):
	return exp(-xi) - xi

#Feito JJ
def newton_raphson(f, f_, x0, TOL=0.001, NMAX=10000):
	n = 1
	while n <= NMAX:
		x1 = x0 - (f(x0)/f_(x0))
		if x1 - x0 < TOL:
			return x1
		else:
			x0 = x1
	return False

#funcao de X
def f(x):
	return exp(-x) - x

#derivada
def f_(x):
	return -(exp(-x)) - 1


def main():
	result = newton_raphson(f, f_, 0.5)
	print result

	print 'Aquino'
	raizEx()

if __name__ == '__main__':
	main()
