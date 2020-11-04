import gfw
from pico2d import *
from gobj import *


def enter():
    global map
    map = Map()
    
    
  
def update():
 # player.update()
 pass


def draw():
   map.draw()
   
   
  
   

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()



def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
