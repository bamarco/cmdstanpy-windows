{ lib, python3Packages }:

with python3Packages;
buildPythonApplication {
  pname = "demo-cmdstanpy";
  version = "0.1";

  propagatedBuildInputs = [
    cmdstanpy
  ];

  src = ./.;
}
