from pico2d import *
import gfw
from gobj import *
import helper

class Stone:

    image = None

    def __init__(self):
      self.pos1 = 340,150
      self.pos2 = 400,210
      self.post = 460,520
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone.image == None:
            Stone.image = gfw.image.load(RES_DIR + '/stone.png')

    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,75,75)
        self.image.clip_draw(0, 0,100,100, *self.pos2,75,75)
        self.image.clip_draw(0, 0,100,100, *self.post,75,75)
        

   