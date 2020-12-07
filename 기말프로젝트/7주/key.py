from pico2d import *
import gfw

class Key:
    def __init__(self):
        #self.image = load_image(RES_DIR + '/basic map.png')
        self.image = gfw.image.load('res/key.png')
        #self.image = load_image(RES_DIR + '/Last mapping.png')
        self.pos = 340,350
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw(0, 0, 160, 160,340,350,40,40)
    def update(self):
        pass
    def get_bb(self):
         
         x,y = self.pos
         return x-10,y-10,x+10,y+10 

class Fkey:
    def __init__(self):
        #self.image = load_image(RES_DIR + '/basic map.png')
        self.image = gfw.image.load('res/key.png')
        #self.image = load_image(RES_DIR + '/Last mapping.png')
        self.pos = 560,220
    def draw(self):

        global image
        image = self.image
     
        self.image.clip_draw(0, 0, 160, 160,560,220,40,40)
    def update(self):
        pass
    def get_bb(self):
         
         x,y = self.pos
         return x-10,y-10,x+10,y+10 
