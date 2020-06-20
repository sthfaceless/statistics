import numpy as np
import itertools as it

def get_params(l, r, count):
    # Count params
    total = count.sum()
    u = ((l + r) / 2 * count).sum() / total

    _r = len(count) - 2

    x0 = l[0]

    lnsum = (np.log((l+r)/2) * count).sum() / total
    a = 1 / (lnsum - np.log(x0))

    # Count f(x)
    f = lambda x: a/x0 * (x0 / x) ** (a+1)

    # Count F(x)
    F = lambda x: 1 - (x0/x) ** a

    # Info
    info = f"""
        E[x] = {u}
        Xo = {x0}
        a = {a}
        df = {_r}
    """

    return F, f, _r, info
