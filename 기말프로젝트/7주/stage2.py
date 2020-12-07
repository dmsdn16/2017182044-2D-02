import gfw
from pico2d import *
from Map import *
from taker import Taker
import time
from skell import *
from stone import *
from key import Key
from box import Box
import final
import dummy

CountDown_Color = (255,255,255)
STATE_IN_GAME,STATE_GAME_OVER,CLEAR = range(3)
 

def enter():
    gfw.world.init(['skell','taker','stone','key','box'])
    global map,player,skell,skell1,stone,stone1,skell2,stone2,stone3,stone4,taker,key
    map = SecondMap()
    taker = Taker()
    gfw.world.add(gfw.layer.taker,taker)
    stone = St2stone()
    gfw.world.add(gfw.layer.stone,stone)
    stone1 = St2stone1()
    gfw.world.add(gfw.layer.stone,stone1)
    stone2 = St2stone2()
    gfw.world.add(gfw.layer.stone,stone2)
    stone3 = St2stone3()
    gfw.world.add(gfw.layer.stone,stone3)
    stone4 = St2stone4()
    gfw.world.add(gfw.layer.stone,stone4)
    skell = St2Skell()
    gfw.world.add(gfw.layer.skell,skell)
    skell1 = St2Skell1()
    gfw.world.add(gfw.layer.skell,skell1)
    skell2 = St2Skell2()
    gfw.world.add(gfw.layer.skell,skell2)
    key = Key()
    gfw.world.add(gfw.layer.key,key)

    global box
    box = Box()
    gfw.world.add(gfw.layer.box,box)

    global Countdown,state,bgm,vgm
    Countdown = 33
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
         
            global taker
            x,y = taker.Returnamount()
  
            z = taker.Returnkey()

           
            if collision(taker,skell):
               Call(skell)
               vgm.play()
               if collision(skell,stone):
                   gfw.world.remove(skell)
                   skell.pos_init()
               elif collision(skell,stone1):
                   gfw.world.remove(skell)
                   skell.pos_init()
               elif collision(skell,stone2):
                   gfw.world.remove(skell)
                   skell.pos_init()
               elif collision(skell,stone3):
                   gfw.world.remove(skell)
                   skell.pos_init()
               elif collision(skell,stone4):
                   gfw.world.remove(skell)
                   skell.pos_init()
               elif collision(skell,skell1):
                   gfw.world.remove(skell)
                   skell.pos_init()
               elif collision(skell,skell2):
                   gfw.world.remove(skell)
                   skell.pos_init()
            elif collision(taker,skell1):
                Call(skell1)
                vgm.play()
                if collision(skell1,stone):
                   gfw.world.remove(skell1)
                elif collision(skell1,stone1):
                   gfw.world.remove(skell1)
                elif collision(skell1,stone2):
                   gfw.world.remove(skell1)
                   skell1.pos_init()
                elif collision(skell1,stone3):
                   gfw.world.remove(skell1)
                   skell1.pos_init()
                elif collision(skell1,stone4):
                   gfw.world.remove(skell1)
                   skell1.pos_init()
                elif collision(skell1,skell):
                   gfw.world.remove(skell1)
                   skell1.pos_init()
                elif collision(skell1,skell2):
                   gfw.world.remove(skell1)
                   skell1.pos_init()
            elif collision(taker,skell2):
                Call(skell2)
                vgm.play()
                if collision(skell2,stone):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
                elif collision(skell2,stone1):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
                elif collision(skell2,stone2):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
                elif collision(skell2,stone3):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
                elif collision(skell2,stone4):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
                elif collision(skell2,skell):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
                elif collision(skell2,skell1):
                   gfw.world.remove(skell2)
                   skell2.pos_init()
            elif collision(taker,stone):
                Call(stone)
                bgm.play()
                if collision(stone,skell):
                    Reversecall(stone)
                elif collision(stone,skell1):
                     Reversecall(stone)
                elif collision(stone,skell2):
                     Reversecall(stone)
                elif collision(stone,stone1):
                     Reversecall(stone)
                elif collision(stone,stone2):
                     Reversecall(stone)
                elif collision(stone,stone3):
                     Reversecall(stone)
                elif collision(stone,stone4):
                     Reversecall(stone)
            elif collision(taker,stone1):
                Call(stone1)
                bgm.play()
                if collision(stone1,skell):
                    Reversecall(stone1)
                elif collision(stone1,skell1):
                     Reversecall(stone1)
                elif collision(stone1,skell2):
                     Reversecall(stone1)
                elif collision(stone1,stone):
                     
                     Reversecall(stone1)
                elif collision(stone1,stone2):
                     
                     Reversecall(stone1)
                elif collision(stone1,stone3):
                     
                     Reversecall(stone1)
                elif collision(stone1,stone4):
                     
                     Reversecall(stone1)
              
            elif collision(taker,stone2):
                Call(stone2)
                bgm.play()
                print(10)
                if collision(stone2,skell):
                    Reversecall(stone2)
                elif collision(stone2,skell1):
                     Reversecall(stone2)
                elif collision(stone2,skell2):
                     Reversecall(stone2)
                elif collision(stone2,stone):
                     Reversecall(stone2)
                     
                elif collision(stone2,stone1):
                     Reversecall(stone2)
                     
                elif collision(stone2,stone3):
                     Reversecall(stone2)
                     
                elif collision(stone2,stone4):
                     Reversecall(stone2)
                     
            elif collision(taker,stone3):
                Call(stone3)
                bgm.play()
                if collision(stone3,skell):
                    Reversecall(stone3)
                elif collision(stone3,skell1):
                     Reversecall(stone3)
                elif collision(stone3,skell2):
                     Reversecall(stone3)
                elif collision(stone3,stone):
                     Reversecall(stone3)
                elif collision(stone3,stone1):
                     Reversecall(stone3)
                elif collision(stone3,stone2):
                     Reversecall(stone3)
                elif collision(stone3,stone4):
                     Reversecall(stone3)

                
            
            elif collision(taker,stone4):
                Call(stone4)
                bgm.play()
                if collision(stone4,skell):
                    Reversecall(stone4)
                elif collision(stone4,skell1):
                     Reversecall(stone4)
                elif collision(stone4,skell2):
                     Reversecall(stone4)
                elif collision(stone4,stone):
                     Reversecall(stone4)
                elif collision(stone4,stone1):
                     Reversecall(stone4)
                elif collision(stone4,stone3):
                     Reversecall(stone4)
                elif collision(stone4,stone2):
                     Reversecall(stone4)


            elif collision(taker,key):
                taker.Takekey()
                gfw.world.remove(key)

            elif collision(taker,box):
                if z != 0:
                    gfw.world.remove(box)
                    box.reset()
                if x > 0 and y == 0: # 좌
                      taker.Lcollision()
                if x < 0 and y == 0: # 우
                      taker.Rcollision()
                if x == 0 and y > 0: # 아래
                      taker.Dcollision()
                if x ==  0 and y < 0: # 위
                      taker.Ucollision()

       
   

            
            elif collision(stone,skell): # 1 1
                gfw.world.remove(skell)
            elif collision(stone2,skell): # 3 1
                gfw.world.remove(skell) 
            elif collision(stone,skell2): # 1 3
                gfw.world.remove(skell2)
            elif collision(stone2,skell2): # 3 3
                gfw.world.remove(skell2) 
            elif collision(stone1,skell): # 2 1
                gfw.world.remove(skell)
            elif collision(stone3,skell): # 4 1
                gfw.world.remove(skell) 
            elif collision(stone4,skell): # 5 1
                gfw.world.remove(skell)
            elif collision(stone,skell1): # 1 2
                gfw.world.remove(skell1)
                
            elif collision(stone1,skell1): # 2 2
                gfw.world.remove(skell1)
            elif collision(stone2,skell1): # 3 2
                gfw.world.remove(skell1) 
            elif collision(stone3,skell1): # 4 2
                gfw.world.remove(skell1)
            elif collision(stone4,skell1): # 5 2
                gfw.world.remove(skell1) 
            elif collision(stone1,skell2): # 2 3
                gfw.world.remove(skell2)
            elif collision(stone3,skell2): # 4 3
                gfw.world.remove(skell2) 
            elif collision(stone4,skell2): # 5 3
                gfw.world.remove(skell2)
            

