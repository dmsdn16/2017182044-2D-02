import random
from pico2d import *

RES_DIR = 'res'

def rand(val):
    return val * random.uniform(0.9, 1.1)

class Map:
    def __init__(self):
        self.image = load_image( 'res/basic map.png')
        #self.image = load_image(RES_DIR + '/New mapping.png')
        #self.image = load_image(RES_DIR + '/Last mapping.png')
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())
    def update(self):
        pass


if __name__ == "__main__":
	print("Running test code ^_^")
