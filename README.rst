===========
Understreck
===========


.. image:: https://img.shields.io/pypi/v/understreck.svg
        :target: https://pypi.python.org/pypi/understreck

.. image:: https://travis-ci.com/cfarvidson/understreck.svg?branch=master
        :target: https://travis-ci.com/cfarvidson/understreck

.. image:: https://readthedocs.org/projects/understreck/badge/?version=latest
        :target: https://understreck.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/ambv/black
        :alt: Code style: black

.. image:: https://pepy.tech/badge/understreck
        :target: https://pepy.tech/project/understreck
        :alt: downloads

A collection of nice utility functions for python


* Free software: GNU General Public License v3
* Documentation: https://understreck.readthedocs.io.


Features
--------

* Perform a safe get on a nested dictionary with the nested_get function
* Split a list into chunks
* Filter a list of dictionaries
* Strip indents from multiline strings

Examples
--------

Get example::

    import understreck as _

    test_dictionary = {
        "foo": {
            "second_level": {"third_level": "it works", "third_level_sibling": False},
            "second_level_list": ["Hello", "World", {"planet": "Earth"}, ["Hello", "World", {"planet": "jupiter"}, ]],
        }
    }

    # Using dot delimited strings
    result = _.get(test_dictionary, "foo.second_level.third_level")  # result == "it works"
    result = _.get(test_dictionary, "foo.second_level.DOES_NOT_EXIST")  # result == None

    # Using a list or tuple
    result = _.get(test_dictionary, ["foo", "second_level", "third_level"])  # result == "it works"
    result = _.get(test_dictionary, ["foo", "second_level", "DOES_NOT_EXIST"])  # result == None

    # Getting elements in list

    result = _.get(test_dictionary, "foo.second_level_list[0]")  # result == "Hello"
    result = _.get(test_dictionary, "foo.second_level_list[1]")  # result == "World"
    result = _.get(test_dictionary, "foo.second_level_list[2].planet")  # result == "Earth"

    # Getting a property in a nested list 
    nested_list = {
                    "foo": {
                        "bar": [
                            "x", [
                                "first", "second", {"name": "Hello World"}
                            ]
                        ]
                    }
                  }

    result = _.get(nested_list, "foo.bar[1][2].name")  # result == "Hello World"

Chunks example::

    import understreck as _

    to_chunk = ["one", "two", "three", "four", "five"]
    result = _.chunks.split(to_chunk, 2)  # result == [["one", "two", "three"], ["four", "five"]]

Filter example::

    import understreck as _

    users = [
            {"user": "barney", "age": 36, "active": True},
            {"user": "fred", "age": 40, "active": False},
        ]

    # Using a lambda function
    result = _.filter(users, lambda x: not x.get("active"))  # result == [{"user": "fred", "age": 40, "active": False}]

    # Using partial dictionary
    result = _.filter(users, {"age": 36, "active": True})  # result == [{"user": "barney", "age": 36, "active": True}]

    # Using a list with a property name and value
    result = _.filter(users, ["active", False])  # result == [{"user": "fred", "age": 40, "active": False}]

    # Using a list with a property name. The value must be truthy.
    result = _.filter(users, ["active"])  # result == [{"user": "barney", "age": 36, "active": True}]

Strip indents example::

    import understreck as _

    def some_function():
        to_strip = """This is a
        multi-line
        string"""

        _.strip(to_strip)  # "This is a\nmulti-line\nstring"

Credits
-------

I have to credit the Lodash_ project for inspiration!

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Lodash: https://lodash.com
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
