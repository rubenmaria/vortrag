"""This module implements a metric to compare embedding spaces"""
from typing import Callable
import numpy as np
from numpy.typing import NDArray
from sklearn.metrics import ndcg_score
from sklearn.neighbors import NearestNeighbors

def ranking_score(
    x: int,
    rank_x: int,
    other_ranking: list[int]
) -> float:
    assert rank_x < len(other_ranking)
    if other_ranking[rank_x] == x:
        return 1
    if x in other_ranking:
        return 0.5
    return 0

def ranking_diffrence(x: list[int], y: list[int]) -> float:
    assert len(x) == len(y)
    k = len(x)
    true_relevance_score = np.array([[ 1 for _ in range(k)]])
    relevance_score = np.array([[ranking_score(x[i], i, y) for i in range(k)]])
    return float(ndcg_score(relevance_score, true_relevance_score))


def k_nearest_neighbor(k: int, point: NDArray, space: NDArray) -> list[int]:
    neighbors = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(space)
    return neighbors.kneighbors([point], k, return_distance=False)[0].tolist()


def compare_embedding_spaces_k(
    k: int,
    x: NDArray,
    y: NDArray,
    get_neighbors: Callable[[int,NDArray,NDArray], list[int]],
    aggregate: Callable[[list[float]], float]
    ) -> float:
    assert x.shape == y.shape
    n = x.shape[0]
    all_neighbors = [
        (get_neighbors(k, x[i], x), get_neighbors(k, y[i], y))
        for i in range(n)
    ]
    ranking_diffrences = [ranking_diffrence(x, y) for x,y in all_neighbors]
    return aggregate(ranking_diffrences)
