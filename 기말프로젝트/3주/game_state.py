import gfw
from pico2d import *
from gobj import *
from player import Player
import time
from skell import Skell
#from stone import Stone

def enter():
    global map,player,skell,stone
    map = Map()
    player = Player()
    skell = Skell()
    #stone = Stone()
    
    
    
  
def update():
   player.update()
   

  
 
def draw():
   map.draw()
  # player.draw()
   skell.draw()
   
def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        time.sleep(1)
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    player.handle_event(e)
    

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
