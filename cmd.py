#!/usr/bin/env python3
import os
from cmdstanpy import CmdStanModel

stan_file = os.path.join('bernoulli.stan')

model = CmdStanModel(stan_file=stan_file)

print(model)
