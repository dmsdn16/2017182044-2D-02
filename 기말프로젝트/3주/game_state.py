import gfw
from pico2d import *
from gobj import *
from player import Player
import time
from skell import *
from stone import *
import stage2


CountDown_Color = (255,255,255)
STATE_IN_GAME,STATE_GAME_OVER,CLEAR = range(3)
 

def enter():
   
    global map,player,skell,stone,skell2,stone2
    map = Map()
    player = Player()
    skell = Skell()
    skell2 = Skell2()
    stone = Stone()
    stone2 = Stone2()
    gfw.world.init(['bg','skell','player','stone'])
    gfw.world.add(gfw.layer.player,player)
    gfw.world.add(gfw.layer.skell,skell)
    
    global Countdown,state
    Countdown = 19
    state = STATE_IN_GAME

    global game_over_image
    game_over_image = gfw.image.load('res/game over.png')

    global clear_image,success_image
    clear_image = gfw.image.load('res/clear.png')
    
    
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
               Call(skell)

            elif collision(player,skell2):
                Call(skell2)
            elif collision(player,stone):
                Call(stone)
            elif collision(player,stone2):
                Call(stone2)
            #print(player.ReturnAction())

def end_game():
    global state
    state = STATE_GAME_OVER
    

def clear():
    x,y = player.clear_check()
    return x,y

def check_clear():
    global state,Countdown
    x,y = clear()
    if Countdown > 0:
        if x==535 and y == 175:
            state = CLEAR

        

    
    
  
def update():
    global Countdown ,state
    check_collision()
 #  gfw.world.update()
    player.update()
    skell.update()
    skell2.update()
    stone.update()
    stone2.update()
    check_clear()

    if Countdown == 0:
        end_game()
    elif Countdown == -1:
        gfw.pop()

    
    elif state == CLEAR:
        gfw.change(stage2)
    
    
   
   
  
 
def draw():
   Countdown_pos = 30,140
  
  # font.draw(*score_pos, 'Score : %.1f' % score, SCORE_TEXT_COLOR)
   map.draw()
   player.draw()
   skell.draw()
   skell2.draw()
   stone.draw()
   stone2.draw()
   if Countdown >=10:
       font.draw(*Countdown_pos,'%.1d' % Countdown,CountDown_Color)
   elif Countdown < 10:
       font.draw(*Countdown_pos,'0%.1d' % Countdown,CountDown_Color)


   
  # gfw.world.draw()
   if state == STATE_GAME_OVER:
        # 화면 한 가운데를 중심으로 이미지를 출력한다.
        x, y = get_canvas_width() // 2, get_canvas_height() // 2
        game_over_image.clip_draw_to_origin(0, 0,game_over_image.w, game_over_image.h,0,0, get_canvas_width(), get_canvas_height())
        
  
   
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

def Call(a):
     if player.ReturnAction() == 2: #좌
        
         a.Lcollision()
         player.Lcollision()
     if player.ReturnAction() == 3:#우
         
         a.Rcollision()
         player.Rcollision()
     if player.ReturnAction() == 6: # 아래
         
         a.Dcollision()
         player.Dcollision()

     if player.ReturnAction() == 7: # 위
         
         a.Ucollision()
         player.Ucollision()

def exit():
    pass
def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
