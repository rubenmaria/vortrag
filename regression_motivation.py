from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

X, y = make_regression(
    n_samples=1000,
    n_features=1,
    n_informative=10,
    random_state=42
)

regression_model = Ridge(alpha=2000)
regression_model.fit(X,y)

print(f"score: {regression_model.score(X,y)}")

