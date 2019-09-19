
from model import Location
from model import Move
from model import Ship
from model import World
import unittest


class TestWorld(unittest.TestCase):
    def test_init(self):
        ship1 = Ship('1', Location(1, 2), 90, 8, 6)
        ship2 = Ship('2', Location(1, 2), 90, 12, 4)
        world = World(300, 200, [ship1, ship2])
        self.assertEqual(300, world.width)
        self.assertEqual(200, world.height)
        self.assertEqual(2, len(world.ships))
        self.assertEqual(ship1, world.ships[0])
        self.assertEqual(ship2, world.ships[1])

    def test_to_dict(self):
        ship1 = Ship('1', Location(1, 2), 90, 8, 6)
        ship2 = Ship('2', Location(1, 2), 90, 12, 4)
        world = World(300, 200, [ship1, ship2])
        expected = {
            'width': 300,
            'height': 200,
            'ships': [
                ship1.to_dict(),
                ship2.to_dict()
            ]
        }
        self.assertEqual(expected, world.to_dict())

    def test_from_dict(self):
        ship1 = Ship('1', Location(1, 2), 90, 8, 6)
        ship2 = Ship('2', Location(1, 2), 90, 12, 4)
        world = World(300, 200, [ship1, ship2])
        self.assertEqual(world, World.from_dict(world.to_dict()))

    def test_apply_move(self):
        ship = Ship('uid', Location(150, 100), 90, 8, 6)
        world = World(300, 200, [ship])
        move = Move(ship.uid, 0, True)
        world.apply_move(move)
        self.assertEqual(Location(150, 94), ship.location)  # moved up 6 (the ship's speed)

    def test_apply_move_collide_with_top_wall(self):
        ship = Ship('uid', Location(100, 5), 90, 8, 6)
        world = World(300, 200, [ship])
        move = Move(ship.uid, 0, True)
        with self.assertRaises(Exception):
            world.apply_move(move)

    def test_apply_move_collide_with_bottom_wall(self):
        ship = Ship('uid', Location(100, 195), 270, 8, 6)
        world = World(300, 200, [ship])
        move = Move(ship.uid, 0, True)
        with self.assertRaises(Exception):
            world.apply_move(move)

    def test_apply_move_collide_with_left_wall(self):
        ship = Ship('uid', Location(5, 100), 180, 8, 6)
        world = World(300, 200, [ship])
        move = Move(ship.uid, 0, True)
        with self.assertRaises(Exception):
            world.apply_move(move)

    def test_apply_move_collide_with_right_wall(self):
        ship = Ship('uid', Location(295, 100), 0, 8, 6)
        world = World(300, 200, [ship])
        move = Move(ship.uid, 0, True)
        with self.assertRaises(Exception):
            world.apply_move(move)

    def test_apply_move_collide_with_ship(self):
        ship1 = Ship('1', Location(150, 100), 0, 8, 6)
        ship2 = Ship('2', Location(155, 100), 0, 8, 6)
        world = World(300, 200, [ship1, ship2])
        move = Move(ship1.uid, 0, True)
        with self.assertRaises(Exception):
            world.apply_move(move)


if __name__ == '__main__':
    unittest.main()
