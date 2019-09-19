
import json


class Ship(object):
    def __init__(self, uid, location, size, orientation):
        self.uid = uid
        self.location = location
        self.size = size
        self.orientation = orientation

    def to_dict(self):
        return {
            'uid': self.uid,
            'location': self.location.to_dict(),
            'size': self.size,
            'orientation': self.orientation
        }

    def __eq__(self, other):
        return isinstance(other, Ship) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
