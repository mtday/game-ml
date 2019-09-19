
import json


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

    def __eq__(self, other):
        return isinstance(other, Location) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
