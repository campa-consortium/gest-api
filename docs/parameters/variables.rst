=========
Variables
=========

Variables define the tunable inputs for the optimization problem.

Each entry in ``VOCS.variables`` is a key–value pair where:

* **key** — variable name (string)
* **value** — a variable definition, which may be shorthand or a full object.

Examples
--------

Shorthand forms:

.. code-block:: python

    from gest_api.vocs import VOCS

    # Continuous variable with bounds
    vocs = VOCS(variables={"x": [0.0, 1.0]})

    # Discrete variable with allowed values
    vocs = VOCS(variables={"x": {0, 1, 2}})

    # Explicit type form
    vocs = VOCS(variables={"x": {"type": "ContinuousVariable", "domain": [0.0, 1.0]}})

Longhand form:

.. code-block:: python

    from gest_api.vocs import ContinuousVariable, VOCS

    x_var = ContinuousVariable(domain=[0.0, 1.0], dtype=float, default_value=0.5)
    vocs = VOCS(variables={"x": x_var})

Associated classes:

.. autoclass:: gest_api.vocs.BaseVariable
.. autoclass:: gest_api.vocs.ContinuousVariable
.. autoclass:: gest_api.vocs.DiscreteVariable
