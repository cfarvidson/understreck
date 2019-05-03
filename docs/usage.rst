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
    result = _.get(test_dictionary, "the_top_level.second_level.third_level")  # result = "it works"
    result = _.get(test_dictionary, "the_top_level.second_level.DOES_NOT_EXIST")  # result = None

    # Using a list or tuple
    result = _.get(test_dictionary, ["the_top_level", "second_level", "third_level"])  # result = "it works"
    result = _.get(test_dictionary, ["the_top_level", "second_level", "DOES_NOT_EXIST"])  # result = None

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