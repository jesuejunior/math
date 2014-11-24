
import unittest
import numpy as np
from method_jacobi import jacobi


__author__ = 'jesuejunior'

class MethodJacobiTest(unittest.TestCase):

    def test_method_jacobi_ok(self):

        matrix_A = np.array([[10., -1., 2., 0.],
                           [-1., 11., -1., 3.],
                           [2., -1., 10., -1.],
                           [0., 3., -1., 8.]])

        matrix_B = np.array([6., 25., -11., 15.])

        expected = np.array([1., 2., -1., 1.])

        result = jacobi(matrix_A, matrix_B)

        assert np.all(result == expected)