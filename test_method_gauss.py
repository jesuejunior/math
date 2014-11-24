import unittest
from method_gauss import gauss
import numpy as np
__author__ = 'jesuejunior'

class MethodGaussTest(unittest.TestCase):

    def test_method_gauss_ok(self):

        matrix = np.array([[0.5, -1., 1., 6.],
                           [3., 2., 1., 8.],
                           [5., -1., -3., -1.]])

        expected = np.array([2., -1., 4.])

        result = gauss(matrix)

        assert np.all(result == expected)

    def test_method_gauss_aula(self):

        matrix = np.array([[1, -1., -1., 0.],
                           [4., 1., 0., 8.],
                           [0., -1., 4., 16.]])

        expected = np.array([3.666, -1.3333, 2.333])

        result = gauss(matrix)

        assert np.all(result == expected)