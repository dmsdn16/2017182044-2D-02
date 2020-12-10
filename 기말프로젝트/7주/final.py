
import gfw
from pico2d import *
from Map import *
from taker import Hell
import time
from skell import *
from stone import *
from key import Fkey
from box import FBox
import Ending
import dummy2
import resetdummy3

CountDown_Color = (255,255,255)
STATE_IN_GAME,STATE_GAME_OVER,CLEAR = range(3)
 

def enter():
    gfw.world.init(['taker','stone','key','box'])
    global map,taker,key
    map = LastMap()
    taker = Hell()
    gfw.world.add(gfw.layer.taker,taker)

    global St,St1,St2,St3,St4,St5,St6,St7,St8,St9,St10,St11,St12,St13
    print(1)
    St = Stone()
    gfw.world.add(gfw.layer.stone,St)

    St1 = Stone1()
    gfw.world.add(gfw.layer.stone,St1)
    St2 = Stone2()
    gfw.world.add(gfw.layer.stone,St2)
    St3 = Stone3()
    gfw.world.add(gfw.layer.stone,St3)
    St4 = Stone4()
    gfw.world.add(gfw.layer.stone,St4)
    St5 = Stone5()
    gfw.world.add(gfw.layer.stone,St5)
    St6 = Stone6()
    gfw.world.add(gfw.layer.stone,St6)
    St7 = Stone7()
    gfw.world.add(gfw.layer.stone,St7)
    St8 = Stone8()
    gfw.world.add(gfw.layer.stone,St8)
    St9 = Stone9()
    gfw.world.add(gfw.layer.stone,St9)
    St10 = Stone10()
    gfw.world.add(gfw.layer.stone,St10)
    St11 = Stone11()
    gfw.world.add(gfw.layer.stone,St11)
    St12 = Stone12()
    gfw.world.add(gfw.layer.stone,St12)
    St13 = Stone13()
    gfw.world.add(gfw.layer.stone,St13)
    
    key = Fkey()
    gfw.world.add(gfw.layer.key,key)

    global box
    box = FBox()
    gfw.world.add(gfw.layer.box,box)

    global Countdown,state,bgm
    Countdown = 35
    state = STATE_IN_GAME

    bgm = load_music('res/stone.mp3')
    
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

           
           
            if collision(taker,St):
                Call(St)
                bgm.play()
                taker.hit()
                if collision(St,St1):
                     Reversecall(St)
                elif collision(St,St2):
                     Reversecall(St)
                elif collision(St,St3):
                     Reversecall(St)
                elif collision(St,St4):
                     Reversecall(St)
                elif collision(St,St5):
                     Reversecall(St)
                elif collision(St,St6):
                     Reversecall(St)
                elif collision(St,St7):
                     Reversecall(St)
                elif collision(St,St8):
                     Reversecall(St)
                elif collision(St,St9):
                     Reversecall(St)
                elif collision(St,St10):
                     Reversecall(St)
                elif collision(St,St11):
                     Reversecall(St)
                elif collision(St,St12):
                     Reversecall(St)
                elif collision(St,St13):
                     Reversecall(St)
            elif collision(taker,St1):
                Call(St1)
                bgm.play()
                taker.hit()
                if collision(St1,St):
                     Reversecall(St1)
                elif collision(St1,St2):
                     Reversecall(St1)
                elif collision(St1,St3):
                     Reversecall(St1)
                elif collision(St1,St4):
                     Reversecall(St1)
                elif collision(St1,St5):
                     Reversecall(St1)
                elif collision(St1,St6):
                     Reversecall(St1)
                elif collision(St1,St7):
                     Reversecall(St1)
                elif collision(St1,St8):
                     Reversecall(St1)
                elif collision(St1,St9):
                     Reversecall(St1)
                elif collision(St1,St10):
                     Reversecall(St1)
                elif collision(St1,St11):
                     Reversecall(St1)
                elif collision(St1,St12):
                     Reversecall(St1)
                elif collision(St1,St13):
                     Reversecall(St1)
                elif collision(St1,box):
                     Reversecall(St1)
              
            elif collision(taker,St2):
                Call(St2)
                bgm.play()
                taker.hit()
                if collision(St2,St):
                     Reversecall(St2)
                elif collision(St2,St1):
                     Reversecall(St2)
                elif collision(St2,St3):
                     Reversecall(St2)
                elif collision(St2,St4):
                     Reversecall(St2)
                elif collision(St2,St5):
                     Reversecall(St2)
                elif collision(St2,St6):
                     Reversecall(St2)
                elif collision(St2,St7):
                     Reversecall(St2)
                elif collision(St2,St8):
                     Reversecall(St2)
                elif collision(St2,St9):
                     Reversecall(St2)
                elif collision(St2,St10):
                     Reversecall(St2)
                elif collision(St2,St11):
                     Reversecall(St2)
                elif collision(St2,St12):
                     Reversecall(St2)
                elif collision(St2,St13):
                     Reversecall(St2)
                elif collision(St2,box):
                     Reversecall(St2)
            elif collision(taker,St3):
                Call(St3)
                bgm.play()
                taker.hit()
                if collision(St3,St):
                     Reversecall(St3)
                elif collision(St3,St1):
                     Reversecall(St1)
                elif collision(St3,St2):
                     Reversecall(St3)
                elif collision(St3,St4):
                     Reversecall(St3)
                elif collision(St3,St5):
                     Reversecall(St3)
                elif collision(St3,St6):
                     Reversecall(St3)
                elif collision(St3,St7):
                     Reversecall(St3)
                elif collision(St3,St8):
                     Reversecall(St3)
                elif collision(St3,St9):
                     Reversecall(St3)
                elif collision(St3,St10):
                     Reversecall(St3)
                elif collision(St3,St11):
                     Reversecall(St3)
                elif collision(St3,St12):
                     Reversecall(St3)
                elif collision(St3,St13):
                     Reversecall(St3)
                elif collision(St3,box):
                     Reversecall(St3)

                
            
            elif collision(taker,St4):
                Call(St4)
                bgm.play()
                taker.hit()
                if collision(St4,St):
                     Reversecall(St4)
                elif collision(St4,St1):
                     Reversecall(St4)
                elif collision(St4,St2):
                     Reversecall(St4)
                elif collision(St4,St3):
                     Reversecall(St4)
                elif collision(St4,St5):
                     Reversecall(St4)
                elif collision(St4,St6):
                     Reversecall(St4)
                elif collision(St4,St7):
                     Reversecall(St4)
                elif collision(St4,St8):
                     Reversecall(St4)
                elif collision(St4,St9):
                     Reversecall(St4)
                elif collision(St4,St10):
                     Reversecall(St4)
                elif collision(St4,St11):
                     Reversecall(St4)
                elif collision(St4,St12):
                     Reversecall(St4)
                elif collision(St4,St13):
                     Reversecall(St4)
                elif collision(St4,box):
                     Reversecall(St4)

            elif collision(taker,St5):
                Call(St5)
                bgm.play()
                taker.hit()
                if collision(St5,St):
                     Reversecall(St5)
                elif collision(St,St1):
                     Reversecall(St5)
                elif collision(St5,St2):
                     Reversecall(St5)
                elif collision(St5,St3):
                     Reversecall(St)
                elif collision(St5,St4):
                     Reversecall(St5)
                elif collision(St5,St6):
                     Reversecall(St5)
                elif collision(St5,St7):
                     Reversecall(St5)
                elif collision(St5,St8):
                     Reversecall(St5)
                elif collision(St5,St9):
                     Reversecall(St5)
                elif collision(St5,St10):
                     Reversecall(St5)
                elif collision(St5,St11):
                     Reversecall(St5)
                elif collision(St5,St12):
                     Reversecall(St5)
                elif collision(St5,St13):
                     Reversecall(St5)
                elif collision(St5,box):
                     Reversecall(St5)

            elif collision(taker,St6):
                Call(St6)
                bgm.play()
                taker.hit()
                if collision(St6,St):
                     Reversecall(St6)
                elif collision(St6,St1):
                     Reversecall(St6)
                elif collision(St6,St2):
                     Reversecall(St6)
                elif collision(St6,St3):
                     Reversecall(St6)
                elif collision(St6,St4):
                     Reversecall(St6)
                elif collision(St6,St5):
                     Reversecall(St6)
                elif collision(St6,St7):
                     Reversecall(St6)
                elif collision(St6,St8):
                     Reversecall(St6)
                elif collision(St6,St9):
                     Reversecall(St6)
                elif collision(St6,St10):
                     Reversecall(St6)
                elif collision(St6,St11):
                     Reversecall(St6)
                elif collision(St6,St12):
                     Reversecall(St6)
                elif collision(St6,St13):
                     Reversecall(St6)
                elif collision(St6,box):
                     Reversecall(St6)

            elif collision(taker,St7):
                Call(St7)
                bgm.play()
                taker.hit()
                if collision(St7,St):
                     Reversecall(St7)
                elif collision(St7,St1):
                     Reversecall(St7)
                elif collision(St7,St2):
                     Reversecall(St7)
                elif collision(St7,St3):
                     Reversecall(St7)
                elif collision(St7,St4):
                     Reversecall(St7)
                elif collision(St7,St5):
                     Reversecall(St7)
                elif collision(St7,St6):
                     Reversecall(St7)
                elif collision(St7,St8):
                     Reversecall(St7)
                elif collision(St7,St9):
                     Reversecall(St7)
                elif collision(St7,St10):
                     Reversecall(St7)
                elif collision(St7,St11):
                     Reversecall(St7)
                elif collision(St7,St12):
                     Reversecall(St7)
                elif collision(St7,St13):
                     Reversecall(St7)
                elif collision(St7,box):
                     Reversecall(St7)
            
            elif collision(taker,St8):
                Call(St8)
                bgm.play()
                taker.hit()
                if collision(St8,St):
                     Reversecall(St8)
                elif collision(St8,St1):
                     Reversecall(St8)
                elif collision(St8,St2):
                     Reversecall(St8)
                elif collision(St8,St3):
                     Reversecall(St8)
                elif collision(St8,St4):
                     Reversecall(St8)
                elif collision(St8,St5):
                     Reversecall(St8)
                elif collision(St8,St6):
                     Reversecall(St8)
                elif collision(St8,St7):
                     Reversecall(St8)
                elif collision(St8,St9):
                     Reversecall(St8)
                elif collision(St8,St10):
                     Reversecall(St8)
                elif collision(St8,St11):
                     Reversecall(St8)
                elif collision(St8,St12):
                     Reversecall(St8)
                elif collision(St8,St13):
                     Reversecall(St8)
                elif collision(St8,box):
                     Reversecall(St8)

            elif collision(taker,St9):
                Call(St9)
                bgm.play()
                taker.hit()
                if collision(St9,St):
                     Reversecall(St9)
                elif collision(St9,St1):
                     Reversecall(St9)
                elif collision(St9,St2):
                     Reversecall(St9)
                elif collision(St9,St3):
                     Reversecall(St9)
                elif collision(St9,St4):
                     Reversecall(St9)
                elif collision(St9,St5):
                     Reversecall(St9)
                elif collision(St9,St6):
                     Reversecall(St9)
                elif collision(St9,St7):
                     Reversecall(St9)
                elif collision(St9,St8):
                     Reversecall(St9)
                elif collision(St9,St10):
                     Reversecall(St9)
                elif collision(St9,St11):
                     Reversecall(St9)
                elif collision(St9,St12):
                     Reversecall(St9)
                elif collision(St9,St13):
                     Reversecall(St9)
                elif collision(St9,box):
                     Reversecall(St9)

            elif collision(taker,St10):
                Call(St10)
                bgm.play()
                taker.hit()
                if collision(St10,St):
                     Reversecall(St10)
                elif collision(St10,St1):
                     Reversecall(St10)
                elif collision(St10,St2):
                     Reversecall(St10)
                elif collision(St10,St3):
                     Reversecall(St10)
                elif collision(St10,St4):
                     Reversecall(St10)
                elif collision(St10,St5):
                     Reversecall(St10)
                elif collision(St10,St6):
                     Reversecall(St10)
                elif collision(St10,St7):
                     Reversecall(St10)
                elif collision(St10,St8):
                     Reversecall(St10)
                elif collision(St10,St9):
                     Reversecall(St10)
                elif collision(St10,St11):
                     Reversecall(St10)
                elif collision(St10,St12):
                     Reversecall(St10)
                elif collision(St10,St13):
                     Reversecall(St10)
                elif collision(St10,box):
                     Reversecall(St10)

            elif collision(taker,St11):
                Call(St11)
                bgm.play()
                taker.hit()
                if collision(St11,St):
                     Reversecall(St11)
                elif collision(St11,St1):
                     Reversecall(St11)
                elif collision(St11,St2):
                     Reversecall(St11)
                elif collision(St11,St3):
                     Reversecall(St11)
                elif collision(St11,St4):
                     Reversecall(St11)
                elif collision(St11,St5):
                     Reversecall(St11)
                elif collision(St11,St6):
                     Reversecall(St11)
                elif collision(St11,St7):
                     Reversecall(St11)
                elif collision(St11,St8):
                     Reversecall(St11)
                elif collision(St11,St9):
                     Reversecall(St11)
                elif collision(St11,St10):
                     Reversecall(St11)
                elif collision(St11,St12):
                     Reversecall(St11)
                elif collision(St11,St13):
                     Reversecall(St11)
                elif collision(St11,box):
                     Reversecall(St11)
            elif collision(taker,St12):
                Call(St12)
                bgm.play()
                taker.hit()
                if collision(St12,St):
                     Reversecall(St12)
                elif collision(St12,St1):
                     Reversecall(St12)
                elif collision(St12,St2):
                     Reversecall(St12)
                elif collision(St12,St3):
                     Reversecall(St12)
                elif collision(St12,St4):
                     Reversecall(St12)
                elif collision(St12,St5):
                     Reversecall(St12)
                elif collision(St12,St6):
                     Reversecall(St12)
                elif collision(St12,St7):
                     Reversecall(St12)
                elif collision(St12,St8):
                     Reversecall(St12)
                elif collision(St12,St9):
                     Reversecall(St12)
                elif collision(St12,St10):
                     Reversecall(St12)
                elif collision(St12,St11):
                     Reversecall(St12)
                elif collision(St12,St13):
                     Reversecall(St12)
                elif collision(St12,box):
                     Reversecall(St12)

            elif collision(taker,St13):
                Call(St13)
                bgm.play()
                taker.hit()
                if collision(St13,St):
                     Reversecall(St13)
                elif collision(St13,St1):
                     Reversecall(St13)
                elif collision(St13,St2):
                     Reversecall(St13)
                elif collision(St13,St3):
                     Reversecall(St13)
                elif collision(St13,St4):
                     Reversecall(St13)
                elif collision(St13,St5):
                     Reversecall(St13)
                elif collision(St13,St6):
                     Reversecall(St13)
                elif collision(St13,St7):
                     Reversecall(St13)
                elif collision(St13,St8):
                     Reversecall(St13)
                elif collision(St13,St9):
                     Reversecall(St13)
                elif collision(St13,St10):
                     Reversecall(St13)
                elif collision(St13,St12):
                     Reversecall(St13)
                elif collision(St13,St11):
                     Reversecall(St13)
                elif collision(St13,box):
                     Reversecall(St13)
            elif collision(taker,key):
                taker.Takekey()
                gfw.world.remove(key)

            elif collision(taker,box):
                if z != 0:
                    gfw.world.remove(box)
                    box.reset()
                if z== 0:
                    if x > 0 and y == 0: # 좌
                      taker.Lcollision()
                    if x < 0 and y == 0: # 우
                      taker.Rcollision()
                    if x == 0 and y > 0: # 아래
                      taker.Dcollision()
                    if x ==  0 and y < 0: # 위
                      taker.Ucollision()

                

       
   

            
           

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
        if x==400 and y == 460:
            state = CLEAR   
 
def update():
    gfw.world.update()
    check_collision()
    check_clear()
    if Countdown == 0:
        end_game()
    elif Countdown == -1:
        gfw.change(dummy2)

    
    elif state == CLEAR: 
        gfw.change(Ending)
  
 
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
        if e.key == SDLK_r:
            gfw.change(resetdummy3)
        
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
    for n in gfw.world.all_objects():
        gfw.world.remove(n)

def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
