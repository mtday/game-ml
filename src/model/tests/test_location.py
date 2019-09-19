
from model import Location
import unittest


class TestLocation(unittest.TestCase):
    def test_init(self):
        self.assertEqual(1, Location(1, 2).x)
        self.assertEqual(2, Location(1, 2).y)

    def test_to_dict(self):
        self.assertEqual({'x': 1, 'y': 2}, Location(1, 2).to_dict())

    def test_repr(self):
        self.assertEqual('{"x": 1, "y": 2}', str(Location(1, 2)))


if __name__ == '__main__':
    unittest.main()
