from pico2d import *
import gfw
from gobj import *
import helper

class FStone:

    image = None

    def __init__(self):
     
      self.pos1 = 355,175
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if FStone.image == None:
            FStone.image = gfw.image.load('res/stone.png')

    
       
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
       
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+45,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55

class FStone2:
    image = None

    def __init__(self):
     
      self.pos2 = 400,230
      self.Prepos2 = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if FStone2.image == None:
            FStone2.image = gfw.image.load('res/stone.png')

    
       
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
    
    image = None

    def __init__(self):
     
      self.pos1 = 500,350
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if St2stone.image == None:
            St2stone.image = gfw.image.load('res/stone.png')

    
       
    def update(self):
        
        map1 =((420,515),(460,515),\
              (380,460),(500,460),\
              (300,405),(340,405),(380,405),(540,405),\
              (260,350),(380,350),(540,350),\
              (540,295),(260,295),\
              (540,240),(340,240),(260,240),\
              (260,185),(340,185),(380,185),(460,185),(500,185),\
              (260,130),(460,130),(500,130),(540,130),\
              (260,75),(300,75),(340,75),(380,75),(420,75),(460,75),(500,75),(540,75))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
       
        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,50,55)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55

class St2stone1:
    
    image = None

    def __init__(self):
     
      self.pos1 = 460,350
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if St2stone1.image == None:
            St2stone1.image = gfw.image.load('res/stone.png')

    
       
    def update(self):
        
        map1 =((420,515),(460,515),\
              (380,460),(500,460),\
              (300,405),(340,405),(380,405),(540,405),\
              (260,350),(380,350),(540,350),\
              (540,295),(260,295),\
              (540,240),(340,240),(260,240),\
              (260,185),(340,185),(380,185),(460,185),(500,185),\
              (260,130),(460,130),(500,130),(540,130),\
              (260,75),(300,75),(340,75),(380,75),(420,75),(460,75),(500,75),(540,75))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
       

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,50,55)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55

class St2stone2:
    
    image = None

    def __init__(self):
     
      self.pos1 = 420,350
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if St2stone2.image == None:
            St2stone2.image = gfw.image.load('res/stone.png')

    
       
    def update(self):
        
        map1 =((420,515),(460,515),\
              (380,460),(500,460),\
              (300,405),(340,405),(380,405),(540,405),\
              (260,350),(380,350),(540,350),\
              (540,295),(260,295),\
              (540,240),(340,240),(260,240),\
              (260,185),(340,185),(380,185),(460,185),(500,185),\
              (260,130),(460,130),(500,130),(540,130),\
              (260,75),(300,75),(340,75),(380,75),(420,75),(460,75),(500,75),(540,75))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
     

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,50,55)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55

class St2stone3:
    
    image = None

    def __init__(self):
     
      self.pos1 = 460,295
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if St2stone3.image == None:
            St2stone3.image = gfw.image.load('res/stone.png')

    
       
    def update(self):
        
        map1 =((420,515),(460,515),\
              (380,460),(500,460),\
              (300,405),(340,405),(380,405),(540,405),\
              (260,350),(380,350),(540,350),\
              (540,295),(260,295),\
              (540,240),(340,240),(260,240),\
              (260,185),(340,185),(380,185),(460,185),(500,185),\
              (260,130),(460,130),(500,130),(540,130),\
              (260,75),(300,75),(340,75),(380,75),(420,75),(460,75),(500,75),(540,75))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,50,55)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55


class St2stone4:
    
    image = None

    def __init__(self):
     
      self.pos1 = 340,295
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if St2stone4.image == None:
            St2stone4.image = gfw.image.load('res/stone.png')

    
       
    def update(self):
        
        map1 =((420,515),(460,515),\
              (380,460),(500,460),\
              (300,405),(340,405),(380,405),(540,405),\
              (260,350),(380,350),(540,350),\
              (540,295),(260,295),\
              (540,240),(340,240),(260,240),\
              (260,185),(340,185),(380,185),(460,185),(500,185),\
              (260,130),(460,130),(500,130),(540,130),\
              (260,75),(300,75),(340,75),(380,75),(420,75),(460,75),(500,75),(540,75))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
       

        for i in range(33):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,100,100, *self.pos1,50,55)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +55

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-55


class Stone:
    image = None

    def __init__(self):
     
      self.pos1 = 240,220
     
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone.image == None:
            Stone.image = gfw.image.load('res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
       

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone1:
    image = None

    def __init__(self):
     
      self.pos1 = 280,160
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone1.image == None:
            Stone1.image = gfw.image.load('res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60


class Stone2:
    image = None

    def __init__(self):
     
      self.pos1 = 320,160
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone2.image == None:
            Stone2.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone3:
    image = None

    def __init__(self):
     
      self.pos1 = 360,160
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone3.image == None:
            Stone3.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone4:
    image = None

    def __init__(self):
     
      self.pos1 = 480,160
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone4.image == None:
            Stone4.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        
        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone5:
    image = None

    def __init__(self):
     
      self.pos1 = 520,160
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone5.image == None:
            Stone5.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone6:
    image = None

    def __init__(self):
     
      self.pos1 = 360,100
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone6.image == None:
            Stone6.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone7:
    image = None

    def __init__(self):
     
      self.pos1 = 480,100
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone7.image == None:
            Stone7.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone8:
    image = None

    def __init__(self):
     
      self.pos1 = 360,340
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone8.image == None:
            Stone8.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone9:
    image = None

    def __init__(self):
     
      self.pos1 = 440,340
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone9.image == None:
            Stone9.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone10:
    image = None

    def __init__(self):
     
      self.pos1 = 360,280
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone10.image == None:
            Stone10.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone11:
    image = None

    def __init__(self):
     
      self.pos1 = 360,220
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone11.image == None:
            Stone11.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone12:
    image = None

    def __init__(self):
     
      self.pos1 = 400,220
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone12.image == None:
            Stone12.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60

class Stone13:
    image = None

    def __init__(self):
     
      self.pos1 = 440,220
      
      self.Prepos = 0,0 # 이전 좌표
      self.delta = 0,0
      self.target = None
      self.targets = []
      if Stone13.image == None:
            Stone13.image = gfw.image.load( 'res/red.png')

    
       
    def update(self):
        
        map1 = ((360,440),(440,440),\
                (320,400),(480,400),\
                (280,340),(320,340),(480,340),(520,340),\
                (240,280),(320,280),(480,280),(560,280),\
                (200,220),(600,220),\
                (200,160),(600,160),\
                (240,100),(560,100),\
                (280,40),(320,40),(360,40),(400,40),(440,40),(480,40),(520,40))
        
        dx,dy=self.delta
      #  self.time += gfw.delta_time
      #  frame = self.time * 12
      #  self.fidx =int(frame) % 12
        x,y = self.pos1
        

        for i in range(25):
            unx1 , uny1 = map1[i] 
            if( x == unx1 and y == uny1):
                self.pos1 = self.Prepos
           
        self.Prepos = x,y

    
    def get_bb(self):
        x,y = self.pos1
        return x-10, y-10, x+10, y+10
   


    def draw(self):
        self.image.clip_draw(0, 0,200,200, *self.pos1,50,50)
      
       
       

    def Lcollision(self):
       
        x,y = self.pos1
        self.pos1 = x-40,y
   
    def Rcollision(self):
        x,y = self.pos1
        self.pos1 = x+40,y

    def Ucollision(self):
        x,y = self.pos1
        self.pos1 = x,y +60

    def Dcollision(self):
        x,y = self.pos1
        self.pos1 = x,y-60


        

   