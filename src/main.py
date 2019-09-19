
from model import Game


RANDOM_SEED = 1
WORLD_WIDTH = 600
WORLD_HEIGHT = 400
SHIPS = 5
SHIP_SIZE = 8
SHIP_SPEED = 6


if __name__ == '__main__':
    game = Game(RANDOM_SEED, WORLD_WIDTH, WORLD_HEIGHT, SHIPS, SHIP_SIZE, SHIP_SPEED)
    game.run()
    game.save('/tmp/game_{}.json'.format(RANDOM_SEED))


