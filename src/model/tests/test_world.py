
from model import Location
from model import Ship
from model import World
import unittest


class TestWorld(unittest.TestCase):
    def test_init(self):
        ship1 = Ship('1', Location(1, 2), 8, 90)
        ship2 = Ship('2', Location(1, 2), 12, 90)
        world = World(300, 200, [ship1, ship2])
        self.assertEqual(world.width, 300)
        self.assertEqual(world.height, 200)
        self.assertEqual(len(world.ships), 2)
        self.assertEqual(world.ships[0], ship1)
        self.assertEqual(world.ships[1], ship2)

    def test_to_dict(self):
        ship1 = Ship('1', Location(1, 2), 8, 90)
        ship2 = Ship('2', Location(1, 2), 12, 90)
        world = World(300, 200, [ship1, ship2])
        expected = {
            'width': 300,
            'height': 200,
            'ships': [
                ship1.to_dict(),
                ship2.to_dict()
            ]
        }
        self.assertEqual(world.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
