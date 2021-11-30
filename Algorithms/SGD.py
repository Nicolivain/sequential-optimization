"""
This file contains functions for gradient descent algorithm applied at the SVM problem
"""
import random as rd
import numpy as np


def sgd(model, X, y, lr, epoch, l, verbose=0):
    """
        Gradient descent algorithms applied with the CO pb il loss and uses tjhe gradloss function to update parameters
        :param X: (nxm) data
        :param y: (n)  labels
        :param lr: (float) learning rate
        :param epoch: (int) maximum number of iteration of the algorithm
        :param l:  (float) regularization parameter (lambda)
        :param verbose: (int) print epoch results every n epochs
        """

    losses = []
    wts = [model.w]
    n, _ = X.shape
    for i in range(epoch):

        # sample
        idx = rd.randint(0, n)
        sample_x = X[idx, :].reshape(1, -1)
        sample_y = np.array(y[idx])  # need an array for compatibility

        # update the last xt
        new_wts = wts[-1] - lr * model.gradLoss(sample_x, sample_y, l)
        model.w = new_wts
        wts.append(new_wts)

        # loss
        current_loss = model.loss(X, y, l)
        losses.append(current_loss)

        if verbose > 0 and i % verbose == 0:
            print("Epoch {:3d} : Loss = {:1.4f}".format(i, current_loss))

    # update wts:
    model.w = np.mean(wts)
    return losses