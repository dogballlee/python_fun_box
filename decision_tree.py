from sklearn.datasets import load_wine
from sklearn import tree
from sklearn.model_selection import train_test_split
import graphviz

wine = load_wine()

x_train, x_test, y_train, y_test = train_test_split(wine.data,wine.target,test_size=.3,random_state=22)
clf = tree.DecisionTreeClassifier(criterion='entropy',random_state=22,splitter='random')

clf.fit(x_train,y_train)
acc = clf.score(x_test,y_test)
# print(acc)

