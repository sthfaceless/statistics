import numpy as np
import itertools as it
from scipy.special import gammainc
from scipy.special import gamma


def get_params(l, r, count):
    # Count params
    total = count.sum()
    u = ((l+r)/2 * count).sum() / total

    _r = len(count) - 1

    #degree freedom
    r = 1

    # Count f(x)
    f = lambda x: ((1/2) ** (r/2)) * (x ** (r/2-1)) * (np.exp(-x/2)) / gamma(r/2)

    # Count F(x)
    F = lambda x: gammainc(r/2, x/2)

    # Info
    info = f"""
        E[x] = {u}
        df = {r}
    """

    return F, f, _r, info
