# Overview

This repository is an effort to standardize the interface of the **generators** in optimization libraries such as:

- [`Xopt`](https://github.com/ChristopherMayes/Xopt)
- [`optimas`](https://github.com/optimas-org/optimas)
- [`libEnsemble`](https://github.com/Libensemble/libensemble)
- [`rsopt`](https://github.com/radiasoft/rsopt)

**The objective of this effort is for these different libraries to be able to use each other's generators with little effort.**

*Examples:*
> Using `libEnsemble` generators in `Optimas`:
> APOSMM [NLopt](https://github.com/optimas-org/optimas/blob/f7f5e656f4b98e64a0c2849b6f73aabd49af7682/examples/libe_aposmm_nlopt/run_example.py) - [IBCDFO](https://github.com/optimas-org/optimas/blob/f7f5e656f4b98e64a0c2849b6f73aabd49af7682/examples/libe_aposmm_ibcdfo/run_example.py)
>
> Using `Xopt` generators in `Optimas`:
> [Multiple Examples](https://github.com/optimas-org/optimas/blob/f49bd63d329a8aca2a3444a6a93dbda548f71cfa/tests/test_xopt_generators.py)
>
> Using `Xopt` generators in `libEnsemble`:
> [ExpectedImprovement](https://github.com/Libensemble/libensemble/blob/589d8fb8b0019469ad6a2784e6bcd5e2c2cac8ee/libensemble/tests/regression_tests/test_xopt_EI.py) - [(with Xopt-style sim)](https://github.com/Libensemble/libensemble/blob/589d8fb8b0019469ad6a2784e6bcd5e2c2cac8ee/libensemble/tests/regression_tests/test_xopt_EI_xopt_sim.py)
>
> Using `Optimas` generators in `libEnsemble`:
> [Multi-Fidelity Ax Generator](https://github.com/Libensemble/libensemble/blob/e7fef19c19343c5eceaa4353985aa963ebada46c/libensemble/tests/regression_tests/test_optimas_ax_mf.py)
>
> Using `libEnsemble` generators in `Xopt`:
> [APOSMM Generator](https://github.com/xopt-org/Xopt/blob/cfb8d704637aee31e836357cf47ac0acb82bdc71/xopt/tests/generators/external/test_aposmm.py)

# Definitions

- **Generator:**

  A generator is an object that recommends points to be evaluated in an optimization. It can also receive data (evaluations from past or ongoing optimization), which helps it make more informed recommendations.

  *Note:* The generator does **not** orchestrate the overall optimization (e.g. dispatch evaluations, etc.). As such, it is distinct from `libEnsemble`'s `gen_f` function, and is not itself "workflow" software.

- **Variables, Objectives, Constraints (VOCS):**

  A `VOCS` is an object that specifies the names and types of components of the optimization problem that will be used by the generator. Each generator will validate that it can handle the specified set of variables, objectives, constraints, etc.

# Documentation

For complete API documentation, examples, and detailed specifications, see the official documentation:

**https://generator-standard.readthedocs.io**

# Installation

The Python abstract classes that define the standard can be installed with:

```
pip install gest-api
```