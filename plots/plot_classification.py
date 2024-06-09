from sklearn.datasets import make_classification
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV
import matplotlib.pyplot as plt

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=1, n_classes=1, random_state=42,
    n_redundant=1
)
param_dist = {
    "min_samples_leaf": randint(1, 9),  # Verteilung
    "max_depth": [3, 4, 5, 6],
    "criterion": ["gini", "entropy"],
}
tree = DecisionTreeClassifier()
tree_cv = RandomizedSearchCV(tree, param_dist, scoring="f1")
tree_cv.fit(X, y)

print(f"Best parameters: {tree_cv.best_params_}")
print(f"Best score: {tree_cv.best_score_}")


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(X, y, color='tab:blue')
#ax.plot(X, regression_model_bad.predict(X), color='tab:orange')
#ax.plot(X, regression_model_cv.predict(X), color='tab:green')
plt.show()
