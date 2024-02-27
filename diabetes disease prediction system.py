# -*- coding: utf-8 -*-
"""Multiple disease prediction system - diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GVQWb8SUa7EGTPvRB3NR6Rhgebk7EvhB

Importing the Dependencies
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
!pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
import missingno as msno

"""Data Collection and Analysis

PIMA Diabetes Dataset
"""

# loading the diabetes dataset to a pandas DataFrame
#diabetes_dataset = pd.read_csv('diabetes.csv')
from google.colab import drive
drive.mount('/content/drive')
diabetes_dataset = pd.read_csv('/content/drive/MyDrive/diabetes.csv')

# printing the first 5 rows of the dataset
diabetes_dataset.head()

# prompt: Using dataframe diabetes_dataset:

diabetes_dataset.hist()

# number of rows and Columns in this dataset
diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()

#count missing values
missing_counts = diabetes_dataset.isnull().sum()
print(missing_counts)

#Plotting Null Count Analysis Plot
p = msno.bar(diabetes_dataset)

#let’s check that how well our outcome column is balanced
color_wheel = {0: "blue", 1: "red"}
colors = diabetes_dataset["Outcome"].map(lambda x: color_wheel.get(x))
print(diabetes_dataset.Outcome.value_counts())
p = diabetes_dataset.Outcome.value_counts().plot(kind="bar")
plt.show()

"""0 --> Non-Diabetic

