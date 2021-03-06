import numpy as np
from sklearn.metrics import mean_squared_error

__ALL__ = [
    "root_mean_squared_error"
]


def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_pred, y_true))
