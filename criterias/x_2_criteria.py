import numpy as np
from scipy.special import gammaincinv

def cnt_criteria(F, f, r, values, w, counts, type):

    if type == 'discrete':
        p = f(values)
    else:
        p = F(values + w / 2) - F(values - w / 2)

    total = counts.sum()
    np = total * p
    v_np = counts - np
    v_np_2 = v_np ** 2
    diff = v_np_2 / np
    x_2 = diff.sum()

    p_1 = 0.05
    p_2 = 0.01

    critical_1 = gammaincinv(r/2, 1-p_1) * 2
    critical_2 = gammaincinv(r/2, 1-p_2) * 2

    info = f"""
        X^2 criteria is: {x_2}
        For statistical significant {p_1} hypothesa is {x_2 < critical_1} [{critical_1}, ...)
        For statistical significant {p_2} hypothesa is {x_2 < critical_2} [{critical_2}, ...)
        
        count: {counts}
        p: {p}
        np: {np}
        count - np: {v_np}
        (count - np) ^ 2: {v_np_2}
        (count - np) ^ 2 / np: {diff}
    """

    return x_2, info
