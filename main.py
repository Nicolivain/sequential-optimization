"""
Sorbonne University
Master M2A
Convex sequential Optimization
Olivain Nicolas
Liautaud Paul
Le Boudec Lise

Main file 
""" 

import numpy as np
import pandas as pd
import pathlib as Path

from Algorithms.GD import GradientDescent, projected_gd
from Algorithms.SGD import sgd, projected_sgd
from Models.LinearSVM import LinearSVM
from utils import *


# --- PARAMETERS ---

lr          = 0.0001
nepoch      = 51
lbd         = 1
z           = 10
verbose     = 1

alg_to_run = ['gd', 'c_gd', 'sgd', 'c_sgd']
# alg_to_run = ['c_sgd']



############################### Read and prepare data ###############################

mnist_train=pd.read_csv('mnist_train.csv', sep=',', header=None)  # Reading
train_data = mnist_train.values[:, 1:]                               # Extract data
train_data = train_data / np.max(train_data)                         # Normalize data
train_labels = mnist_train.values[:, 0]                              # Extract labels
train_labels[np.where(train_labels != 0)] = -1                       # if labels is not 0 => -1 (Convention chosen)
train_labels[np.where(train_labels == 0)] = 1                        # if label is 0 ==> 1

mnist_test=pd.read_csv('mnist_test.csv', sep=',', header=None)
test_data = mnist_test.values[:, 1:]
test_data = test_data / np.max(test_data)
test_labels = mnist_test.values[:, 0]
test_labels[np.where(test_labels != 0)] = -1
test_labels[np.where(test_labels == 0)] = 1

n, m = train_data.shape

############################### Test algorithms ###############################

# Unconstrained GD

if 'gd' in alg_to_run:
    model = LinearSVM(m)
    GDloss = GradientDescent(model, train_data, train_labels, lr, nepoch, lbd, verbose)
    pred_test_labels = model.predict(test_data)
    GDacc = accuracy(test_labels, pred_test_labels)
    print('After {:3d} epoch, Unconstrained GD algorithm has a loss of {:1.6f} and accuracy {:1.6f}'.format(nepoch, GDloss[-1], GDacc))


# Constrained GD: projection on B1(z)

if 'c_gd' in alg_to_run:
    model = LinearSVM(m)
    GDloss = projected_gd(model, train_data, train_labels, lr, nepoch, lbd, z, verbose)
    pred_test_labels = model.predict(test_data)
    GDacc = accuracy(test_labels, pred_test_labels)
    print('After {:3d} epoch, constrained GD (radius {:2d} algorithm has a loss of {:1.6f} and accuracy {:1.6f}'.format(nepoch, z, GDloss[-1], GDacc))

# Unconstrained SGD

if 'sgd' in alg_to_run:
    model = LinearSVM(m)
    loss = sgd(model, train_data, train_labels, lr, nepoch, lbd, verbose)
    pred_test_labels = model.predict(test_data)
    acc = accuracy(test_labels, pred_test_labels)
    print('After {:3d} epoch, Unconstrained SGD algorithm has a loss of {:1.6f} and accuracy {:1.6f}'.format(nepoch, loss[-1], acc))

# Projected SGD

if 'c_sgd' in alg_to_run:
    model = LinearSVM(m)
    loss = projected_sgd(model, train_data, train_labels, lr, nepoch, lbd, z, verbose)
    pred_test_labels = model.predict(test_data)
    print(test_labels)
    print(pred_test_labels)
    acc = accuracy(test_labels, pred_test_labels)
    print('After {:3d} epoch, constrained SGD algorithm has a loss of {:1.6f} and accuracy {:1.6f}'.format(nepoch, loss[-1], acc))
