from pico2d import *
import gfw
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
            Skell.image = gfw.image.load(RES_DIR + '/Skeleton.png')
       self.radius = self.image.w // 2
    def update(self):
        pass

    def get_bb(self):
        x,y = self.pos1
        return x-50, y-50, x + 50, y + 50

    def draw(self):
        sx = self.fidx * 100
        sy = self. action * 100
        self.image.clip_draw(0, sy,100,100, *self.pos1,75,75)
        self.image.clip_draw(0, sy,100,100, *self.pos2,75,75)
