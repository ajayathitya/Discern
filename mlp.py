from sklearn.neural_network import MLPClassifier
from sklearn import *
from sklearn.metrics import *
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mnist import MNIST

model = MLPClassifier(max_iter=250)

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

model.fit(train_x,train_y)
predictions = model.predict(X_test)

b=[]
for i in range(0,500):
    for j in range(0,27):
        if j==26:
            b.append(26)
            break
        if predictions[i][j]==1:
            b.append(j)
            break
            
print(accuracy_score(b,Y_test))
print(confusion_matrix(b,Y_test))