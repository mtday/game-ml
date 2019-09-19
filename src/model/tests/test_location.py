
from model import Location
import unittest


class TestLocation(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Location(1, 2).x, 1)
        self.assertEqual(Location(1, 2).y, 2)

    def test_to_dict(self):
        self.assertEqual(Location(1, 2).to_dict(), {'x': 1, 'y': 2})

    def test_repr(self):
        self.assertEqual(str(Location(1, 2)), '{"x": 1, "y": 2}')


if __name__ == '__main__':
    unittest.main()
