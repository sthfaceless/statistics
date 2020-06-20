import numpy as np
import distributions_params.pareto_distribution_params as pareto
import distributions_params.poisson_distribution_params as poisson
import distributions_params.discrete_uniform_distribution_params as d_uniform
import distributions_params.uniform_distribution_params as uniform
import distributions_params.exponential_distribution_params as exponential
import distributions_params.normal_distribution_params as normal
import distributions_params.x_2_distribution_params as x_2_distribution

distributions = {
    'pareto': pareto.get_params,
    'poisson': poisson.get_params,
    'd_uniform': d_uniform.get_params,
    'uniform': uniform.get_params,
    'normal': normal.get_params,
    'exponential': exponential.get_params,
    'x_2' : x_2_distribution.get_params
}


def try_distribution(values, count, w, type, name):

    if type == 'discrete':
        F, f, r, info = distributions[name](values, count)
        t = values
    else:
        F, f, r, info = distributions[name](l=values - w / 2, r=values + w / 2, count=count)
        t = np.arange(start=values[0] - w, stop=values[-1] + w, step=(values[-1] + w - values[0] - w) / 100.0)

    s = f(t)

    return F, f, r, s, t, info
