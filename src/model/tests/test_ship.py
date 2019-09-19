
from model import Location
from model import Ship
import unittest


class TestShip(unittest.TestCase):
    def test_init(self):
        ship = Ship(Location(1, 2), 8, 90)
        self.assertEqual(ship.location, Location(1, 2))
        self.assertEqual(ship.size, 8)
        self.assertEqual(ship.orientation, 90)

    def test_to_dict(self):
        ship = Ship(Location(1, 2), 8, 90)
        self.assertEqual(ship.to_dict(), {'location': {'x': 1, 'y': 2}, 'size': 8, 'orientation': 90})

    def test_repr(self):
        ship = Ship(Location(1, 2), 8, 90)
        self.assertEqual(str(ship), '{"location": {"x": 1, "y": 2}, "size": 8, "orientation": 90}')


if __name__ == '__main__':
    unittest.main()
