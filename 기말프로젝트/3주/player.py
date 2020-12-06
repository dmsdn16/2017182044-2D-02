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
       self.pos = 520,460
       self.action = 3
       self.fidx = 5
       self.delta = 0,0
       self.target = None
       self.targets = []
       self.time =0
       
       if Player.image == None:
            Player.image = gfw.image.load(RES_DIR + '/Hero(R).png')
       self.radius = self.image.w //2

     def draw(self):
        sx = self.fidx * 100
        sy = self. action * 0
        self.image.clip_draw(sx,827,100,100, *self.pos,75,75)

     def update(self):
       map1 = ((400,460),(340,460),(280,460),(220,400),\
               (220,340),(160,280),(160,220),(160,160),\
               (220,100),(280,100),(340,100),(400,100),(460,100),(520,100),(580,100),\
               (580,460),(580,400),(520,340),(460,520),(520,520),\
               (340,280),(400,280),(460,280),(520,280),(580,280),(580,220),(640,160))
       x,y = self.pos
       dx,dy = self.delta
       self.pos = x+dx, y+dy
       self.time += gfw.delta_time
       frame = self.time * 12
       self.fidx =int(frame) % 12

       for i in range(27):
            unx1 , uny1 = map1[i]
            
            if(self.action ==1 and x +60 == unx1 and y == uny1):# 우
                self.pos =x,y
            elif(self.action ==0 and x-60 == unx1 and y == uny1): #좌
                self.pos =x,y
            elif(self.action ==5 and x == unx1 and y + 60 == uny1): # 위
                self.pos =x,y
            elif(self.action ==4 and x == unx1 and y - 60 == uny1): # 아래
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
        dx += ddx * 60
        dy += ddy * 60
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
    
     def ReturnAction(self):
         act = self.action
         return act

     def Lcollision(self):
         x,y = self.pos
         self.pos = x+60, y
    
     def Rcollision(self):
         x,y = self.pos
         self.pos = x-60, y

     def Ucollision(self):
         x,y = self.pos
         self.pos = x, y -60

     def Dcollision(self):
         x,y = self.pos
         self.pos = x, y +60
              
           
            
   
         
   
           
         


    


   
  