# -*- coding: utf-8 -*-
"""customer segmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12LrwgvUmntuWQlhrI4Y4YBk0GuzzErzA
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("/content/Mall_Customers.csv")

df.head()

df.describe()

sns.distplot(df['Annual Income (k$)']);

df.columns

columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.distplot(df[i])

columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.kdeplot(x=df[i], shade=True, hue=df['Gender']) # Changed the first argument to x=df[i]

columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.boxplot(data=df,x='Gender',y=df[i])

df['Gender'].value_counts(normalize=True)

clustering1 = KMeans(n_clusters=3)
clustering1.fit(df[['Annual Income (k$)']])
KMeans(n_clusters=3)
clustering1.labels_

sns.scatterplot(data=df, x='Annual Income (k$)',y='Spending Score (1-100)' )

sns.pairplot(df,hue='Gender')

df.groupby(['Gender'])[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean() # changed tuple to list

df = pd.get_dummies(df, columns=['Gender'], drop_first=True)


df.corr()

import numpy as np
import seaborn as sns
import pandas as pd

sns.heatmap(df.select_dtypes(include=np.number).corr(),annot=True,cmap='coolwarm')

clustering1 = KMeans(n_clusters=3)
clustering1.fit(df[['Annual Income (k$)']])

clustering1.labels_

df['Income Cluster'] = clustering1.labels_
df.head()

df['Income Cluster'].value_counts()

clustering1.inertia_

intertia_scores=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df[['Annual Income (k$)']])
    intertia_scores.append(kmeans.inertia_)
intertia_scores

plt.plot(range(1,11),intertia_scores)

df.columns
df.groupby('Income Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()

clustering2 = KMeans(n_clusters=5)
clustering2.fit(df[['Annual Income (k$)','Spending Score (1-100)']])
df['Spending and Income Cluster'] =clustering2.labels_
df.head()

intertia_scores2=[]
for i in range(1,11):
    kmeans2=KMeans(n_clusters=i)
    kmeans2.fit(df[['Annual Income (k$)','Spending Score (1-100)']])
    intertia_scores2.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_scores2)

centers =pd.DataFrame(clustering2.cluster_centers_)
centers.columns = ['x','y']
plt.figure(figsize=(10,8))
plt.scatter(x=centers['x'],y=centers['y'],s=100,c='black',marker='*')
sns.scatterplot(data=df, x ='Annual Income (k$)',y='Spending Score (1-100)',hue='Spending and Income Cluster',palette='tab10')
plt.savefig('clustering_bivaraiate.png')

print(df.columns)

if 'Gender' in df.columns:
    pd.crosstab(df['Spending and Income Cluster'],df['Gender'],normalize='index')
else:
    print("Column 'Gender' not found in DataFrame.")

df.groupby('Spending and Income Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df.head()

dff = pd.get_dummies(df,drop_first=True)
dff.head()

dff.columns

dff = dff[['Age', 'Annual Income (k$)', 'Spending Score (1-100)','Gender_Male']]
dff.head()

intertia_scores3=[]
for i in range(1,11):
    kmeans3=KMeans(n_clusters=i)
    kmeans3.fit(dff)
    intertia_scores3.append(kmeans3.inertia_)
plt.plot(range(1,11),intertia_scores3)

df