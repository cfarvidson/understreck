#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `understreck` package."""
from __future__ import absolute_import
import pytest


from understreck import nested_get, InvalidArgumentError

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
    result = nested_get(dict_to_test, key_to_get)
    assert result == expected


@pytest.mark.parametrize(
    "dict_to_test,key_to_get,expectedException",
    [
        (None, "", InvalidArgumentError),
        ("", "", InvalidArgumentError),
        (1, "", InvalidArgumentError),
        (test_dictionary, None, InvalidArgumentError),
        (test_dictionary, {}, InvalidArgumentError),
        (test_dictionary, 1, InvalidArgumentError),
    ],
)
def test_nested_get_exceptions(dict_to_test, key_to_get, expectedException):
    print(expectedException)
    with pytest.raises(expectedException):
        nested_get(dict_to_test, key_to_get)
