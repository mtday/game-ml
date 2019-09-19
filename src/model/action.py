
import json


class Action(object):
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

    @staticmethod
    def from_dict(d):
        return Action(d['ship_uid'], d['rotation'], d['forward'])

    def __eq__(self, other):
        return isinstance(other, Action) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
