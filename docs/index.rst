
=========================
Generator Standard (GeST)
=========================

.. include:: ../README.md
    :parser: myst_parser.sphinx_
    :start-after: # Overview
    :end-before: # Documentation

Specification of the standard
-----------------------------

In order to conform to the standard, a given optimization library (e.g. `Xopt`, `optimas`, `libEnsemble`)
must define the classes documented below, and their corresponding methods:

.. toctree::
    :maxdepth: 2

    generator
    vocs

This is best done by subclassing the abstract classes defined in the Python package `gest-api`, which can be installed with:

.. code-block:: bash

    pip install gest-api
