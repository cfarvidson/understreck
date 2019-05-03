from __future__ import absolute_import

import understreck as _


def test_filter__function():
    users = [
        {"user": "barney", "age": 36, "active": True},
        {"user": "fred", "age": 40, "active": False},
    ]

    result = _.filter(users, lambda x: not x.get("active"))
    assert result == [{"user": "fred", "age": 40, "active": False}]


def test_filter__function_tuple():
    users = (
        {"user": "barney", "age": 36, "active": True},
        {"user": "fred", "age": 40, "active": False},
    )

    result = _.filter(users, lambda x: not x.get("active"))
    assert result == ({"user": "fred", "age": 40, "active": False},)


def test_filter__matches():
    users = [
        {"user": "barney", "age": 36, "active": True},
        {"user": "fred", "age": 40, "active": False},
    ]

    result = _.filter(users, {"age": 36, "active": True})
    assert result == [{"user": "barney", "age": 36, "active": True}]


def test_filter__matches_tuple():
    users = (
        {"user": "barney", "age": 36, "active": True},
        {"user": "fred", "age": 40, "active": False},
    )

    result = _.filter(users, {"age": 36, "active": True})
    assert result == ({"user": "barney", "age": 36, "active": True},)


def test_filter__matches_property():
    users = [
        {"user": "barney", "age": 36, "active": True},
        {"user": "fred", "age": 40, "active": False},
    ]

    result = _.filter(users, ["active", False])
    assert result == [{"user": "fred", "age": 40, "active": False}]


def test_filter__property():
    users = [
        {"user": "barney", "age": 36, "active": True},
        {"user": "fred", "age": 40, "active": False},
    ]

    result = _.filter(users, ["active"])
    assert result == [{"user": "barney", "age": 36, "active": True}]
