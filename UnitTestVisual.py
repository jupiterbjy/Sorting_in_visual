import unittest


class TestBasicOutput(unittest.TestCase):
    def test_single(self):
        from VisualMethod import _horizontal
        func = _horizontal().__dict__['str_convert_gen']



