
import json


class Ship(object):
    def __init__(self, uid, location, orientation, size, speed):
        self.uid = uid
        self.location = location
        self.orientation = orientation  # in degrees with 0=Right, 90=Up, 180=Left, 270=Down
        self.size = size
        self.speed = speed

    def to_dict(self):
        return {
            'uid': self.uid,
            'location': self.location.to_dict(),
            'orientation': self.orientation,
            'size': self.size,
            'speed': self.speed
        }

    def __eq__(self, other):
        return isinstance(other, Ship) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
