#-*- coding:utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
import numpy as np

#DictVectorizer将python字典对象转为向量
vec = DictVectorizer()
measurements = [
    {'city': 'Dubai', 'temperature': 33.},
    {'city': 'London', 'temperature': 12.},
    {'city': 'San Fransisco', 'temperature': 18.},
]
vector = vec.fit_transform(measurements)
print vector.toarray()
print vec.get_feature_names()

#StandardScaler特征标准化
print "StandardScaler特征标准化"
scaler = preprocessing.StandardScaler()
scaler.fit(vector.toarray())
print scaler
print scaler.mean_
print scaler.scale_
print scaler.var_
X = np.array([[ 1., -1., 1.0,  -2.],
    [ 2.,  0., 1.0,  0.],
    [ 0.,  1., 1.0, 1.]])
print type(X)
print type(vector.toarray())
print scaler.transform(X)

#特征缩放
print "特征缩放minMaxScaler"
minMaxScaler = preprocessing.MinMaxScaler()
Y = minMaxScaler.fit_transform(X)
print minMaxScaler.data_min_
print minMaxScaler.data_max_
print Y
print minMaxScaler.transform(X)
print "特征缩放maxAbsScaler"
maxAbsScaler = preprocessing.MaxAbsScaler()
Y = maxAbsScaler.fit_transform(X)
print maxAbsScaler.scale_
print Y
print maxAbsScaler.transform(X)