import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset('iris')

print(iris['species'].unique())
print(iris.shape)

# countplot to find catagory and count of catagory
# sns.countplot(iris['species'])

# pairplot is total data show in row x colume and hue is give different color for catagory 
# sns.pairplot(iris , hue= 'species') 

# swarmplot for not overlap value plots 
# sns.swarmplot(iris)

virginica = iris[iris['species'] == 'virginica']
versicolor = iris[iris['species'] == 'versicolor']
setosa = iris[iris['species'] == 'setosa']

print(setosa.head())
print(versicolor.head())
print(virginica.head())

# print(setosa.describe())
# print("------------------------------------------------------------")
# print(virginica.describe())
# print("------------------------------------------------------------")
# print(versicolor.describe())
plt.show()