# Overview

This repository is an effort to standardize the interface of the **generators** in optimization libraries such as:

- [`Xopt`](https://github.com/ChristopherMayes/Xopt)
- [`optimas`](https://github.com/optimas-org/optimas)
- [`libEnsemble`](https://github.com/Libensemble/libensemble)
- [`rsopt`](https://github.com/radiasoft/rsopt)

**The objective of this effort is for these different libraries to be able to use each other's generators with little effort.**

*Example: [using `Xopt` generators in `optimas`](https://github.com/optimas-org/optimas/pull/151)*

# Definitions

- **Generator:**

  A generator is an object that recommends points to be evaluated in an optimization. It can also receive data (evaluations from past or ongoing optimization), which helps it make more informed recommendations.

  *Note:* The generator does **not** orchestrate the overall optimization (e.g. dispatch evaluations, etc.). As such, it is distinct from `libEnsemble`'s `gen_f` function, and is not itself "workflow" software.

  *Examples:*
    - `Xopt`: [here](https://github.com/ChristopherMayes/Xopt/blob/main/xopt/generators/sequential/neldermead.py#L64) is the generator for the Nelder-Mead method. All Xopt generators implement the methods `generate` (i.e. make recommendations) and `add_data` (i.e. receive data).
    - `optimas`: [here](https://github.com/optimas-org/optimas/blob/main/optimas/generators/base.py#L27) is the base class for all generators. It implements the methods `suggest` (i.e. make recommendations) and `ingest` (i.e. receive data).

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