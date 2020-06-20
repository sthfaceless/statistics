from functools import reduce

import numpy as np
import itertools as it
import scipy.special


def get_params(val, count):
    # Count params
    u = (val * count).sum() / count.sum()

    _r = len(count) - 2

    # By maximum likelihood estimation
    h = u

    # Count f(x)
    f = lambda x: np.exp(-h) * (h ** x) / scipy.special.factorial(x)

    # Info
    info = f"""
        E[x] = {u}
        h = {u}
        df = {_r}
    """

    return f, f, _r, info
