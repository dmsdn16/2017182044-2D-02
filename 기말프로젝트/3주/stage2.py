import gfw
from pico2d import *
from Map import *
from taker import Taker
import time
from skell import *
from stone import *



CountDown_Color = (255,255,255)
STATE_IN_GAME,STATE_GAME_OVER,CLEAR = range(3)
 

def enter():
    gfw.world.init(['skell','taker','stone'])
    global map,player,skell,stone,skell2,stone2,taker
    map = SecondMap()
    taker = Taker()
    gfw.world.add(gfw.layer.taker,taker)

   
 
def update():
    gfw.world.update()
   
  
 
def draw():
   map.draw()
   taker.draw()
   

   
 
   
def handle_event(e):
    global taker
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        time.sleep(0.5)
        
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    taker.handle_events(e)
        
   



def exit():
    pass
def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