1 --> Diabetic
"""

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

#Calculate Correlation Matrix:
correlation_matrix = X.corr()
print(correlation_matrix)

# Calculate correlation matrix
plt.figure(figsize=(10,7))
sn.heatmap(correlation_matrix, annot=True)
plt.show()

print(X)

print(Y)

"""Train Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the Model"""

modelsvm = svm.SVC(kernel='rbf',gamma='scale')

#training the support vector Machine Classifier
modelsvm.fit(X_train, Y_train)

"""**Model Evaluation and Accuracy Score**"""

# accuracy score on the training data of support vector Machine Classifier
X_train_prediction = modelsvm.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data SVM: ', training_data_accuracy)

# accuracy score on the test data of support vector Machine Classifier
X_test_prediction = modelsvm.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data SVM : ', test_data_accuracy)

cmSVM = confusion_matrix(Y_test, X_test_prediction)
cmSVM

plt.figure(figsize=(7,5))
sn.heatmap(cmSVM, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Calculate precision
precision = precision_score(Y_test, X_test_prediction)
print(f"Precision for your SVM model:",precision)

# Calculate recall
recall = recall_score(Y_test, X_test_prediction)
print(f"recall for your SVM model:",recall)

# Calculate f1_score
f1 = f1_score(Y_test, X_test_prediction)
print("f1_score for your SVM model:",f1)

# SVm model performance using cross_val_score
cross_val_score(SVC(gamma='auto'), X, Y,cv=3)

"""**Training the Model Decision tree Classifier**"""

modelDT = tree.DecisionTreeClassifier(criterion="entropy", max_depth=4)
modelDT.fit(X_train, Y_train)
#training the Decition tree Classifier
#model.score(inputs_n,target)
# accuracy score on the training data
X_train_prediction = modelDT.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data DT: ', training_data_accuracy)

"""**Model Evaluation Accuracy Score**"""

# accuracy score on the test data of Decition tree Classifier
X_test_prediction = modelDT.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data DT: ', test_data_accuracy)

cmDT = confusion_matrix(Y_test, X_test_prediction)
cmDT

plt.figure(figsize=(7,5))
sn.heatmap(cmDT, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Calculate precision
precision = precision_score(Y_test, X_test_prediction)
print(f"Precision for your DT model:",precision)

# Calculate recall
recall = recall_score(Y_test, X_test_prediction)
print(f"recall for your DT model:",recall)

# Calculate f1_score
f1 = f1_score(Y_test, X_test_prediction)
print("f1_score for your DT model:",f1)

# Decision tree model performance using cross_val_score
cross_val_score(DecisionTreeClassifier(max_depth=40), X, Y, cv=3)

"""**training the Logistic Regression**"""

modelLR = LogisticRegression()
#training the Logistic Regression
modelLR.fit(X_train, Y_train)
# accuracy score on the training data
#model.score(X_test,y_test)
#y_predicted = model.predict(X_test)
#model.predict_proba(X_test)
X_train_prediction = modelLR.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data LR: ', training_data_accuracy)

# accuracy score on the test data of Logistic Regression
X_test_prediction = modelLR.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data LR: ', test_data_accuracy)

cmLR = confusion_matrix(Y_test, X_test_prediction)
cmLR

plt.figure(figsize=(7,5))
sn.heatmap(cmLR, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Calculate precision
precision = precision_score(Y_test, X_test_prediction)
print(f"Precision for your LR model:",precision)

# Calculate recall
recall = recall_score(Y_test, X_test_prediction)
print(f"recall for your LR model:",recall)

# Calculate f1_score
f1 = f1_score(Y_test, X_test_prediction)
print("f1_score for your LR model:",f1)

#Logistic regression model performance using cross_val_score
cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'), X, Y,cv=3)

"""**training the K_Nereast_Neighbors  Classifier**"""

modelKNN = KNeighborsClassifier(n_neighbors=10)
modelKNN.fit(X_train, Y_train)
#training the K_Nereast_Neighbors  Classifier
#knn.score(X_test, Y_test)
X_train_prediction = modelKNN.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data KNN : ', training_data_accuracy)

# accuracy score on the test data ofK_Nereast_Neighbors  Classifier
X_test_prediction = modelKNN.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data KNN : ', test_data_accuracy)

cmKNN = confusion_matrix(Y_test, X_test_prediction)
cmKNN

plt.figure(figsize=(7,5))
sn.heatmap(cmKNN, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Calculate precision
precision = precision_score(Y_test, X_test_prediction)
print(f"Precision for your KNN model:",precision)

# Calculate recall
recall = recall_score(Y_test, X_test_prediction)
print(f"recall for your KNN model:",recall)

# Calculate f1_score
f1 = f1_score(Y_test, X_test_prediction)
print("f1_score for your KNN model:",f1)

#K_ Nearest Neighbors model performance using cross_val_score
cross_val_score(KNeighborsClassifier(n_neighbors=5), X, Y, cv=3)

"""**training the Random forest Classifier**"""

modelRF = RandomForestClassifier(n_estimators=20, max_depth=150)
modelRF.fit(X_train, Y_train)
#training the Random forest Classifier
X_train_prediction = modelRF.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data RF : ', training_data_accuracy)

# accuracy score on the test data of Random forest Classifier
X_test_prediction = modelRF.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data RF : ', test_data_accuracy)

cmRF = confusion_matrix(Y_test, X_test_prediction)
cmRF

plt.figure(figsize=(7,5))
sn.heatmap(cmRF, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Calculate precision
precision = precision_score(Y_test, X_test_prediction)
print(f"Precision for your RF model:",precision)

# Calculate recall
recall = recall_score(Y_test, X_test_prediction)
print(f"recall for your RF model:",recall)

# Calculate f1_score
f1 = f1_score(Y_test, X_test_prediction)
print("f1_score for your RF model:",f1)

# Random forest model performance using cross_val_score
cross_val_score(RandomForestClassifier(n_estimators=40), X, Y,cv=3)

"""**training the Gradient Boosting Classifier**"""

modelGB = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
modelGB.fit(X_train, Y_train)
#training the Gradient Boosting Classifier
X_train_prediction = modelGB.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data GB: ', training_data_accuracy)

# accuracy score on the test data of Gradient Boosting Classifier
X_test_prediction = modelGB.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data GB: ', test_data_accuracy)

cmGB = confusion_matrix(Y_test, X_test_prediction)
cmGB

plt.figure(figsize=(7,5))
sn.heatmap(cmGB, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Calculate precision
precision = precision_score(Y_test, X_test_prediction)
print(f"Precision for your GB model:",precision)

# Calculate recall
recall = recall_score(Y_test, X_test_prediction)
print(f"recall for your GB model:",recall)

# Calculate f1_score
f1 = f1_score(Y_test, X_test_prediction)
print("f1_score for your GB model:",f1)

#Gradient Boosting  model performance using cross_val_score
cross_val_score(GradientBoostingClassifier(n_estimators=100, learning_rate=0.1), X, Y, cv=3)

"""Making a Predictive System"""

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = modelsvm.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

"""Saving the trained model"""

import pickle

filename = 'diabetes_model.sav'
pickle.dump(modelsvm, open(filename, 'wb'))

# loading the saved model
loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

for column in X.columns:
  print(column)