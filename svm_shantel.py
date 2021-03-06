import pandas as pd
import numpy as np

from sklearn import preprocessing, cross_validation, svm


from sklearn.svm import SVC
from sklearn import metrics
from sklearn.utils import shuffle


# df = pd.read_csv('shantel.csv')

df = pd.read_csv('labeled_shantel.csv')
df =  shuffle(df)

array = df.values
X = array[:,0:6]
Y = array[:,6]



X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size = 0.3)

# Training
clf = SVC(probability=True)
clf.fit(X_train,y_train)




# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)

ypred=clf.predict(X_test)
print(print(metrics.accuracy_score(y_test,ypred)))
print(metrics.confusion_matrix(y_test,ypred))
print(metrics.classification_report(y_test,ypred))

# print(clf.predict_proba([[17,29,23,40,94,69]]))
# print(clf.predict([[19,48,26,17,95,63]]))
# print(clf.predict([[19,14,10,25,62,41]]))



#
# print(clf.predict_proba([[17,	29,	23,	26,	95,	67]]))
# print(clf.predict_proba([[18,	30,	23,	38,	95,	67]]))
# print(clf.predict_proba([[18,	30,	23,	35,	97,	68]]))
# print(clf.predict_proba([[15,	33,	24,	23,	94,	23]]))
# print(clf.predict_proba([[18,	30,	24,	34,	95,	68]]))
# print(clf.predict_proba([[14,	32,	25,	28,	90,	61]]))
# print(clf.predict_proba([[19,	30,	24,	34,	89,	61]]))
# print(clf.predict_proba([[21,	35,	27,	14,	85,	48]]))
# print(clf.predict_proba([[17,	30,	23,43,100,75]]))


# forecast_prediction = clf.predict(X_forecast)
# print(forecast_prediction)
