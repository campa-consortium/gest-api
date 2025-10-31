==========
Objectives
==========

Objectives define the optimization targets—what the optimizer seeks to
minimize, maximize, or explore.

Each entry in ``VOCS.objectives`` is a key–value pair where:

* **key** — objective name (string)
* **value** — a shorthand or longhand definition.

Examples
--------

Shorthand forms:

.. code-block:: python

    from gest_api.vocs import VOCS

    # Minimize an objective named "f"
    vocs = VOCS(objectives={"f": "MINIMIZE"})

    # Maximize an objective
    vocs = VOCS(objectives={"f": "MAXIMIZE"})

    # Mark an objective for exploration
    vocs = VOCS(objectives={"f": "EXPLORE"})

Longhand form:

.. code-block:: python

    from gest_api.vocs import MinimizeObjective, VOCS

    f_obj = MinimizeObjective(dtype=float)
    vocs = VOCS(objectives={"f": f_obj})

Associated classes:

.. autoclass:: gest_api.vocs.BaseObjective
.. autoclass:: gest_api.vocs.MinimizeObjective
.. autoclass:: gest_api.vocs.MaximizeObjective
.. autoclass:: gest_api.vocs.ExploreObjective

.. include:: _dtype_note.rst
