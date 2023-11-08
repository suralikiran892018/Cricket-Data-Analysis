# -*- coding: utf-8 -*-
"""Cricket-Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s9jw55ECmiy9mw69ExeifL58b1W8Pc9a
"""

import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
import sklearn

data=pd.read_csv("matches.csv")

data

data.head()

data.describe()

data[['dl_applied',	'win_by_runs',	'win_by_wickets']].describe()







data.isnull().sum()

data=data.iloc[:,:-1]
data.dropna(inplace=True)

data.isnull().sum()

data['team1'].unique()

##delhi
data['team1']=data['team1'].str.replace('Delhi Daredevils','Delhi Capitals')
data['team2']=data['team2'].str.replace('Delhi Daredevils','Delhi Capitals')
data['winner']=data['winner'].str.replace('Delhi Daredevils','Delhi Capitals')

#Sunrisers Hyderabad
data['team1']=data['team1'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
data['team2']=data['team2'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
data['winner']=data['winner'].str.replace('Deccan Chargers','Sunrisers Hyderabad')

data['team1'].unique()

plt.figure(figsize=(10,6))
sns.countplot(y='winner',data=data,order=data['winner'].value_counts().index)
plt.xlabel('Wins')
plt.ylabel('Team')
plt.title('Number of IPL matches won by each team')

plt.figure(figsize=(10,6))
sns.countplot(y='venue',data=data,order=data['venue'].value_counts().iloc[:10].index)
plt.xlabel('No. of matches')
plt.ylabel('Venue')
plt.title('Total Number of Matches played in different stadium')

plt.figure(figsize=(10,6))
sns.countplot(x="toss_decision",data=data)
plt.xlabel("Toss descision")
plt.ylabel("Count")
plt.title("Toss decision")



data.drop(['id','venue','city','date','umpire1','season','player_of_match'],axis=1,inplace=True)

data

X = data.drop(['winner'],axis=1)
y = data['winner']

X=pd.get_dummies(X,['team1','team2','toss_winner','toss_decision','result'],drop_first=True)

X



from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.8)

from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier(n_estimators=200,min_samples_split=3,max_features="auto")

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score

ac=accuracy_score(y_pred,y_test)
ac



