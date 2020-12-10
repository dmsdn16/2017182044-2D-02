import gfw
from pico2d import *
from gobj import *
from player import Player
import time
from skell import *
from stone import *
import stage2
import resetdummy

CountDown_Color = (255,255,255)
STATE_IN_GAME,STATE_GAME_OVER,CLEAR = range(3)
 

def enter():
    gfw.world.init(['skell','player','stone'])
    global map,player,skell,stone,skell2,stone2
    map = Map()
    player = Player()
    gfw.world.add(gfw.layer.player,player)
    skell = Skell()
    gfw.world.add(gfw.layer.skell,skell)
    skell2 = Skell2()
    gfw.world.add(gfw.layer.skell,skell2)
    stone = FStone()
    gfw.world.add(gfw.layer.stone,stone)
    stone2 = FStone2()
    gfw.world.add(gfw.layer.stone,stone2)

    
    global Countdown,state,bgm,vgm
    Countdown = 19
    state = STATE_IN_GAME

    bgm = load_music('res/stone.mp3')
    vgm = load_music('res/hitting.mp3')
    global game_over_image
    game_over_image = gfw.image.load('res/game over.png')

    global clear_image,success_image
    clear_image = gfw.image.load('res/clear.png')
    
    
    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 100)
    
    
def collision(a,b):

        left_a,bottom_a,right_a,top_a = a.get_bb()
        left_b,bottom_b,right_b,top_b = b.get_bb()
       
        if right_a < left_b or left_a > right_b or top_b < bottom_a or bottom_b > top_a:
            return False
        else:
            return True

    
def check_collision():
         
            global bgm
            if collision(player,skell):
               vgm.play()
               Call(skell)
               player.hit()
              
            elif collision(player,skell2):
                Call(skell2)
                vgm.play()
                player.hit()
            elif collision(player,stone):
                Call(stone)
                bgm.play()
                player.hit()
            elif collision(player,stone2):
                Call(stone2)
                bgm.play()
                player.hit()
            elif collision(stone,skell):
                gfw.world.remove(skell)
            elif collision(stone2,skell):
                gfw.world.remove(skell) 
            elif collision(stone,skell2):
                gfw.world.remove(skell2)
            elif collision(stone2,skell2):
                gfw.world.remove(skell2)
            #print(collision(player,stone))
           
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
    global Countdown ,state, C
    check_collision()
    gfw.world.update()
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
   
   if Countdown >=10:
       font.draw(*Countdown_pos,'%.1d' % Countdown,CountDown_Color)
   elif Countdown < 10:
       font.draw(*Countdown_pos,'0%.1d' % Countdown,CountDown_Color)


   
   gfw.world.draw()
   if state == STATE_GAME_OVER:
        # 화면 한 가운데를 중심으로 이미지를 출력한다.
        x, y = get_canvas_width() // 2, get_canvas_height() // 2
        game_over_image.clip_draw_to_origin(0, 0,game_over_image.w, game_over_image.h,0,0, get_canvas_width(), get_canvas_height())
        
  
   
def handle_event(e):
    global player,Countdown,state
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        a,b = player.Returnamount()
        if a== 0 and b == 0:
            Countdown -= 1
        if e.key == SDLK_r:
            gfw.change(resetdummy)
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    if state != CLEAR:
        player.handle_event(e)

    

def Call(a):
    global player
    x,y = player.ReturnAction()
   
    if x > 0 and y == 0: # 좌
         a.Lcollision()
         player.Lcollision()
       
    if x < 0 and y == 0:#우
         a.Rcollision()
         player.Rcollision()
    if x ==  0 and y > 0: # 아래
         a.Dcollision()
         player.Dcollision()

    if x == 0 and y < 0: # 위
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
