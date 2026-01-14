=========
Constants
=========

Constants represent fixed inputs passed to the objective function that
do not vary during optimization.

Each entry in ``VOCS.constants`` is a key–value pair where:

* **key** — constant name (string)
* **value** — a shorthand or longhand definition.

Examples
--------

Shorthand forms:

.. code-block:: python

    from gest_api.vocs import VOCS

    vocs = VOCS(constants={"alpha": 1.0, "beta": 2.0})
    vocs = VOCS(constants={"alpha": {"type": "Constant", "value": 1.0}})

Longhand form:

.. code-block:: python

    from gest_api.vocs import Constant, VOCS

    alpha_c = Constant(value=1.0)
    vocs = VOCS(constants={"alpha": alpha_c})

Associated classes:

.. autoclass:: gest_api.vocs.Constant

.. include:: _dtype_note.rst
