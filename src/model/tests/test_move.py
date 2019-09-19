
from model import Move
import unittest


class TestMove(unittest.TestCase):
    def test_init(self):
        move = Move('ship_uid', -5, True)
        self.assertEqual('ship_uid', move.ship_uid)
        self.assertEqual(-5, move.rotation)
        self.assertEqual(True, move.forward)

    def test_to_dict(self):
        move = Move('ship_uid', -5, True)
        self.assertEqual({'ship_uid': 'ship_uid', 'rotation': -5, 'forward': True}, move.to_dict())

    def test_from_dict(self):
        move = Move('ship_uid', -5, True)
        self.assertEqual(move, Move.from_dict(move.to_dict()))

    def test_repr(self):
        move = Move('ship_uid', -5, True)
        self.assertEqual('{"ship_uid": "ship_uid", "rotation": -5, "forward": true}', str(move))


if __name__ == '__main__':
    unittest.main()
