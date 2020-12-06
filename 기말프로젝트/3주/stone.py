from pico2d import *
import gfw
from gobj import *
import helper

class Stone:

    image = None

    def __init__(self):
     
      self.pos1 = 355,175
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone.image == None:
            Stone.image = gfw.image.load(RES_DIR + '/stone.png')

    
       
    def update(self):
        
        map1 = ((220,450),(265,450),(310,450),(355,450),(400,450),(535,450),\
               (220,395),(265,395),(535,395),\
               (220,340),(265,340),(490,340),(535,340),\
               (220,285),(355,285),(400,285),(445,285),(490,285),(535,285),\
               (220,230),(535,230),\
               (220,175),(580,175),\
               (220,120),(265,120),(310,120),(35,120),(400,120),(445,120),(490,120),(535,120),(445,505),(490,505))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        print(self.pos1)

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-45,y
        print(self.pos1)
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+45,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55

class Stone2:
    image = None

    def __init__(self):
     
      self.pos2 = 400,230
      self.Prepos2 = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone2.image == None:
            Stone2.image = gfw.image.load(RES_DIR + '/stone.png')

    
       
    def update(self):
        
        map1 = ((220,450),(265,450),(310,450),(355,450),(400,450),(535,450),\
               (220,395),(265,395),(535,395),\
               (220,340),(265,340),(490,340),(535,340),\
               (220,285),(355,285),(400,285),(445,285),(490,285),(535,285),\
               (220,230),(535,230),\
               (220,175),(580,175),\
               (220,120),(265,120),(310,120),(35,120),(400,120),(445,120),(490,120),(535,120),(445,505),(490,505))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos2
        

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos2 = self.Prepos2
            
        self.Prepos2 = x,y

    
    def get_bb(self):
        x,y = self.pos2
        return x-5, y-5, x+5, y+5
   


    def draw(self):
       
        self.image.clip_draw(0, 0,100,100, *self.pos2,50,50)

       
       

    def Lcollision(self):
       
        x,y = self.pos2
        self.pos2 = x-45,y
        
    def Rcollision(self):
        x,y = self.pos2
        self.pos2 = x+45,y

    def Ucollision(self):
        x,y = self.pos2
        self.pos2 = x,y +55

    def Dcollision(self):
        x,y = self.pos2
        self.pos2 = x,y-55
      
class St2stone:
    pass

class Ltstone:
    pass
        

   