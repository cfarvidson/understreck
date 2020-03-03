#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `understreck` package."""
from __future__ import absolute_import
import pytest


import understreck as _

test_dictionary = {
    "the_top_level": {
        "second_level": {"third_level": "it works", "third_level_sibling": False}
    }
}


@pytest.mark.parametrize(
    "dict_to_test,key_to_get,expected",
    [
        (test_dictionary, "the_top_level.second_level.third_level", "it works"),
        (test_dictionary, "the_top_level.second_level.third_level_sibling", False),
        (test_dictionary, "the_top_level.second_level.DOES_NOT_EXIST", None),
        (test_dictionary, ["the_top_level", "second_level", "DOES_NOT_EXIST"], None),
        (
            test_dictionary,
            "the_top_level.second_level",
            {"third_level": "it works", "third_level_sibling": False},
        ),
        (test_dictionary, ["the_top_level", "second_level", "third_level"], "it works"),
        (
            test_dictionary,
            ["the_top_level", "second_level"],
            {"third_level": "it works", "third_level_sibling": False},
        ),
    ],
)
def test_nested_get(dict_to_test, key_to_get, expected):
    result = _.nested_get(dict_to_test, key_to_get)
    assert result == expected
    result = _.get(dict_to_test, key_to_get)
    assert result == expected


@pytest.mark.parametrize(
    "dict_to_test,key_to_get,expectedException",
    [
        (None, "", _.exceptions.InvalidArgumentError),
        ("", "", _.exceptions.InvalidArgumentError),
        (1, "", _.exceptions.InvalidArgumentError),
        (test_dictionary, None, _.exceptions.InvalidArgumentError),
        (test_dictionary, {}, _.exceptions.InvalidArgumentError),
        (test_dictionary, 1, _.exceptions.InvalidArgumentError),
    ],
)
def test_nested_get_exceptions(dict_to_test, key_to_get, expectedException):
    print(expectedException)
    with pytest.raises(expectedException):
        _.nested_get(dict_to_test, key_to_get)


def test_get_elements_from_list():
    test_dictionary = {"the_top_level": {"second_level_list": ["Hello", "World"]}}
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[0]")
    assert result == "Hello"
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[0]")
    assert result == "Hello"

    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[1]")
    assert result == "World"
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[1]")
    assert result == "World"


def test_get_elements_from_list__object_in_list():
    test_dictionary = {
        "the_top_level": {"second_level_list": [{"name": "Kalle"}, "World"]}
    }
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[0]")
    assert result == {"name": "Kalle"}
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[0]")
    assert result == {"name": "Kalle"}

    assert result == {"name": "Kalle"}
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[0].name")
    assert result == "Kalle"

    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[1]")
    assert result == "World"
    result = _.nested_get(test_dictionary, "the_top_level.second_level_list[1]")
    assert result == "World"


def test_get_elements_from_list__2_levels_deep():
    test_dictionary = {
        "the_top_level": {
            "second_level_list": [
                {"tags": [{"name": "first_tag"}, {"name": "second_tag"}]}
            ]
        }
    }

    result = _.get(test_dictionary, "the_top_level.second_level_list[0].tags[1].name")
    assert result == "second_tag"


def test_get_elements_from_list__3_levels_deep():
    test_dictionary = {
        "the_top_level": {
            "second_level_list": [
                {
                    "tags": [
                        {"name": "first_tag"},
                        {"name": "second_tag"},
                        [{"name": "first_tag"}, {"name": "second_tag"}],
                    ]
                }
            ]
        }
    }

    result = _.get(test_dictionary, "the_top_level.second_level_list[0].tags[2]")
    assert result == [{"name": "first_tag"}, {"name": "second_tag"}]

    result = _.get(
        test_dictionary, "the_top_level.second_level_list[0].tags[2][1].name"
    )
    assert result == "second_tag"


def test_get_elements_from_list__deep_1():
    test_dictionary = {"foo": {"bar": ["x", ["first", "second", "Hello World"]]}}

    result = _.get(test_dictionary, "foo.bar[1][2]",)
    assert result == "Hello World"


def test_get_elements_from_list__deep_2():
    test_dictionary = {
        "foo": {"bar": ["x", ["first", "second", {"name": "Hello World"}]]}
    }

    result = _.get(test_dictionary, "foo.bar[1][2].name",)
    assert result == "Hello World"


def test_get_elements_from_list__deep_3():
    test_dictionary = {"foo": {"bar": ["x", "y", ["x", "y", "z", "Hello World",]]}}

    result = _.get(test_dictionary, "foo.bar[2][3]",)
    assert result == "Hello World"


def test_get_elements_from_list__deep_4():
    test_dictionary = {
        "data": {
            "signUp": {
                "somethingElese": "hello",
                "errors": [{"name": "Error name", "field": "Hello World"}],
            }
        }
    }

    result = _.get(test_dictionary, "data.signUp.errors[0].field",)
    assert result == "Hello World"
