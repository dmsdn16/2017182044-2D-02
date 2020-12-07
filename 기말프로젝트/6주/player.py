from pico2d import *
from gobj import *
import helper
from time import sleep
import gfw




class Player:
  
     KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
     image = None

     def __init__(self):
       self.pos = 490,450#490,450 # 550 420(map2), 160 150(last map)
       self.action = 3
       self.fidx = 5
       self.delta = 0,0
       self.target = None
       self.targets = []
       self.time =0
       self.x_amount = 0
       self.y_amount = 0
       
       if Player.image == None:
            Player.image = gfw.image.load('res/Hero(R).png')
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
       
       if self.x_amount < 0:
           self.pos = x + 4.5 , y
       if self.x_amount > 0:
           self.pos = x - 4.5 , y
       if self.y_amount < 0:
           self.pos = x , y + 5.5
       if self.y_amount > 0:
           self.pos = x , y - 5.5
       if self.x_amount > 0:
           self.x_amount -= 4.5
       if self.x_amount < 0:
           self.x_amount += 4.5
       if self.y_amount > 0:
           self.y_amount -= 5.5
       if self.y_amount < 0:
           self.y_amount += 5.5
      
       #self.pos = x+dx, y+dy
       self.time += gfw.delta_time
       frame = self.time * 12
       self.fidx =int(frame) % 12

       for i in range(33):
            unx1 , uny1 = map1[i]
            
            if(self.x_amount < 0 and x +45 == unx1 and y == uny1):# 우
                self.pos =x - 4.5,y
            elif(self.x_amount > 0 and x-45 == unx1 and y == uny1): #좌
                self.pos =x + 4.5,y
            elif(self.y_amount < 0 and x == unx1 and y + 55 == uny1): # 위
                self.pos =x, y - 5.5  
            elif(self.y_amount > 0 and x == unx1 and y - 55 == uny1): # 아래
                self.pos =x, y + 5.5
            
       
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

   
     def updateDelta(self):
        dx,dy = 4.5, 5.5
       
        self.delta = dx, dy
        
   
       
     
     def handle_event(self, e):
       
         if self.x_amount == 0 and self.y_amount == 0:
             if e.type == SDL_KEYDOWN:
                
                 if e.key == SDLK_LEFT:
                     self.x_amount +=45
                     self.updateDelta()
                 elif e.key == SDLK_RIGHT:
                     self.x_amount -=45
                     self.updateDelta()
                 elif e.key == SDLK_UP:
                     self.y_amount -=55
                     self.updateDelta()
                 elif e.key == SDLK_DOWN:
                     self.y_amount +=55
                     self.updateDelta()
                
          

             

               
        #pair = (e.type, e.key)
        #if pair in Player.KEY_MAP:
             
        #    if self.target is not None:
        #        if e.type == SDL_KEYUP: return
        #        self.target = None
        #        self.delta = 0,0
        #        self.targets = []
        #        self.speed = 0
        #    self.updateDelta(*Player.KEY_MAP[pair])
    
     def ReturnAction(self):
         x,y = self.x_amount, self.y_amount
         return x,y

     def Lcollision(self):
        
         x,y = self.pos
         self.pos = x + 45 , y
        
    
     def Rcollision(self):
         x,y = self.pos
         self.pos = x - 45, y

     def Ucollision(self):
         
         x,y = self.pos
         self.pos = x, y -55
        

     def Dcollision(self):
         
         x,y = self.pos
         self.pos = x, y +55

     def Returnamount(self):
        x,y = self.x_amount, self.y_amount
        return x,y

   
           
         


    


   
  