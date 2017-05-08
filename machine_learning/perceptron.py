from numpy import array, dot, random
import unittest
from matplotlib.pyplot import plot, show


class Perceptron(object):
    def __init__(self):
        self.w = random.rand(2) * 2 - 1  # weight for a 2d problem
        self.eta = 0.1
        self.errors = []  # Save to graph errors
        pass

    def __unit_step(self, x):
        result = dot(self.w, x)
        if (result < 0):
            return 0
        else:
            return 1

    def update_weight(self, x, delta_error):
        self.w[0] += self.eta * delta_error * x[0]
        self.w[1] += self.eta * delta_error * x[1]

    def train(self, training_data):
        """
        Trains off of training_data, must be array w/3 elements.
        3rd element is expected output.
        """
        learned = False
        i = 0
        delta_error = 0.0
        while not (learned or i >= 100):
            for x in training_data:
                r = self.__unit_step(x)
                if x[2] != r:
                    delta_error = x[2] - r
                    self.update_weights(x, delta_error)
                    delta_error = abs(delta_error)
            i += 1
            if delta_error == 0.0:
                print 'Iterations: {}'.format(i)
                learned = True
#        ylim([-1, 1])
#        plot(errors)


class PerceptronTest(unittest.TestCase):
    def setUp(self):
        self.or_data = [
            array([0, 0, 0]),
            array([0, 1, 1]),
            array([1, 0, 1]),
            array([1, 1, 1])
        ]

        self.nor_data = [
            array([0, 0, 0]),
            array([0, 1, 0]),
            array([1, 0, 0]),
            array([1, 1, 1])
        ]

        self.and_data = [
            array([0, 0, 0]),
            array([0, 1, 0]),
            array([1, 0, 0]),
            array([1, 1, 1])
        ]

        self.nand_data = [
            array([0, 0, 1]),
            array([0, 1, 1]),
            array([1, 0, 1]),
            array([1, 1, 0])
        ]

    def gen_data(self, n):
        x_a = (random.rand(n)*2-1)/2-0.5
        x_b = (random.rand(n)*2-1)/2+0.5
        y_a = (random.rand(n)*2-1)/2+0.5
        y_b = (random.rand(n)*2-1)/2-0.5
        data = []
        for i in xrange(n):
            data.append([x_a[i], y_a[i], 1])
            data.append([x_b[i], y_b[i], -1])
        return data

    def test_perceptron(self):
        perceptron = Perceptron()
        perceptron.run_perceptron(self.training_data)

if __name__ == '__main__':
    unittest.main()
