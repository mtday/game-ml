
import json


class Move(object):
    def __init__(self, ship_uid, rotation, forward):
        self.ship_uid = ship_uid
        self.rotation = rotation
        self.forward = forward

    def to_dict(self):
        return {
            'ship_uid': self.ship_uid,
            'rotation': self.rotation,
            'forward': self.forward
        }

    def __eq__(self, other):
        return isinstance(other, Move) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
