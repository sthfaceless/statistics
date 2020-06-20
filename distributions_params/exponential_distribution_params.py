import numpy as np
import itertools as it

def get_params(l, r, count):
    # Count params
    total = count.sum()
    u = ((l+r)/2*count).sum()/total

    _r = len(count) - 2

    #By maximum likelihood estimation
    h = 1.0 / u

    # Count f(x)
    f = lambda x: h * np.exp(-h*x)

    # Count F(x)
    F = lambda x: 1 - np.exp(-x * h)

    # Info
    info = f"""
        E[x] = {u}
        h = {h}
        df = {_r}
    """

    return F, f, _r, info
