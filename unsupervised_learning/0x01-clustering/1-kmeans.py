#!/usr/bin/env python3
"""Module that contains the function kmeans that performs K-means on a
dataset."""

import numpy as np


def kmeans(X, k, iterations=1000):
    """Function that performs K-means on a dataset.

    Args:
        X (numpy.ndarray): A tensor of shape (n, d) containing the dataset,
            where n is the number of data points and d is the number of
            dimensions for each data point.
        k (int): The number of clusters.
        iterations (int, optional): The maximum number of iterations that
            should be performed. Defaults to 1000.

    Returns:
        C (numpy.ndarray) A tensor of shape (k, d) containing the centroid
            means for each cluster.
        clss (numpy.ndarray) A tensor of shape (n,) containing the index of
            the cluster in C that each data point belongs to.
        None, None on failure.
    """
    if (not isinstance(X, np.ndarray) or not isinstance(k, int) or k <= 0 or
            len(X.shape) != 2 or k > X.shape[0] or
            not isinstance(iterations, int) or iterations <= 0):
        return None, None

    # Initialize centroids
    n, d = X.shape
    low = X.min(axis=0)
    high = X.max(axis=0)
    centroids = np.random.uniform(low=low, high=high, size=(k, d))

    for i in range(iterations):
        # Calculate distance between centroids and data points
        diffrence = (X - centroids[:, None, :])  # (k, n, d)
        dist = np.linalg.norm(diffrence, axis=2).T  # (n, k)
        # Seperate into clusters
        clss = np.argmin(dist, axis=1)
        labeled = np.concatenate((X.copy(), np.reshape(clss, (n, 1))), axis=1)

        # Calculate the means of each cluster
        C = np.empty((k, d))
        for j in range(k):
            temp = labeled[labeled[:, -1] == j]
            temp = temp[:, :d]
            if temp.size == 0:
                re_init = np.random.uniform(low=low, high=high, size=(1, d))
                C[j] = re_init
            else:
                C[j] = np.mean(temp, axis=0)
        # Recalculate clss
        clss = np.argmin(np.linalg.norm((X - C[:, None, :]), axis=2).T, axis=1)

        # Check for change
        if np.array_equal(centroids, C):
            break

        # Assign new centroids
        centroids = C

    return C, clss


if __name__ == "__main__":
    """matplotlib.pyplot as plt

    np.random.seed(0)
    a = np.random.multivariate_normal([30, 40], [[16, 0], [0, 16]], size=50)
    b = np.random.multivariate_normal([10, 25], [[16, 0], [0, 16]], size=50)
    c = np.random.multivariate_normal([40, 20], [[16, 0], [0, 16]], size=50)
    d = np.random.multivariate_normal([60, 30], [[16, 0], [0, 16]], size=50)
    e = np.random.multivariate_normal([20, 70], [[16, 0], [0, 16]], size=50)
    X = np.concatenate((a, b, c, d, e), axis=0)
    np.random.shuffle(X)
    C, clss = kmeans(X, 5)
    print(C)
    plt.scatter(X[:, 0], X[:, 1], s=10, c=clss)
    plt.scatter(C[:, 0], C[:, 1], s=50, marker='*', c=list(range(5)))
    plt.show()"""

    np.random.seed(1)
    a = np.random.multivariate_normal([30, 40], [[16, 0], [0, 16]], size=50)
    b = np.random.multivariate_normal([10, 25], [[16, 0], [0, 16]], size=50)
    c = np.random.multivariate_normal([40, 20], [[16, 0], [0, 16]], size=50)
    d = np.random.multivariate_normal([60, 30], [[16, 0], [0, 16]], size=50)
    e = np.random.multivariate_normal([20, 70], [[16, 0], [0, 16]], size=50)
    X = np.concatenate((a, b, c, d, e), axis=0)
    np.random.shuffle(X)
    C, clss = kmeans(X, 5, iterations=1)
    print(C)
    print(clss)
    C, clss = kmeans(X, 5, iterations=5)
    print(C)
    print(clss)
