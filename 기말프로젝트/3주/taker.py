from pico2d import *
from gobj import *
import helper
from time import sleep
import gfw




class Taker:
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
       self.pos = 490,175 # 550 420(map2), 160 150(last map)
       self.action = 3
       self.fidx = 5
       self.delta = 0,0
       self.target = None
       self.targets = []
       self.time =0
       
       if Taker.image == None:
            Taker.image = gfw.image.load(RES_DIR + '/Hero(R).png')
       self.radius = self.image.w //2

     def draw(self):
        sx = self.fidx * 100
        sy = self. action * 0
        self.image.clip_draw(sx,827,100,100, *self.pos,50,50)

     def update(self):

       map1 = ((220,450),(265,450),(310,450),(355,450),(400,450),(535,450),\
               (220,395),(265,395),(535,395),\
               (220,340),(265,340),(490,340),(535,340),\
               (220,285),(355,285),(400,285),(445,285),(490,285),(535,285),\
               (220,230),(535,230),\
               (220,175),(580,175),\
               (220,120),(265,120),(310,120),(35,120),(400,120),(445,120),(490,120),(535,120),\
               (445,505),(490,505))

       x,y = self.pos
       dx,dy = self.delta
       print(dx,dy)
       self.pos = x+dx, y+dy
       self.time += gfw.delta_time
       frame = self.time * 12
       self.fidx =int(frame) % 12

       for i in range(33):
            unx1 , uny1 = map1[i]
            
            if(self.action ==1 and x +45 == unx1 and y == uny1):# 우
                self.pos =x,y
            elif(self.action ==0 and x-45 == unx1 and y == uny1): #좌
                self.pos =x,y
            elif(self.action ==5 and x == unx1 and y + 55 == uny1): # 위
                self.pos =x,y
            elif(self.action ==4 and x == unx1 and y - 55 == uny1): # 아래
                self.pos =x,y
            
       
       if self.target is not None:
            ddx = -self.delta[0]
            helper.move_toward_obj(self)
            if self.target == None:
                del self.targets[0]
                if len(self.targets) > 0:
                    helper.set_target(self, self.targets[0])
                    self.updateAction(self.delta[0],0)
                else:
                    self.speed = 0
                    self.updateAction(0, ddx)
     
     def get_bb(self):
         x,y = self.pos
         return x-10,y-10,x+10,y+10 
     
     def clear_check(self):
         x,y = self.pos
         return x,y

   
     def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        dx += ddx * 45
        dy += ddy * 55
        if ddx != 0:
            self.updateAction(dx, ddx)
        if ddy !=0:
            self.updateActionY(dy,ddy)
        self.delta = dx, dy
        
     def updateAction(self, dx, ddx):
        self.action = \
            0 if dx < 0 else \
            1 if dx > 0 else \
            2 if ddx > 0 else 3
        

     def updateActionY(self,dy,ddy):
        self.action = \
            4 if dy < 0 else \
            5 if dy >0 else \
            6 if ddy > 0 else 7
       
     
     def handle_events(self, e):
       
        pair = (e.type, e.key)
        if pair in Taker.KEY_MAP:
             
            if self.target is not None:
                if e.type == SDL_KEYUP: return
                self.target = None
                self.delta = 0,0
                self.targets = []
                self.speed = 0
            self.updateDelta(*Taker.KEY_MAP[pair])
    
     def ReturnAction(self):
         act = self.action
         return act

     def Lcollision(self):
         x,y = self.pos
         self.pos = x+45, y
    
     def Rcollision(self):
         x,y = self.pos
         self.pos = x-45, y

     def Ucollision(self):
         x,y = self.pos
         self.pos = x, y -55

     def Dcollision(self):
         x,y = self.pos
         self.pos = x, y +55

   
           
         


    


   
  