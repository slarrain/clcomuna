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
Each *comuna* in Chile has a unique code that makes easier to map them to
different attributes (e.g. choropleth). Since I was going through the hassle
of doing it each time I had a new project, I decided to build a very simple
tool that could automate the task. I hope this can be of use to other
developers / civic-hackers.

I added a fuzzy version for cases where there was no exact match.

Features
--------
- Given a comuna name, it returns its code, taking care of special characters, uppercases and lowercases.
- If it doesn't find an exact match, it prints that and returns None
- A fuzzy function returns the best match (uses fuzzywuzzy)
- You can specify to print the score of the fuzzy match
- You can specify a threshold above which it should return a match and below which it shouldn't.
- There is a function that tries the exact match and if it doesn't find it, it goes to the fuzzy version.
- The list of comunas-code is a simple CSV file for easier edition.
- If you want some comuna name version added to the csv file, just contact me and I'll add them right away.

Installation
------------
::
    
    pip3 install clcomuna

Requirements
------------

- fuzzywuzzy
- Python3.3+



Usage:
------

>>> import clcomuna

(If there is a warning, ignore it. It comes with the dependency)

**get_code**

>>> clcomuna.get_code("peumo")
'06112'

**get_fuzzy**: returns name, not code

>>> clcomuna.get_fuzzy("alragobo")
'ALGARROBO'
>>> clcomuna.get_fuzzy("alragobo", True)
('ALGARROBO', 71)
'ALGARROBO'
>>> clcomuna.get_fuzzy("alragobo", True, 72)
('ALGARROBO', 71)
Score lower than minimum threshold for comuna: ALRAGOBO - ALGARROBO

The optional second parameter *True* prints the found comuna and the score.
The optional third parameter *int* stablishes a threshold for the function to
return the best name match

**get_steps**

>>> clcomuna.get_steps("alragobo")
Could not find code for:  ALRAGOBO
'ALGARROBO'
>>> clcomuna.get_fuzzy("alragobo", False, 74)
Score lower than minimum threshold for comuna: ALRAGOBO - ALGARROBO
