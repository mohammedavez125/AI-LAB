from sklearn.datasets import make_classification
from sklearn import tree
from sklearn.model_selection import train_test_split

X, t = make_classification(100, 5, n_classes=2, shuffle=True, random_state=10)

X_train, X_test, t_train, t_test = train_test_split(
    X, t, test_size=0.3, shuffle=True, random_state=1
)

model = tree.DecisionTreeClassifier()
model.fit(X_train, t_train)

predicted_value = model.predict(X_test)
print(predicted_value)

tree.plot_tree(model)

zeroes = sum(1 for label in t_train if label == 0)
ones = sum(1 for label in t_train if label == 1)
print("Number of zeros:", zeroes)
print("Number of ones:", ones)
val = 1 - ((zeroes / len(t_train)) ** 2 + (ones / len(t_train)) ** 2)
print("Gini impurity:", val)

match = sum(1 for pred, true in zip(predicted_value, t_test) if pred == true)
unmatch = len(t_test) - match
accuracy = match / len(t_test)
print("Accuracy is:", accuracy)