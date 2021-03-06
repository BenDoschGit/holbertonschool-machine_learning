#!/usr/bin/env python3
"""Module containing the function test_model.
"""

import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """Function that tests a neural network.

    Args:
        network (keras.Model): The network model to test.
        data (tensor): The input data to test the model with.
        labels (tensor): The correct one-hot labels of data.
        verbose (bool, optional): A boolean that determines if output should
            be printed during the testing process. Defaults to True.

    Returns:
        The loss and accuracy of the model with the testing data, respectively.
    """
    return network.evaluate(
        x=data,
        y=labels,
        verbose=verbose
    )
