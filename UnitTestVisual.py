import unittest


class TestBasicOutput(unittest.TestCase):
    def test_single(self):
        from VisualMethod import _horizontal_bar
        func = _horizontal_bar().__dict__['str_convert_gen']



