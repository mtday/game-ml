
from model import Action
from model import Environment
from model import Location
from model import Ship
import unittest


class TestWorld(unittest.TestCase):
    def test_init(self):
        ship1 = Ship('1', Location(1, 2), 90, 8, 6)
        ship2 = Ship('2', Location(1, 2), 90, 12, 4)
        environment = Environment(300, 200, [ship1, ship2])
        self.assertEqual(300, environment.width)
        self.assertEqual(200, environment.height)
        self.assertEqual(2, len(environment.ships))
        self.assertEqual(ship1, environment.ships[0])
        self.assertEqual(ship2, environment.ships[1])

    def test_to_dict(self):
        ship1 = Ship('1', Location(1, 2), 90, 8, 6)
        ship2 = Ship('2', Location(1, 2), 90, 12, 4)
        environment = Environment(300, 200, [ship1, ship2])
        expected = {
            'width': 300,
            'height': 200,
            'ships': [
                ship1.to_dict(),
                ship2.to_dict()
            ]
        }
        self.assertEqual(expected, environment.to_dict())

    def test_from_dict(self):
        ship1 = Ship('1', Location(1, 2), 90, 8, 6)
        ship2 = Ship('2', Location(1, 2), 90, 12, 4)
        environment = Environment(300, 200, [ship1, ship2])
        self.assertEqual(environment, Environment.from_dict(environment.to_dict()))

    def test_apply_action(self):
        ship = Ship('uid', Location(150, 100), 90, 8, 6)
        environment = Environment(300, 200, [ship])
        action = Action(ship.uid, 0, True)
        environment.apply_action(action)
        self.assertEqual(Location(150, 94), ship.location)  # moved up 6 (the ship's speed)

    def test_apply_action_collide_with_top_wall(self):
        ship = Ship('uid', Location(100, 5), 90, 8, 6)
        environment = Environment(300, 200, [ship])
        action = Action(ship.uid, 0, True)
        with self.assertRaises(Exception):
            environment.apply_action(action)

    def test_apply_action_collide_with_bottom_wall(self):
        ship = Ship('uid', Location(100, 195), 270, 8, 6)
        environment = Environment(300, 200, [ship])
        action = Action(ship.uid, 0, True)
        with self.assertRaises(Exception):
            environment.apply_action(action)

    def test_apply_action_collide_with_left_wall(self):
        ship = Ship('uid', Location(5, 100), 180, 8, 6)
        environment = Environment(300, 200, [ship])
        action = Action(ship.uid, 0, True)
        with self.assertRaises(Exception):
            environment.apply_action(action)

    def test_apply_action_collide_with_right_wall(self):
        ship = Ship('uid', Location(295, 100), 0, 8, 6)
        environment = Environment(300, 200, [ship])
        action = Action(ship.uid, 0, True)
        with self.assertRaises(Exception):
            environment.apply_action(action)

    def test_apply_action_collide_with_ship(self):
        ship1 = Ship('1', Location(150, 100), 0, 8, 6)
        ship2 = Ship('2', Location(155, 100), 0, 8, 6)
        environment = Environment(300, 200, [ship1, ship2])
        action = Action(ship1.uid, 0, True)
        with self.assertRaises(Exception):
            environment.apply_action(action)


if __name__ == '__main__':
    unittest.main()
