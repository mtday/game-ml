
from .ship import Ship

import json


class Environment(object):
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

    @staticmethod
    def from_dict(d):
        ships = [Ship.from_dict(s) for s in d['ships']]
        return Environment(d['width'], d['height'], ships)

    def apply_action(self, action):
        for ship in self.ships:
            if ship.uid == action.ship_uid:
                ship.orientation = (ship.orientation + action.rotation) % 360
                if action.forward:
                    ship.location.translate(ship.speed, ship.orientation)
                    self._validate_ship_positions()
        return self

    def apply_actions(self, actions):
        for action in actions:
            self.apply_action(action)
        return self

    def _validate_ship_positions(self):
        self._validate_ship_wall_collision()
        self._validate_ship_ship_collision()

    def _validate_ship_wall_collision(self):
        for ship in self.ships:
            ship_radius = ship.size / 2
            left_edge = ship.location.x - ship_radius
            right_edge = ship.location.x + ship_radius
            top_edge = ship.location.y - ship_radius
            bottom_edge = ship.location.y + ship_radius
            if left_edge < 0 or top_edge < 0 or right_edge > self.width or bottom_edge > self.height:
                raise Exception('Ship {} moved beyond world boundary'.format(ship.uid))

    def _validate_ship_ship_collision(self):
        for ship1 in self.ships:
            for ship2 in self.ships:
                if ship1.uid == ship2.uid:
                    continue
                d = ship1.location.distance_to(ship2.location)
                if d < ship1.size / 2 or d < ship2.size / 2:
                    raise Exception('Ships {} and {} collided'.format(ship1.uid, ship2.uid))

    def __eq__(self, other):
        return isinstance(other, Environment) and self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return json.dumps(self.to_dict())
