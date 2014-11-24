__author__ = 'jesuejunior'

import numpy as np

a = np.array([[17., -2, -3.], [-5., 21., -2.], [-5., -5., 22.]])

b = np.array([500., 200., 30.])


def gausseidel():

	#aproximacaoo desejada\/
	x = np.array([34., 19., 13.])
	# x = np.zeros_like(b)
	for n in range(100):
		x_new = np.zeros_like(x)
		for i in range(a.shape[0]):
			s1 = np.dot(a[i, :i], x_new[:i])
			s2 = np.dot(a[i, i + 1:], x[i + 1:])
			x_new[i] = (b[i] - s1 - s2) / a[i, i]
		if np.allclose(x, x_new, rtol=0.0025):
			break
		x = x_new

	print "x0: {0}".format(x[0])
	print "x1: {0}".format(x[1])
	print "x2: {0}".format(x[2])




def main():
	gausseidel()

if __name__ == '__main__':
	main()
