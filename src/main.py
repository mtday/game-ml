
from model import Game


RANDOM_SEED = 1
WIDTH = 600
HEIGHT = 400
SHIPS = 5
SHIP_SIZE = 8
SHIP_SPEED = 6


if __name__ == '__main__':
    game = Game(RANDOM_SEED, WIDTH, HEIGHT, SHIPS, SHIP_SIZE, SHIP_SPEED)
    game.run()
    game.save('/tmp/game_{}.json'.format(RANDOM_SEED))


