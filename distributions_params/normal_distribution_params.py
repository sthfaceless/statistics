import numpy as np
import itertools as it
from scipy.special import erf


def get_params(l, r, count):
    # Count params
    total = count.sum()
    u = ((l+r)/2 * count).sum() / total

    _r = len(count) - 3

    sigma_2 = ((((l+r)/2-u) ** 2) * count).sum() / (total-1)
    sigma = sigma_2 ** (1 / 2)

    # Count f(x)
    f = lambda x: 1 / (sigma * (2 * np.pi) ** (1 / 2)) * np.exp(-np.square(x - u) / (2 * sigma_2))

    # Count F(x)
    laplace = lambda x: erf(x / 2 ** 0.5) / 2
    normal = lambda x: (x - u) / sigma
    F = lambda x: laplace(normal(x))

    # Info
    info = f"""
        E[x] = {u}
        D[x] = {sigma_2}
        sigma = {sigma}
        df = {_r}
    """

    return F, f, _r, info
