#!/usr/bin/env python3
import os
from cmdstanpy import CmdStanModel

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# summarize the results (wraps CmdStan `bin/stansummary`):
if __name__ == '__main__':
    stan_file = resource_path('bernoulli.stan')
    data_file = resource_path('bernoulli.data.json')

    # instantiate a model; compiles the Stan program by default
    model = CmdStanModel(stan_file=stan_file)

    # obtain a posterior sample from the model conditioned on the data
    fit = model.sample(chains=4, data=data_file)

    fit.summary()
