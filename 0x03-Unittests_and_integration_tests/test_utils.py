#!/usr/bin/env python3
"""Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit Test for utils.access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, {"a"}, {"b", 2}),
            ({"a": {"b": 2}}, {"a", "b"}, 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method for utils.access_nested_map"""
        got = access_nested_map(nested_map, path)
        self.assertEqual(got, expected)
