from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import seaborn as sns
from sklearn.metrics import accuracy_score
iris = sns.load_dataset('iris')

x = iris.iloc[:,0:4]
y = iris.iloc[:, 4]
# x= iris[['sepal_length','sepal_width','petal_length','petal_width']]
# y = iris['species']

# print(x)
# print(y)

x_train , x_test, y_train, y_test = train_test_split(x,y,test_size= 0.2, random_state= 42)
# training qns, exam qns, training ans, exam ans

print(x_train.shape)
print(y_train.shape)

print(x_train.head())

knn = KNeighborsClassifier(n_neighbors= 5) # Hyperparameters
knn.fit(x_train,y_train)

# print(knn.fit(x_train,y_train))

predictions = knn.predict(x_test)
# print(predictions)

print(f"Accuracy is {accuracy_score(predictions, y_test)*100}")
