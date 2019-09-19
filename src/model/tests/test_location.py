
from model import Location
import unittest


class TestLocation(unittest.TestCase):
    def test_init(self):
        self.assertEqual(1, Location(1, 2).x)
        self.assertEqual(2, Location(1, 2).y)

    def test_to_dict(self):
        self.assertEqual({'x': 1, 'y': 2}, Location(1, 2).to_dict())

    def test_from_dict(self):
        location = Location(1, 2)
        self.assertEqual(location, Location.from_dict(location.to_dict()))

    def test_translate(self):
        # translate 20 pixels right (0 degrees)
        self.assertEqual(120, Location(100, 100).translate(20, 0).x)
        self.assertEqual(100, Location(100, 100).translate(20, 0).y)
        # translate 20 pixels up (90 degrees)
        self.assertEqual(100, Location(100, 100).translate(20, 90).x)
        self.assertEqual(80,  Location(100, 100).translate(20, 90).y)
        # translate 20 pixels left (180 degrees)
        self.assertEqual(80,  Location(100, 100).translate(20, 180).x)
        self.assertEqual(100, Location(100, 100).translate(20, 180).y)
        # translate 20 pixels down (270 degrees)
        self.assertEqual(100, Location(100, 100).translate(20, 270).x)
        self.assertEqual(120, Location(100, 100).translate(20, 270).y)
        # translate 20 pixels top-right (45 degrees)
        self.assertEqual(114, Location(100, 100).translate(20, 45).x)
        self.assertEqual(86,  Location(100, 100).translate(20, 45).y)
        # translate 20 pixels top-left (135 degrees)
        self.assertEqual(86,  Location(100, 100).translate(20, 135).x)
        self.assertEqual(86,  Location(100, 100).translate(20, 135).y)
        # translate 20 pixels bottom-left (225 degrees)
        self.assertEqual(86,  Location(100, 100).translate(20, 225).x)
        self.assertEqual(114, Location(100, 100).translate(20, 225).y)
        # translate 20 pixels bottom-right (315 degrees)
        self.assertEqual(114, Location(100, 100).translate(20, 315).x)
        self.assertEqual(114, Location(100, 100).translate(20, 315).y)

    def test_repr(self):
        self.assertEqual('{"x": 1, "y": 2}', str(Location(1, 2)))


if __name__ == '__main__':
    unittest.main()
