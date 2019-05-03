from __future__ import absolute_import

import understreck as _


def test_strip_indents():
    to_strip = """This is a
    multi-line
    string"""

    expected = "This is a\nmulti-line\nstring"

    assert _.strip(to_strip) == expected
