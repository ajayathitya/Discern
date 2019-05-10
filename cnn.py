from sklearn.neural_network import MLPClassifier
from sklearn import *
from sklearn.metrics import *
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mnist import MNIST

emnist_data = MNIST(path='gzip\\', return_type='numpy')
emnist_data.select_emnist('bymerge')
x_orig, y_orig = emnist_data.load_training()

x_train = x_orig[0:1000, :]
Y = y_orig.reshape(y_orig.shape[0], 1)
Y = Y[0:1000, :]
Y = Y[:, 0]
y_train = (np.arange(np.max(Y) + 1) == Y[:, None]).astype(int)

X_test = x_orig[1000:1200, :]
Y_test = y_orig.reshape(y_orig.shape[0], 1)
Y_test = Y_test[1000:1200, :]
Y_test = Y_test[:, 0]

img = x_train[59]

# visualize image
plt.imshow(img[0], cmap='gray')