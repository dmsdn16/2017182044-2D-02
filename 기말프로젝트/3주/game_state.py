import gfw
from pico2d import *
from gobj import *
from player import Player
import time
from skell import Skell
from stone import Stone


CountDown_Color = (255,255,255)
 

def enter():
   
    global map,player,skell,stone
    map = Map()
    player = Player()
    skell = Skell()
    stone = Stone()
    gfw.world.init(['bg','skell','player','stone'])
    gfw.world.add(gfw.layer.player,player)
    gfw.world.add(gfw.layer.skell,skell)
    
    global Countdown
    Countdown = 20
    
    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 100)
    
    
def collision(a,b):

        left_a,bottom_a,right_a,top_a = a.get_bb()
        left_b,bottom_b,right_b,top_b = b.get_bb()
        if left_a> right_b  : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False

        return True

    
def check_collision():
         
            if collision(player,skell):
                if player.ReturnAction() ==2:
                    skell.Lcollision()
                    player.Lcollision()
                if player.ReturnAction() == 3:
                    skell.Rcollision()
                    player.Rcollision()
                if player.ReturnAction() == 6:
                    skell.Dcollision()
                    player.Dcollision()

                if player.ReturnAction() == 7:
                    skell.Ucollision()
                    player.Ucollision()
                 
            print(player.ReturnAction())
            
          


    
  
def update():
    global Countdown 
    check_collision()
 #  gfw.world.update()
    player.update()
    skell.update()
    
   
   
  
 
def draw():
   Countdown_pos = 690,550
  
  # font.draw(*score_pos, 'Score : %.1f' % score, SCORE_TEXT_COLOR)
   map.draw()
   player.draw()
   skell.draw()
   stone.draw()
   font.draw(*Countdown_pos,'%.1d' % Countdown,CountDown_Color)
  # gfw.world.draw()
   
def handle_event(e):
    global player,Countdown
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        time.sleep(0.5)
        Countdown -=1
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    
        
    player.handle_event(e)


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
