=====
Usage
=====

To use Understreck in a project::

    import understreck as _

Then you can use the various helper functions.

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