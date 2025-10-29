============
Observables
============

Observables represent additional outputs from the objective function
that are recorded for analysis but not used directly for optimization.

Each entry in ``VOCS.observables`` is a key–value pair where:

* **key** — observable name (string)
* **value** — a shorthand or longhand definition.

Examples
--------

Shorthand forms:

.. code-block:: python

    from gest_api.vocs import VOCS

    # As a set of names
    vocs = VOCS(observables={"temp", "pressure"})

    # As a dictionary with explicit types
    vocs = VOCS(observables={"temp": "float", "pressure": "float"})

    # Explicit object type form
    vocs = VOCS(observables={"temp": {"type": "Observable", "dtype": float}})

Longhand form:

.. code-block:: python

    from gest_api.vocs import Observable, VOCS

    obs = Observable(dtype=float)
    vocs = VOCS(observables={"temp": obs})

Associated classes:

.. autoclass:: gest_api.vocs.Observable

.. include:: _dtype_note.rst
