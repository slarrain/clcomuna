.. image:: https://travis-ci.org/slarrain/clcomuna.svg?branch=master
    :target: https://travis-ci.org/slarrain/clcomuna

.. image:: https://img.shields.io/badge/pypy-0.3.1-blue.svg
    :target: https://pypi.python.org/pypi/clcomuna

clcomuna
========

Very simple package that, given the name of a comuna
from Chile, returns its code

Description
-----------
Each _comuna_ in Chile has a unique code that makes easier to map them to
different attributes (e.g. choropleth). Since I was going through the hassle
of doing it each time I had a new project, I decided to build a very simple
tool that could automate the task. I hope this can be of use to other
developers / civic-hackers.

I added a fuzzy version for cases where there was no exact match.

Installation
------------

::
    pip3 install clcomuna

Requirements
------------

    - fuzzywuzzy
    - Python3.3+



Usage:
.. code:: python
    >>> import clcomuna
    >>> clcomuna.get_code("peumo")
    '06112'
