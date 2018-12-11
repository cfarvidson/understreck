===========
Understreck
===========


.. image:: https://img.shields.io/pypi/v/understreck.svg
        :target: https://pypi.python.org/pypi/understreck

.. image:: https://travis-ci.org/cfp2000/understreck.svg?branch=master
        :target: https://travis-ci.org/cfp2000/understreck

.. image:: https://readthedocs.org/projects/understreck/badge/?version=latest
        :target: https://understreck.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/cfp2000/understreck/shield.svg
     :target: https://pyup.io/repos/github/cfp2000/understreck/
     :alt: Updates



A collection of nice utility functions for python


* Free software: GNU General Public License v3
* Documentation: https://understreck.readthedocs.io.


Features
--------

* Perform a safe get on a nested dictionary with the nested_get function
* Split a list into chunks

Nested Get example::

    import understreck as _

    test_dictionary = {
        "the_top_level": {
            "second_level": {"third_level": "it works", "third_level_sibling": False}
        }
    }

    # Using dot delimited strings
    result = _.nested_get(test_dictionary, "the_top_level.second_level.third_level")  # result = "it works"
    result = _.nested_get(test_dictionary, "the_top_level.second_level.DOES_NOT_EXIST")  # result = None

    # Using a list or tuple
    result = _.nested_get(test_dictionary, ["the_top_level", "second_level", "third_level"])  # result = "it works"
    result = _.nested_get(test_dictionary, ["the_top_level", "second_level", "DOES_NOT_EXIST"])  # result = None

Chunks example::

    import understreck as _

    to_chunk = ["one", "two", "three", "four", "five"]
    result = _.chunks.split(to_chunk, 2)  # result == [["one", "two", "three"], ["four", "five"]]

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
