
import json


class World(object):
    def __init__(self, width, height, ships):
        self.width = width
        self.height = height
        self.ships = ships

    def to_dict(self):
        return {
            'width': self.width,
            'height': self.height,
            'ships': [ship.to_dict() for ship in self.ships]
        }

    def __eq__(self, other):
        return isinstance(other, World) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())

