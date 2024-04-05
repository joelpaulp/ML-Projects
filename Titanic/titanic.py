# -*- coding: utf-8 -*-
"""Titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vPHL0e8-Ma1rGusrJ2Zg89RkBuqRr90o
"""

import numpy as np
import pandas as pd
df=pd.read_csv("Titanic/train.csv")
df1=pd.read_csv("Titanic/test.csv")
df2=pd.read_csv("Titanic/gender_submission.csv")

df2

df1.drop(["PassengerId","Name","Embarked","Cabin","Ticket"], axis=1,inplace=True)
df1.reset_index(drop=True)
df1["Sex"]=df1["Sex"].replace({"male":1,"female":0})

mean= df1.mean()
df1.fillna(mean,inplace=True)
df1.isna().sum()

df

df.isna().sum()

df.drop(["PassengerId","Name","Embarked","Cabin","Ticket"], axis=1,inplace=True)
df.reset_index(drop=True)
df.dropna(subset="Age",axis=0,inplace=True)

y=df["Survived"]
y.reset_index(drop=True)

df.isna().sum()

df.Sex.unique()

df["Sex"]=df["Sex"].replace({"male":1,"female":0})
df

x=df.drop(["Survived"],axis=1)
x.reset_index(drop=True)

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

x_train=x
x_test=df1
y_train=y
y_test=df2.Survived
print(y_test)

print(y_test.shape)
print(x_test.shape)

knn=KNeighborsClassifier()
svc=SVC()
nb=GaussianNB()
ls=[knn,svc,nb]


for i in ls:
  i.fit(x_train,y_train)
  y_pred=i.predict(x_test)
  acc= accuracy_score(y_test,y_pred)
  print("Accuracy Score of",i,"is",acc)

df_result = pd.DataFrame({
    'PassengerId': df2['PassengerId'],
    'y_pred': y_pred
})

# Save the dataframe to a CSV file
df_result.to_csv('result.csv', index=False)