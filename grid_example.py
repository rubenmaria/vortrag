from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

X, y = make_regression(
    n_samples=1000,
    n_features=1,
    n_informative=10,
    random_state=42
)
parameter_grid = {"alpha": [1, 5, 10, 20, 50, 100, 2000]}
regression_model = Ridge()  # Lineare Regression mit Ridge
regression_model_cv = GridSearchCV(regression_model, parameter_grid, scoring="r2")
regression_model_cv.fit(X, y)

print(f"Best parameters: {regression_model_cv.best_params_}")
print(f"Best score: {regression_model_cv.best_score_}")
