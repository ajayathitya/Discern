from sklearn.neural_network import MLPClassifier
from sklearn import *
from sklearn.metrics import *
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mnist import MNIST

emnist_data = MNIST(path='gzip\\', return_type='numpy')
emnist_data.select_emnist('letters')
x_orig, y_orig = emnist_data.load_training()

train_x = x_orig[0:3000, :]
Y = y_orig.reshape(y_orig.shape[0], 1)
Y = Y[0:3000, :]
Y = Y[:, 0]
train_y = (np.arange(np.max(Y) + 1) == Y[:, None]).astype(int)

X_test = x_orig[3000:3500, :]
Y_test = y_orig.reshape(y_orig.shape[0], 1)
Y_test = Y_test[3000:3500, :]
Y_test = Y_test[:, 0]

a = train_x[90]
print(a)
a = a.reshape(28,28)
print("----------------------------")
print(a)
plt.imshow(a,cmap='gray')
plt.show()