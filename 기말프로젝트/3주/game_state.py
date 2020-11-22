import gfw
from pico2d import *
from gobj import *
from player import Player
import time
from skell import Skell
from stone import Stone



 

def enter():
   
    global map,player,skell,stone
    map = Map()
    player = Player()
    skell = Skell()
    stone = Stone()
    gfw.world.init(['bg','skell','player','stone'])
    gfw.world.add(gfw.layer.player,player)
    gfw.world.add(gfw.layer.skell,skell)
    
   
def collision(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()
    if left_a> right_b  : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


    
  
def update():
   player.update()
   
  
 
def draw():
   map.draw()
   player.draw()
   skell.draw()
   stone.draw()
   
def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        #time.sleep(1)
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    player.handle_event(e)


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