def end_game():
    global state
    state = STATE_GAME_OVER
    

def clear():
    x,y = taker.clear_check()
    return x,y

def check_clear():
    global state,Countdown
    x,y = clear()
    if Countdown > 0:
        if x==420 and y == 460:
            state = CLEAR   
 
def update():
    gfw.world.update()
    check_collision()
    check_clear()
    if Countdown == 0:
        end_game()
    elif Countdown == -1:
        gfw.change(dummy)

    
    elif state == CLEAR: 
        gfw.change(final)
  
 
def draw():
   map.draw()
   gfw.world.draw()

   Countdown_pos = 30,140
   
   if Countdown >=10:
       font.draw(*Countdown_pos,'%.1d' % Countdown,CountDown_Color)
   elif Countdown < 10:
       font.draw(*Countdown_pos,'0%.1d' % Countdown,CountDown_Color)
   
   if state == STATE_GAME_OVER:
        # 화면 한 가운데를 중심으로 이미지를 출력한다.
        x, y = get_canvas_width() // 2, get_canvas_height() // 2
        game_over_image.clip_draw_to_origin(0, 0,game_over_image.w, game_over_image.h,0,0, get_canvas_width(), get_canvas_height())
        


   
 
   
def handle_event(e):
    global taker,Countdown,state
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        a,b = taker.Returnamount()
        if a== 0 and b == 0:
            Countdown -= 1
        
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    if state != CLEAR:
        taker.handle_events(e)
        
def Call(a):
    global taker
    x,y = taker.Returnamount()
   
    if x > 0 and y == 0: # 좌
         a.Lcollision()
         taker.Lcollision()
       
    if x < 0 and y == 0:#우
         a.Rcollision()
         taker.Rcollision()
    if x ==  0 and y > 0: # 아래
         a.Dcollision()
         taker.Dcollision()

    if x == 0 and y < 0: # 위
         a.Ucollision()
         taker.Ucollision()

def Reversecall(a):
    global taker
    x,y = taker.Returnamount()
   
    if x < 0 and y == 0: # 좌
         a.Lcollision()
         
       
    if x > 0 and y == 0:#우
         a.Rcollision()
         
    if x ==  0 and y < 0: # 아래
         a.Dcollision()
         

    if x == 0 and y > 0: # 위
         a.Ucollision()
         




def exit():
    pass
def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
