from pico2d import *
import gfw_image
from gobj import *
import helper

class Skell:

    image = None

    def __init__(self):
       
       self.pos1 = 350,340
       self.pos2 = 400,410
       self.action = 3
       self.fidx = 1
       self.delta = 0,0
       self.target = None
       self.targets = []
       if Skell.image == None:
            Skell.image = gfw_image.load(RES_DIR + '/Skeleton.png')
    def update(self):
        pass

    def draw(self):
        sx = self.fidx * 100
        sy = self. action * 100
        self.image.clip_draw(0, sy,100,100, *self.pos1,75,75)
        self.image.clip_draw(0, sy,100,100, *self.pos2,75,75)
