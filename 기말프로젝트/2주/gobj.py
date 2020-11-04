import random
from pico2d import *

RES_DIR = '../res'

def rand(val):
    return val * random.uniform(0.9, 1.1)

class Map:
    def __init__(self):
        self.image = load_image(RES_DIR + '/basic map.png')
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass


if __name__ == "__main__":
	print("Running test code ^_^")
