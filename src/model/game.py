
from .location import Location
from .ship import Ship
from .world import World

import json
import random


class Game(object):
    def __init__(self, random_seed, width=600, height=400, num_ships=5, ship_size=8, ship_speed=6):
        self.random_seed = random_seed
        self.width = width
        self.height = height
        self.num_ships = num_ships
        self.ship_size = ship_size
        self.ship_speed = ship_speed

        self.world = self._random_world()
        self.moves = []

        self.initial_world = self.world.to_dict()

    def _random_world(self):
        random.seed(self.random_seed)

        # generate some random ships
        ships = []
        while len(ships) < self.num_ships:
            random_x = random.randint(self.ship_size, self.width - self.ship_size)
            random_y = random.randint(self.ship_size, self.height - self.ship_size)
            random_location = Location(random_x, random_y)

            # make sure this location does not collide with existing ships
            valid_location = True
            for ship in ships:
                if ship.location.distance_to(random_location) < self.ship_size:
                    valid_location = False

            if valid_location:
                random_orientation = random.randint(0, 359)
                uid = str(len(ships) + 1)
                ships.append(Ship(uid, random_location, random_orientation, self.ship_size, self.ship_speed))

        # create the world
        return World(self.width, self.height, ships)

    def run(self):
        pass

    def save(self, file_path):
        data = {
            'random_seed': self.random_seed,
            'width': self.width,
            'height': self.height,
            'num_ships': self.num_ships,
            'ship_size': self.ship_size,
            'ship_speed': self.ship_speed,
            'initial_world': self.initial_world,
            'moves': [move.to_dict() for move in self.moves]
        }
        with open(file_path, 'w') as file:
            file.write(json.dumps(data, indent=2))