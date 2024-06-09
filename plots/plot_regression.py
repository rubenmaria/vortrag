from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

X, y = make_regression(
    n_samples=1000,
    n_features=1,
    n_informative=10,
    random_state=42
)
parameter_grid = {"alpha": [1, 5, 10, 20, 50, 100]}
regression_model = Ridge()  # Lineare Regression mit Ridge
regression_model_cv = GridSearchCV(regression_model, parameter_grid, scoring="r2")
regression_model_cv.fit(X, y)

regression_model_bad = Ridge(alpha=2000)
regression_model_bad.fit(X,y)


print(regression_model_bad.score(X,y))
print(f"Best parameters: {regression_model_cv.best_params_}")
print(f"Best score: {regression_model_cv.best_score_}")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(X, y, color='tab:blue')
ax.plot(X, regression_model_bad.predict(X), color='tab:orange')
ax.plot(X, regression_model_cv.predict(X), color='tab:green')
plt.show()

