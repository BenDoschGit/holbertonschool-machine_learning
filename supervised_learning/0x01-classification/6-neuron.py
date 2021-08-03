#!/usr/bin/env python3
"""Module containing the class Neuron which defines a single neuron performing
binary classification"""

import numpy as np
from numpy.core.fromnumeric import shape


class Neuron():
    """Class which defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        """Initizilation function for Neuron

        Args:
            nx (int): The number of input features to the neuron
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        else:
            self.__W = np.random.randn(1, nx)
            self.__b = 0
            self.__A = 0

    @property
    def W(self):
        """Getter for private instance atribute W.

        Returns:
            [float]: The weights vector for the neuron.
        """
        return self.__W

    @property
    def b(self):
        """Getter for private instance atribute b

        Returns:
            [float]: The bias for the neuron.
        """
        return self.__b

    @property
    def A(self):
        """Getter for private instance atribute

        Returns:
            [numpy.ndarray]: The activated output of the neuron.
        """
        return self.__A

    def forward_prop(self, X):
        """Function that calculates the forward propagation of the neuron.
        Uses Logistic Regresssion.

        Args:
            X (numpy.ndarray): N-dimensional array with the shape (nx, m) that
                contains the input data, where nx is the number of input
                features to the neuron and m is the number of examples.

        Returns:
            [float]: The activated output of the neuron (self.__A).
        """
        z = np.dot(self.W, X) + self.b
        self.__A = 1/(1 + np.exp(-z))  # Sigmoid
        return self.__A

    def cost(self, Y, A):
        """Function that alculates the cost of the model using
            logistic regression

        Args:
            Y (numpy.ndarray): N-dimensional array with shape (1, m) that
                contains the correct labels for the input data.
            A (numpy.ndarray): N-dimensioal array with shape (1, m) containing
                the activated output of the neuron for each example.
                Sometiems refered to as "y hat" a y with a "^" above it.
        """
        shape = np.shape(Y)
        m = shape[1]
        cost_array = -((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A)))
        return np.sum(cost_array) / m

    def evaluate(self, X, Y):
        """Function that valuates the neuron’s predictions.

        Args:
            X (numpy.ndarray): N-dimensioal array with shape (nx, m) that
                contains the input data, where nx is the number of input
                features to the neuron and m is the number of examples.
            Y (numpy.ndarray): N-dimensioal array with shape (1, m) that
                contains the correct labels for the input data.

        Returns:
            A (numpy.ndarray): The neuron’s prediction. The predictions shape
                will be (1, m), containing the predicted labels for each
                example.
            cost (float): The cost of the network.

        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        A = np.where(A >= 0.5, 1, 0)
        return A, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Function that calculates one pass of gradient descent on the neuron.

        Args:
            X (numpy.ndarray): N-dimensioal array with shape (nx, m) that
                contains the input data, where nx is the number of input
                features to the neuron and m is the number of examples.
            Y (numpy.ndarray): N-dimensioal array with shape (1, m) that
                contains the correct labels for the input data.
            A (numpy.ndarray): N-dimensioal array with shape (1, m) that
                contains the activated output of the neuron for each example.
            alpha (float, optional): The learning rate. Defaults to 0.05.
        """
        shape = X.shape
        m = shape[1]
        dZ = A - Y
        dW = (np.matmul(X, dZ.T) / m).T
        db = np.sum(dZ) / m
        W = self.W - (alpha * dW)
        b = self.b - (alpha * db)
        self.__W = W
        self.__b = b

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Function that trains the neuron

        Args:
            X (numpy.ndarray): N-dimensioal array with shape (nx, m) that
                contains the input data, where nx is the number of input
                features to the neuron and m is the number of examples.
            Y (numpy.ndarray): N-dimensioal array with shape (1, m) that
                contains the correct labels for the input data.
            iterations (int, optional): The number of iterations to train over.
                Defaults to 5000.
            alpha (float, optional): The learning rate. Defaults to 0.05.

        Returns:
            A (numpy.ndarray): The neuron’s prediction after iterations of
                training has occured. The predictions shape will be (1, m),
                containing the predicted labels for each example.
            cost (float): The cost of the network after iterations of
                training has occured.

        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        elif iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        elif not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        elif alpha <= 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            A = self.forward_prop(X)
            self.gradient_descent(X, Y, A)

        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        A = np.where(A >= 0.5, 1, 0)
        return A, cost
