
import json
import math


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

    @staticmethod
    def from_dict(d):
        return Location(d['x'], d['y'])

    """
    Direction is in degrees with:
      0 = Right
      90 = Up
      180 = Left
      270 = Down
    """
    def translate(self, distance, direction):
        self.x += round(distance * math.cos(math.radians(direction)))
        self.y += round(distance * math.sin(math.radians(-direction)))
        return self

    def distance_to(self, location):
        x1 = self.x
        x2 = location.x
        y1 = self.y
        y2 = location.y
        return round(math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))))

    def __eq__(self, other):
        return isinstance(other, Location) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
