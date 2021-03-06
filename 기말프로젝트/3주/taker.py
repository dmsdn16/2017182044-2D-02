from pico2d import *
from gobj import *
import helper
from time import sleep
import gfw




class Taker:
    
     KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
     image = None

     
     def __init__(self):
       self.pos = 500,240 # 550 420(map2), 160 150(last map)
       self.action = 3
       self.fidx = 5
       self.delta = 0,0
       self.target = None
       self.targets = []
       self.time =0
       self.x_amount = 0
       self.y_amount = 0

       global key

       key = 0
       
       if Taker.image == None:
            Taker.image = gfw.image.load(RES_DIR + '/Hero(R).png')
       self.radius = self.image.w //2

     def draw(self):
        sx = self.fidx * 100
        sy = self. action * 0
        self.image.clip_draw(sx,827,100,100, *self.pos,50,50)

     def update(self):

       map1 = ((420,515),(460,515),\
              (380,460),(500,460),\
              (300,405),(340,405),(380,405),(540,405),\
              (260,350),(380,350),(540,350),\
              (540,295),(260,295),\
              (540,240),(340,240),(260,240),\
              (260,185),(340,185),(380,185),(460,185),(500,185),\
              (260,130),(460,130),(500,130),(540,130),\
              (260,75),(300,75),(340,75),(380,75),(420,75),(460,75),(500,75),(540,75))
      
      
       x,y = self.pos
       dx,dy = self.delta
       
       if self.x_amount < 0:
           self.pos = x + 4 , y
       if self.x_amount > 0:
           self.pos = x - 4 , y
       if self.y_amount < 0:
           self.pos = x , y + 5.5
       if self.y_amount > 0:
           self.pos = x , y - 5.5
       if self.x_amount > 0:
           self.x_amount -= 4
       if self.x_amount < 0:
           self.x_amount += 4
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
            
            if(self.x_amount < 0 and x +40 == unx1 and y == uny1):# 우
                self.pos =x - 4,y
            elif(self.x_amount > 0 and x-40 == unx1 and y == uny1): #좌
                self.pos =x + 4,y
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
        dx,dy = 4, 5.5
        
      
        self.delta = dx, dy
        
   
       
     
     def handle_events(self, e):
       
         if self.x_amount == 0 and self.y_amount == 0:
             if e.type == SDL_KEYDOWN:
                
                 if e.key == SDLK_LEFT:
                     self.x_amount +=40
                     self.updateDelta()
                 elif e.key == SDLK_RIGHT:
                     self.x_amount -=40
                     self.updateDelta()
                 elif e.key == SDLK_UP:
                     self.y_amount -=55
                     self.updateDelta()
                 elif e.key == SDLK_DOWN:
                     self.y_amount +=55
                     self.updateDelta()
                
          

             

               
        #pair = (e.type, e.key)
        #if pair in Taker.KEY_MAP:
             
        #    if self.target is not None:
        #        if e.type == SDL_KEYUP: return
        #        self.target = None
        #        self.delta = 0,0
        #        self.targets = []
        #        self.speed = 0
        #    self.updateDelta(*Taker.KEY_MAP[pair])
    
     def ReturnAction(self):
         x,y = self.x_amount, self.y_amount
         return x,y

     def Lcollision(self):
        
         x,y = self.pos
         self.pos = x + 40 , y
        
    
     def Rcollision(self):
         x,y = self.pos
         self.pos = x - 40, y

     def Ucollision(self):
         
         x,y = self.pos
         self.pos = x, y -55
        

     def Dcollision(self):
         
         x,y = self.pos
         self.pos = x, y +55

     def Returnamount(self):
        x,y = self.x_amount, self.y_amount
        return x,y

     def Takekey(self):
         global key
         key += 1
     def Returnkey(self):
         global key
         return key
         
   
           
         


    


   
  