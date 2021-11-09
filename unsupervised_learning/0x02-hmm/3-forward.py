#!/usr/bin/env python3
"""Module that containst the function forward that performs the forward
algorithm for a hidden markov model."""

import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """Function that performs the forward algorithm for a hidden markov model.

    Args:
        Observation (numpy.ndarray): A tensor of shape (T,) that contains the
            index of the observation, where T is the number of observations.
        Emission (numpy.ndarray): A tensor of shape (N, M) containing the
            emission probability of a specific observation given a hidden
            state, where Emission[i, j] is the probability of observing j given
            the hidden state i, N is the number of hidden states, and M is the
            number of all possible observations.
        Transition (numpy.ndarray): A tensor of shape (N, N) containing the
            transition probabilities, where Transition[i, j] is the probability
            of transitioning from the hidden state i to j.
        Initial (numpy.ndarray): A tensor of shape (N, 1) containing the
            probability of starting in a particular hidden state.

    Returns:
        P (float): The likelihood of the observations given the model.
        F (numpy.ndarray): A tensor of shape (N, T) containing the forward path
            probabilities, where F[i, j] is the probability of being in hidden
            state i at time j given the previous observations.
        None, None on failure.
    """
    P = None
    F = None
    return P, F


if __name__ == "__main__":
    np.random.seed(1)
    Emission = np.array([[0.90, 0.10, 0.00, 0.00, 0.00, 0.00],
                         [0.40, 0.50, 0.10, 0.00, 0.00, 0.00],
                         [0.00, 0.25, 0.50, 0.25, 0.00, 0.00],
                         [0.00, 0.00, 0.05, 0.70, 0.15, 0.10],
                         [0.00, 0.00, 0.00, 0.20, 0.50, 0.30]])
    Transition = np.array([[0.60, 0.39, 0.01, 0.00, 0.00],
                           [0.20, 0.50, 0.30, 0.00, 0.00],
                           [0.01, 0.24, 0.50, 0.24, 0.01],
                           [0.00, 0.00, 0.15, 0.70, 0.15],
                           [0.00, 0.00, 0.01, 0.39, 0.60]])
    Initial = np.array([0.05, 0.20, 0.50, 0.20, 0.05])
    Hidden = [np.random.choice(5, p=Initial)]
    for _ in range(364):
        Hidden.append(np.random.choice(5, p=Transition[Hidden[-1]]))
    Hidden = np.array(Hidden)
    Observations = []
    for s in Hidden:
        Observations.append(np.random.choice(6, p=Emission[s]))
    Observations = np.array(Observations)
    P, F = forward(
        Observations, Emission, Transition, Initial.reshape((-1, 1))
        )
    print(P)
    print(F)