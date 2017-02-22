from random import choice
from numpy import array, dot, random
# from pylab import plot, ylim
import unittest


class Perceptron(object):
    def __init__(self):
        pass

    def __unit_step(self, x):
        if (x < 0):
            return 0
        else:
            return 1

    def run_perceptron(self, training_data):

        errors = []
        eta = 0.2
        n = 100
        vector_length = len(training_data[0][0])
        w = random.rand(vector_length)

        for _ in xrange(n):
            x, expected = choice(training_data)
            result = dot(w, x)
            error = expected - self.__unit_step(result)
            errors.append(error)
            w += eta * error * x

        for x, _ in training_data:
            result = dot(x, w)
            print("{}: {} -> {}".format(x[:2], result, self.__unit_step(result)))

#        ylim([-1, 1])
#        plot(errors)


class PerceptrionTest(unittest.TestCase):
    def setUp(self):
        self.training_data = [
            (array([0, 0, 1]), 0),
            (array([0, 1, 1]), 1),
            (array([1, 0, 1]), 1),
            (array([1, 1, 1]), 1)
        ]

    def test_perceptrion(self):
        perceptron = Perceptron()
        perceptron.run_perceptron(self.training_data)
if __name__ == '__main__':
    unittest.main()
