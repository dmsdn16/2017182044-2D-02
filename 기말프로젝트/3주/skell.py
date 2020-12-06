from pico2d import *
import gfw
from gobj import *
import helper
from player import Player




class Skell:

    image = None

    def __init__(self):

       
       
        self.bool = 0
        self.time = 0
        self.pos1 = 355,340
        self.action = 3
        self.fidx = 1
        self.delta = 0,0
        self.target = None
        self.targets = []
        if Skell.image == None:
            Skell.image = gfw.image.load(RES_DIR + '/Skeleton.png')
        
         
            
    def update(self):
        global b
        map1 = ((220,450),(265,450),(310,450),(355,450),(400,450),(535,450),\
               (220,395),(265,395),(535,395),\
               (220,340),(265,340),(490,340),(535,340),\
               (220,285),(355,285),(400,285),(445,285),(490,285),(535,285),\
               (220,230),(535,230),\
               (220,175),(580,175),\
               (220,120),(265,120),(310,120),(35,120),(400,120),(445,120),(490,120),(535,120),(445,505),(490,505))
        dx,dy=self.delta
        self.time += gfw.delta_time
        frame = self.time * 12
        self.fidx =int(frame) % 12
        x,y = self.pos1
        b = self.bool

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                b = 1
    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-45,y
        
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+45,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55  
            
                
           
      
        
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):

        sx = self.fidx * 100
        sy = self. action * 100
        x,y = self.pos1
        if b == 0:
             self.image.clip_draw(sx, sy,100,100, *self.pos1,50,50)
        



class Skell2:

    image = None

    def __init__(self):

       
        global player

        player = Player() 
        self.bool = 0
        self.time = 0
        self.pos2 = 400,395
        self.action = 3
        self.fidx = 1
        self.delta = 0,0
        self.target = None
        self.targets = []
        if Skell2.image == None:
            Skell2.image = gfw.image.load(RES_DIR + '/Skeleton.png')
        
         
            
    def update(self):
        global c
        map1 = ((220,450),(265,450),(310,450),(355,450),(400,450),(535,450),\
               (220,395),(265,395),(535,395),\
               (220,340),(265,340),(490,340),(535,340),\
               (220,285),(355,285),(400,285),(445,285),(490,285),(535,285),\
               (220,230),(535,230),\
               (220,175),(580,175),\
               (220,120),(265,120),(310,120),(35,120),(400,120),(445,120),(490,120),(535,120),(445,505),(490,505))
        dx,dy=self.delta
        self.time += gfw.delta_time
        frame = self.time * 12
        self.fidx =int(frame) % 12
        x,y = self.pos2
        c = self.bool

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                c = 1
                
            
                
           
      
        
    def get_bb(self):
        x,y = self.pos2
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        sx = self.fidx * 100
        sy = self. action * 100
        if c == 0:
             self.image.clip_draw(sx, sy,100,100, *self.pos2,50,50)

       
       

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


class St2Skell:
    pass
class Ltskell:
    pass