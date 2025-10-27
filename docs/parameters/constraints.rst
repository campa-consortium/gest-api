============
Constraints
============

Constraints define valid conditions on outputs of the objective function
that must be satisfied during optimization.

Each entry in ``VOCS.constraints`` is a key–value pair where:

* **key** — constraint name (string)
* **value** — a shorthand or longhand definition.

Examples
--------

Shorthand forms:

.. code-block:: python

    from gest_api.vocs import VOCS

    # Value must be less than 1.0
    vocs = VOCS(constraints={"c": ["LESS_THAN", 1.0]})

    # Value must be greater than 0.0
    vocs = VOCS(constraints={"c": ["GREATER_THAN", 0.0]})

    # Value must stay within [0, 1]
    vocs = VOCS(constraints={"c": ["BOUNDS", [0.0, 1.0]]})

Longhand form:

.. code-block:: python

    from gest_api.vocs import BoundsConstraint, VOCS

    c_con = BoundsConstraint(range=[0.0, 1.0])
    vocs = VOCS(constraints={"c": c_con})

Associated classes:

.. autoclass:: gest_api.vocs.BaseConstraint
.. autoclass:: gest_api.vocs.LessThanConstraint
.. autoclass:: gest_api.vocs.GreaterThanConstraint
.. autoclass:: gest_api.vocs.BoundsConstraint
