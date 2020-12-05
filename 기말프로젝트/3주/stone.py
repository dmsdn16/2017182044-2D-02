from pico2d import *
import gfw
from gobj import *
import helper

class Stone:

    image = None

    def __init__(self):
     
      self.pos1 = 340,160
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone.image == None:
            Stone.image = gfw.image.load(RES_DIR + '/stone.png')

    
       
    def update(self):
        
        map1 = ((400,460),(340,460),(280,460),(220,400),\
               (220,340),(160,280),(160,220),(160,160),\
               (220,100),(280,100),(340,100),(400,100),(460,100),(520,100),(580,100),\
               (580,460),(580,400),(520,340),(460,520),(520,520),\
               (340,280),(400,280),(460,280),(520,280),(580,280),(580,220),(640,160))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(27):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,75,75)
      
       
       

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

class Stone2:
    image = None

    def __init__(self):
     
      self.pos2 = 400,220
      self.Prepos2 = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone2.image == None:
            Stone2.image = gfw.image.load(RES_DIR + '/stone.png')

    
       
    def update(self):
        
        map1 = ((400,460),(340,460),(280,460),(220,400),\
               (220,340),(160,280),(160,220),(160,160),\
               (220,100),(280,100),(340,100),(400,100),(460,100),(520,100),(580,100),\
               (580,460),(580,400),(520,340),(460,520),(520,520),\
               (340,280),(400,280),(460,280),(520,280),(580,280),(580,220),(640,160))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos2
        

        for i in range(27):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos2 = self.Prepos2
            
        self.Prepos2 = x,y

    
    def get_bb(self):
        x,y = self.pos2
        return x-10, y-10, x+10, y+10
   


    def draw(self):
       
        self.image.clip_draw(0, 0,100,100, *self.pos2,75,75)

       
       

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
      
        

   