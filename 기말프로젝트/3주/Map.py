from pico2d import *
import gfw

class SecondMap:
    def __init__(self):
        #self.image = load_image(RES_DIR + '/basic map.png')
        self.image = gfw.image.load('res/New mapping.png')
        #self.image = load_image(RES_DIR + '/Last mapping.png')
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())
    def update(self):
        pass


class LastMap:
    def __init__(self):
        #self.image = load_image(RES_DIR + '/basic map.png')
        #self.image = load_image(RES_DIR + '/New mapping.png')
        self.image = gfw.image.load('..res/Last mapping.png')
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())
    def update(self):
        pass

