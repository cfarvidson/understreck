from __future__ import absolute_import

import understreck as _


def test_chunk_size():
    to_chunk = ["one", "two", "three", "four", "five"]
    chunk_size = _.chunks.calculate_size(to_chunk, 2)
    assert chunk_size == 3
    assert isinstance(chunk_size, int)


def test_chunks_5():
    to_chunk = ["one", "two", "three", "four", "five"]
    result = _.chunks.split(to_chunk, 2)
    expected = [["one", "two", "three"], ["four", "five"]]
    assert result == expected


def test_chunks_7():
    to_chunk = ["one", "two", "three", "four", "five", "six", "seven"]
    result = _.chunks.split(to_chunk, 2)
    expected = [["one", "two", "three", "four"], ["five", "six", "seven"]]
    assert result == expected
