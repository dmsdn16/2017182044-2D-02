from pico2d import *
import gfw
from gobj import *
import helper
from player import Player




class Skell:

    image = None

    def __init__(self):

       
        global player

        player = Player() 
        self.bool = 0
        self.time = 0
        self.pos1 = 340,340
        self.action = 3
        self.fidx = 1
        self.delta = 0,0
        self.target = None
        self.targets = []
        if Skell.image == None:
            Skell.image = gfw.image.load(RES_DIR + '/Skeleton.png')
        
         
            
    def update(self):
        global b
        map1 = ((400,460),(340,460),(280,460),(220,400),\
               (220,340),(160,280),(160,220),(160,160),\
               (220,100),(280,100),(340,100),(400,100),(460,100),(520,100),(580,100),\
               (580,460),(580,400),(520,340),(460,520),(520,520),\
               (340,280),(400,280),(460,280),(520,280),(580,280),(580,220),(640,160))
        dx,dy=self.delta
        self.time += gfw.delta_time
        frame = self.time * 12
        self.fidx =int(frame) % 12
        x,y = self.pos1
        b = self.bool

        for i in range(27):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                b = 1
    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-60,y
        
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+60,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60  
            
                
           
      
        
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        sx = self.fidx * 100
        sy = self. action * 100
        if b == 0:
             self.image.clip_draw(sx, sy,100,100, *self.pos1,75,75)



class Skell2:

    image = None

    def __init__(self):

       
        global player

        player = Player() 
        self.bool = 0
        self.time = 0
        self.pos2 = 400,400
        self.action = 3
        self.fidx = 1
        self.delta = 0,0
        self.target = None
        self.targets = []
        if Skell2.image == None:
            Skell2.image = gfw.image.load(RES_DIR + '/Skeleton.png')
        
         
            
    def update(self):
        global c
        map1 = ((400,460),(340,460),(280,460),(220,400),\
               (220,340),(160,280),(160,220),(160,160),\
               (220,100),(280,100),(340,100),(400,100),(460,100),(520,100),(580,100),\
               (580,460),(580,400),(520,340),(460,520),(520,520),\
               (340,280),(400,280),(460,280),(520,280),(580,280),(580,220),(640,160))
        dx,dy=self.delta
        self.time += gfw.delta_time
        frame = self.time * 12
        self.fidx =int(frame) % 12
        x,y = self.pos2
        c = self.bool

        for i in range(27):
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
             self.image.clip_draw(sx, sy,100,100, *self.pos2,75,75)

       
       

    def Lcollision(self):
       
        x,y = self.pos2
        self.pos2 = x-60,y
        
    def Rcollision(self):
        x,y = self.pos2
        self.pos2 = x+60,y

    def Ucollision(self):
        x,y = self.pos2
        self.pos2 = x,y +60

    def Dcollision(self):
        x,y = self.pos2
        self.pos2 = x,y-60
