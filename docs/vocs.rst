========
VOCS API
========

.. .. autopydantic_model:: gest_api.vocs.VOCS
..     :model-show-json: False
..     :model-show-validator-members: False
..     :field-list-validators: False
..     :model-show-validator-summary: False
..     :model-show-config-member: False
..     :model-show-config-summary: False
..     :member-order: bysource
    .. :model-show-field-list: False


.. autoclass:: gest_api.vocs.VOCS


.. tab-set::

    .. tab-item:: variables

        Names and settings for input parameters for passing to an objective
        function to solve the optimization problem.

        A **dictionary** with **keys** being variable names (as strings) and **values** as either:

            - A two-element list, representing bounds.
            - A set of discrete values, with curly-braces.

        .. code-block:: python
            :linenos:

            from gest_api.vocs import VOCS

            vocs = VOCS(variables={"x": [0.0, 1.0]})
            ...
            vocs = VOCS(variables={"x": {0, 1, 2, "/usr", "/home", "/bin"}})


    .. tab-item:: objectives

        Names of objective function outputs, and guidance for the direction of optimization.

        A **dictionary** with **keys** being objective names (as strings) and **values** as either:

            - ``"MINIMIZE"``
            - ``"MAXIMIZE"``
            - ``"EXPLORE"``

        .. code-block:: python
            :linenos:

            from gest_api.vocs import VOCS

            vocs = VOCS(objectives={"f": "MINIMIZE"})
            ...
            vocs = VOCS(objectives={"f": "MAXIMIZE"})
            ...
            vocs = VOCS(objectives={"f": "EXPLORE"})


    .. tab-item:: constraints

        Names of function outputs that and their category of constraint that must be satisfied for
        a valid solution to the optimization problem.

        A **dictionary** with **keys** being constraint names (as strings) and **values** as a length-2 list
        with the first element being ``"LESS_THAN"``, ``"GREATER_THAN"``, or ``"BOUNDS"``.

        The second element depends on the type of constraint:
            - If ``"BOUNDS"``, a two-element list of floats, representing boundaries.
            - If ``"LESS_THAN"``, or ``"GREATER_THAN"``, a single float value.

        .. code-block:: python
            :linenos:

            from gest_api.vocs import VOCS

            vocs = VOCS(constraints={"c": ["LESS_THAN", 1.0]})
            ...
            vocs = VOCS(constraints={"c": ["GREATER_THAN", 0.0]})
            ...
            vocs = VOCS(constraints={"c": ["BOUNDS", [0.0, 1.0]]})


    .. tab-item:: constants

        Names and values of constants for passing alongside `variables` to the objective function.

        A **dictionary** with **keys** being constant names (as strings) and **values** as any type.

        .. code-block:: python
            :linenos:

            from gest_api.vocs import VOCS

            vocs = VOCS(constants={"alpha": 1.0, "beta": 2.0})

    .. tab-item:: observables

        Names of other objective function outputs that will be passed
        to the optimizer (alongside the `objectives` and `constraints`).

        A **set** of strings or a **dictionary** with **keys** being names and **values** being type:

        .. code-block:: python
            :linenos:

            from gest_api.vocs import VOCS

            vocs = VOCS(observables={"temp", "temp2"})
            ...
            vocs = VOCS(observables={"temp": "float", "temp2": "int"})


The :class:`~gest_api.vocs.VOCS` class defines all inputs and outputs
of an optimization problem.

Each section below links to the detailed structure for that parameter type.

.. toctree::
   :maxdepth: 1
   :caption: Parameter Reference

   parameters/variables
   parameters/objectives
   parameters/constraints
   parameters/constants
   parameters/observables
