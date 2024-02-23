# Cmdstanpy on Windows

- github workflow does not currently bundle cmdstan into the exe
- nix python support for windows is experimental enough so as to be non-existent

``` sh
pyinstaller -F --add-data bernoulli.stan:. --add-data bernoulli.data.json:. --add-binary $CMDSTAN:./cmdstan  --runtime-hook env_patch.py cmd.py
```
