from pico2d import *
import gfw

class Box:
    def __init__(self):
        #self.image = load_image(RES_DIR + '/basic map.png')
        self.image = gfw.image.load('res/box.png')
        #self.image = load_image(RES_DIR + '/Last mapping.png')
        self.pos = 460,405
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw(0, 0, 200, 200,460,405,50,50)
    def update(self):
        pass
    def get_bb(self):
         
         x,y = self.pos
         return x-10,y-10,x+10,y+10 
class FBox:
    def __init__(self):
        #self.image = load_image(RES_DIR + '/basic map.png')
        self.image = gfw.image.load('res/box.png')
        #self.image = load_image(RES_DIR + '/Last mapping.png')
        self.pos = 400,340
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw(0, 0, 200, 200,400,340,50,50)
    def update(self):
        pass
    def get_bb(self):
         
         x,y = self.pos
         return x-10,y-10,x+10,y+10 
