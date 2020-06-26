from functools import reduce
import numpy as np
from scipy.special import gamma
from scipy.special import gammainc
from scipy.special import gammaincinv
from scipy.special import erfinv


val = 0.48
print(erfinv(val * 2) * (2 ** 0.5))