import sys, os
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid,softmax


def get_test_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


# load network parameter
def init_network(filename):
    with open(filename, 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    # get weight and biasing from network file
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # input ---> layer 1 ---> hidden layer1 with sigmoid function
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    # layer 1 ---> layer 2 ---> hidden layer2 with sigmoid function
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    # layer 2 ---> output layer ---> output after softmax function
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y


