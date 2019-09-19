
from model import Location
from model import Ship
import unittest


class TestShip(unittest.TestCase):
    def test_init(self):
        ship = Ship('uid', Location(1, 2), 8, 90)
        self.assertEqual('uid', ship.uid)
        self.assertEqual(Location(1, 2), ship.location)
        self.assertEqual(8, ship.size)
        self.assertEqual(90, ship.orientation)

    def test_to_dict(self):
        ship = Ship('uid', Location(1, 2), 8, 90)
        self.assertEqual({'uid': 'uid', 'location': {'x': 1, 'y': 2}, 'size': 8, 'orientation': 90}, ship.to_dict())

    def test_repr(self):
        ship = Ship('uid', Location(1, 2), 8, 90)
        self.assertEqual('{"uid": "uid", "location": {"x": 1, "y": 2}, "size": 8, "orientation": 90}', str(ship))


if __name__ == '__main__':
    unittest.main()
