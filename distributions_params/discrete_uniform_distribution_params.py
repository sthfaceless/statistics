import numpy as np
import itertools as it

def get_params(val, count):
    # Count params
    total = len(count)
    u = (val * count).sum() / count.sum()

    _r = len(val) - 1

    # Count f(x)
    f = lambda x: 1 / total + x * 0

    # Info
    info = f"""
        E[x] = {u}
        p = {1/total}
        len = {total}
        df = {_r}
    """

    return f, f, r, info
