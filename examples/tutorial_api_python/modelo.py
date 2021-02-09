import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score, validation_curve, learning_curve
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Ridge
import random, math

random.seed(1235)
datos = pd.read_csv('D:\mat\output_jsons\csvxx.csv')
# print(datos.info())
# print(datos[:10])

body_parts = ["Nose.x", "Nose.y", "Nose.confidence","Neck.x","Neck.y","Neck.confidence","RShoulder.x","RShoulder.y","RShoulder.confidence","RElbow.x","RElbow.y","RElbow.confidence","RWrist.x","RWrist.y","RWrist.confidence",
            "LShoulder.x", "LShoulder.y", "LShoulder.confidence","LElbow.x","LElbow.y","LElbow.confidence","LWrist.x","LWrist.y","LWrist.confidence","MidHip.x","MidHip.y","MidHip.confidence","RHip.x","RHip.y","RHip.confidence",
    "RKnee.x","RKnee.y","RKnee.confidence","RAnkle.x","RAnkle.y","RAnkle.confidence","LHip.x","LHip.y","LHip.confidence","LKnee.x","LKnee.y","LKnee.confidence","LAnkle.x","LAnkle.y","LAnkle.confidence","REye.x","REye.y","REye.confidence",
    "LEye.x","LEye.y","LEye.confidence","REar.x","REar.y","REar.confidence","LEar.x","LEar.y","LEar.confidence","LBigToe.x","LBigToe.y","LBigToe.confidence","LSmallToe.x","LSmallToe.y","LSmallToe.confidence",
    "LHeel.x","LHeel.y","LHeel.confidence","RBigToe.x","RBigToe.y","RBigToe.confidence","RSmallToe.x","RSmallToe.y","RSmallToe.confidence","RHeel.x","RHeel.y", "RHeel.confidence"]
    
X = datos[['LAnkle.x','LAnkle.y', 'LHip.x','LHip.y','RAnkle.x','RAnkle.y', 'RHip.x','RHip.y'  ,'MidHip.x', 'MidHip.y', 'LSmallToe.x',  'LSmallToe.y',  'RSmallToe.x',  'RSmallToe.y','RBigToe.x',  'RBigToe.y',  'RBigToe.x',  'RBigToe.y']]

y = datos[['LKnee.x','LKnee.y','RKnee.x','RKnee.y']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.8, random_state = 0)

# create dataset
# summarize shape
# print(X, y)

# train model
clf = MultiOutputRegressor(Ridge(random_state=123)).fit(X_train, y_train)
# print(X)

#predict
y_pred = clf.predict(X_test)

#check prediction
# print(clf.score(X_test,y_test))

X_prueba = X_test[1:2]
y_mal= [[1224.82,  850.098,  1150.98,  860.599]]
y_bien=[[1424.82,  777.098,  1398.98,  803.599]]

# print(y_mal[0][0])

DIST = np.linalg.norm(np.array(y_mal)-np.array(y_bien), axis=1) / np.linalg.norm(np.array(y_mal))
# print(type(y_mal))
# print('distance : ', DIST[0]*100, ' %')
# print(np.array(y_mal)-np.array(y_bien))
# print(np.linalg.norm(np.array(y_mal)-np.array(y_bien), ord='nuc'))
# print(np.linalg.norm(np.array(y_mal)-np.array(y_bien)))


def bien_o_mal(pred, real):
    type(pred)
    dist = np.linalg.norm(np.array(pred)-np.array(real), axis=1) / np.linalg.norm(np.array(pred))
    # DIST = np.linalg.norm(np.array(y_mal)-np.array(y_bien), axis=1) / np.linalg.norm(np.array(y_mal))
    # print('distance : ', DIST[0]*100, ' %')
    print(dist[0]*100)
    print(pred)
    print(real)

    return "Bien" if dist[0]*100 < 5  else "mal" 


y_pred = clf.predict(X_prueba)
#print(bien_o_mal(y_pred,y_bien))
print(bien_o_mal(y_pred,y_mal))
print(clf.score(X_prueba,y_bien))

# print('\nBITE', y_test[0:2])



