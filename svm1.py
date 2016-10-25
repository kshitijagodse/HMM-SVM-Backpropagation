# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:45:19 2016

@author: Kshitija
"""
from __future__ import division
import numpy as np

import matplotlib.pyplot as plt
from random import randint
import math
import numpy as np
from sklearn.svm import SVC
#def safe_ln(x, minval=0.0000000001):
#    return np.log(x.clip(min=minval))
fileP = open("nnsvm-data.txt","rU")
temp = [r.split(' ')  for r in fileP.read().split('\n')]
#print temp
dataPoints = [[]]
#del(temp[100])
dataPoints =  [ [float(t[0]),float(t[1])] for t in temp]
label=[float(t[2]) for t in temp]
#print dataPoints
#print label
X=np.array(dataPoints)
print "--------------------INPUT DATA---------------------------------------------"
print X
print X[0]
y=np.array(label)
print y

def square(X):
    return map(lambda x: x ** 2, X)
X_sqr= square(X)
print "Transformed Input"
for i in range(len(X_sqr)):
    print X_sqr[i]


clf = SVC(kernel='linear')
clf.fit(X_sqr, y)

 # get the separating hyperplane
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
print "--------------------------------------------------"
print "Slope Value"
print a
print "Intercept Value"
print (clf.intercept_[0]) / w[1]
print "--------------------------------------------------"
#print eq
yy = a * xx - (clf.intercept_[0]) / w[1]
eq = np.multiply(a,X_sqr) - (clf.intercept_[0]) / w[1]
print "Equation of line"
print eq
# plot the parallels to the separating hyperplane that pass through the
# support vectors

b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])
print "Support Vectors"
print clf.support_vectors_
print "Pre-images"
l = clf.support_
for i in l:
    
    print X[i]
#print clf.support_vectors_
#print clf.support_vectors_[:, 1]
#plt.plot(xx, yy, 'k-')
#plt.plot(xx, yy_down, 'k--')
#plt.plot(xx, yy_up, 'k--')
#
#plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
#            s=80, facecolors='none')
#plt.scatter(X[:, 0], X[:, 1], cmap=plt.cm.Paired)
#i = 0
#for row in X_sqr:
#    x = row[0]
#    y = row[1]
#    plt.scatter(x, y, c=y[i])
#    i += 1
#
#plt.axis('tight')
##print clf.support_
#
##print clf.get_params(True)
#plt.show()

#plt.clf()