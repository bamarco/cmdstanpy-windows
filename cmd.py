#!/usr/bin/env python3
import os
from cmdstanpy import CmdStanModel

stan_file = os.path.join('bernoulli.stan')
data_file = os.path.join('bernoulli.data.json')

# instantiate a model; compiles the Stan program by default
model = CmdStanModel(stan_file=stan_file)

# obtain a posterior sample from the model conditioned on the data
fit = model.sample(chains=4, data=data_file)

# summarize the results (wraps CmdStan `bin/stansummary`):
fit.summary()
