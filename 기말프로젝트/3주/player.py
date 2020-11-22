from pico2d import *
from gobj import *
import helper
from time import sleep
import gfw



class Player:
     KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
     KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
     image = None

     def __init__(self):
       self.pos = 520,480
       self.action = 3
       self.fidx = 5
       self.delta = 0,0
       self.target = None
       self.targets = []
       
       
       if Player.image == None:
            Player.image = gfw.image.load(RES_DIR + '/Hero(R).png')
       self.radius = self.image.w //2

     def draw(self):
        sx = self.fidx * 100
        sy = self. action * 0
        self.image.clip_draw(sx,827,100,100, *self.pos,75,75)

     def update(self):
       x,y = self.pos
       dx,dy = self.delta
       self.pos = x+dx, y+dy
       self.fidx = (self.fidx + 1) % 8
       
       if self.target is not None:
            ddx = -self.delta[0]
            helper.move_toward_obj(self)
            if self.target == None:
                print("Removing target: ", self.targets[0], " from %d target(s)." % len(self.targets))
                del self.targets[0]
                if len(self.targets) > 0:
                    helper.set_target(self, self.targets[0])
                else:
                    self.speed = 0
     
     def get_bb(self):
         x,y = self.pos
         return x - 50, y - 50 , x + 50, y + 50 

   
     def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        dx += ddx * 10
        dy += ddy * 10
        self.delta = dx, dy
        self.delta = dx, dy
        
     
     def handle_event(self, e):
       
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
             
            if self.target is not None:
                if e.type == SDL_KEYUP: return
                self.target = None
                self.delta = 0,0
                self.targets = []
                self.speed = 0
            self.updateDelta(*Player.KEY_MAP[pair])

              
           
            
   
         
   
           
         


    


   
  