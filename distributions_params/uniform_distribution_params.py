import numpy as np
import itertools as it

def get_params(l, r, count):
    # Count params
    total = count.sum()
    u = ((l + r) / 2 * count).sum() / total

    _r = len(count)-1

    a = l[0]
    b = r[len(r)-1]

    # Count f(x)
    f = lambda x: 1 / (b-a) + x * 0

    # Count F(x)
    F = lambda x: x / (b-a)

    # Info
    info = f"""
        E[x] = {u}
        p = {1/(b-a)}
        len = {b-a}
        df = {_r}
    """

    return F, f, _r, info
