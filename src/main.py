
from model import Location
from model import Ship
from model import World

import random


WIDTH = 600
HEIGHT = 400
SHIP_SIZE = 8
SHIPS = 5

ships = []
for i in range(SHIPS):
    location = Location(random.randint(WIDTH), random.randint(HEIGHT))
    orientation = int(random.random() * 360)
    ships.append(Ship(SHIP_SIZE, location, orientation))

world = World(
    WIDTH,
    HEIGHT,
    ships
)



