from abc import ABC, abstractmethod
from .vocs import VOCS


class Generator(ABC):
    """
    Tentative suggest/ingest generator interface

    .. code-block:: python

        class MyGenerator(Generator):
            def __init__(self, VOCS, my_parameter, my_keyword=None):
                self.model = init_model(VOCS, my_parameter, my_keyword)

            def suggest(self, num_points):
                return self.model.create_points(num_points)

            def ingest(self, results):
                self.model.update_model(results)

            def finalize(self):
                self.model.dump()

        my_generator = MyGenerator(my_parameter=100)
        results = simulate(my_generator.suggest(10))
        my_generator.ingest(results)
        my_generator.finalize()

    """

    returns_id: bool = False
    """
    Indicates whether this generator returns IDs with the suggested points. Default is ``False``.
    Subclasses should override this if they return IDs. When a generator produces an identifier,
    it must be included in the corresponding dictionary passed back to that generator in ``ingest``
    (under the same key: ``"_id"``).
    """

    @abstractmethod
    def __init__(self, vocs: VOCS, *args, **kwargs):
        """
        Initialize the Generator object on the user-side. Constants, class-attributes,
        and preparation goes here.

        The mandatory `VOCS` defines the input and output names used inside the generator.
        The constructor also accommodates variable positional and keyword arguments so each
        generator can be customized.

        **Parameters:**
            - ``vocs`` (VOCS): The mandatory VOCS object that defines the input and output names.
            - ``*args``: Variable positional arguments for generator-specific customization.
            - ``**kwargs``: Variable keyword arguments for generator-specific customization.

        .. code-block:: python

            >>> generator = NelderMead(
            ...     VOCS(variables={"x": [-5.0, 5.0], "y": [-3.0, 2.0]}, objectives={"f": "MAXIMIZE"}),
            ...     adaptive=False
            ... )
        """
        self._validate_vocs(vocs)

    @abstractmethod
    def _validate_vocs(self, vocs) -> None:
        """
        Validate if the vocs object is compatible with the current generator. Should
        raise a ValueError if the vocs object is not compatible with the generator
        object.

        This method is called automatically during initialization.

        **Parameters:**
            - ``vocs`` (VOCS): The VOCS object to validate.

        **Raises:**
            - ``ValueError``: If the VOCS is not compatible with the generator.

        .. code-block:: python

            >>> generator = NelderMead(
            ...     VOCS(
            ...         variables={"x": [-5.0, 5.0], "y": [-3.0, 2.0]},
            ...         objectives={"f": "MAXIMIZE"},
            ...         constraints={"c": ["LESS_THAN", 0.0]}
            ...     )
            ... )
            ValueError("NelderMead generator cannot accept constraints")
        """

    @abstractmethod
    def suggest(self, num_points: int | None) -> list[dict]:
        """
        Request the next set of points to evaluate.

        Returns a list of points in the input space, to be evaluated next. Each element of the list
        is a separate point. Keys of the dictionary include the name of each input variable specified
        in VOCS (variables + constants). Values of the dictionaries are **scalars** unless the variable
        was declared with an array ``dtype`` attribute.

        **Parameters:**
            - ``num_points`` (int | None): Optional number of points to generate. When not provided,
              the generator decides how many points to return.

        **Returns:**
            - ``list[dict]``: A list of dictionaries, where each dictionary represents a point to
              evaluate. Each dictionary contains keys for all variables and constants from the VOCS,
              and optionally an ``"_id"`` key if the generator supports IDs.

        **Raises:**
            - ``ValueError``: If ``num_points`` is specified but the generator cannot produce that
              exact number of points.

        **Notes:**
            - When ``num_points`` is passed, the generator should return exactly that number of points
              or raise a ``ValueError``.
            - When ``num_points`` is not passed, the generator decides how many points to return.
              Different generators will return different numbers of points. For instance, the simplex
              would return 1 or 3 points. A genetic algorithm could return the whole population.
              Batched Bayesian optimization would return the batch size (i.e., number of points that
              can be processed in parallel), which would be specified in the constructor.
            - Some generators can assign a unique identifier to each generated point (indicated by the
              ``returns_id`` class attribute). If implemented, this identifier should appear in the
              dictionary under the key ``"_id"``.

        .. code-block:: python

            >>> points = generator.suggest(2)
            >>> print(points)
            [{"x": 1.2, "y": 0.8}, {"x": -0.2, "y": 0.4}]

            >>> points = generator.suggest()  # Generator decides
            >>> print(points)
            [{"x": 1.2, "y": 0.8}, {"x": -0.2, "y": 0.4}, {"x": 4.3, "y": -0.1}]
        """

    def ingest(self, results: list[dict]) -> None:
        """
        Send the results of evaluations to the generator.

        Feeds data (past evaluations) to the generator. Each element of the list is a separate point.
        Keys of the dictionary must include each named field specified in the VOCS provided to the
        generator on instantiation (variables, constants, objectives, constraints, and observables).

        **Parameters:**
            - ``results`` (list[dict]): A list of dictionaries, where each dictionary represents an
              evaluated point. Each dictionary must contain keys for all variables, constants,
              objectives, constraints, and observables from the VOCS.

        **Raises:**
            - ``ValueError``: If points are given to ``ingest`` with an ``_id`` value that is not known
              internally (for generators that support IDs).

        **Notes:**
            - Any points provided to the generator via ``ingest`` that were not created by the current
              generator instance should omit the ``_id`` field.
            - If points are given to ``ingest`` with an ``_id`` value that is not known internally,
              a ``ValueError`` error should be raised.

        .. code-block:: python

            >>> point = generator.suggest(1)
            >>> point
            [{"x": 1, "y": 1}]
            >>> point[0]["f"] = objective(point[0])
            >>> point
            [{"x": 1, "y": 1, "f": 2}]
            >>> generator.ingest(point)
        """

    def finalize(self) -> None:
        """
        Perform any work required to close down the generator.

        **Optional.** Performs any work required to close down the generator. Some generators may need
        to close down background processes, files, databases, or asynchronous components. After
        finalize is called, the generator's data is guaranteed to be up to date, including results
        from any outstanding processes, threads, or asynchronous tasks.

        .. code-block:: python

            >>> generator.finalize()
        """
