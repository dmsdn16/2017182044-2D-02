
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


CountDown_Color = (255,255,255)
STATE_IN_GAME,STATE_GAME_OVER,CLEAR = range(3)
 

def enter():
    gfw.world.init(['skell','taker','stone','key','box'])
    global map,taker,key
    map = LastMap()
    taker = Hell()
    gfw.world.add(gfw.layer.taker,taker)
    global LS,LS1,LS2,LS3,LS4,LS5,LS6,LS7,LS8,LS9,LS10,LS11,LS12,LS13
    LS = LS()
    gfw.world.add(gfw.layer.stone,LS)
    LS1 = LS1()
    gfw.world.add(gfw.layer.stone,LS1)
    LS2 = LS2()
    gfw.world.add(gfw.layer.stone,LS2)
    LS3 = LS3()
    gfw.world.add(gfw.layer.stone,LS3)
    LS4 = LS4()
    gfw.world.add(gfw.layer.stone,LS4)
    LS5 = LS5()
    gfw.world.add(gfw.layer.stone,LS5)
    LS6 = LS6()
    gfw.world.add(gfw.layer.stone,LS6)
    LS7 = LS7()
    gfw.world.add(gfw.layer.stone,LS7)
    LS8 = LS8()
    gfw.world.add(gfw.layer.stone,LS8)
    LS9 = LS9()
    gfw.world.add(gfw.layer.stone,LS9)
    LS10 = LS10()
    gfw.world.add(gfw.layer.stone,LS10)
    LS11 = LS11()
    gfw.world.add(gfw.layer.stone,LS11)
    LS12 = LS12()
    gfw.world.add(gfw.layer.stone,LS12)
    LS13 = LS13()
    gfw.world.add(gfw.layer.stone,LS13)
    
    key = Fkey()
    gfw.world.add(gfw.layer.key,key)

    global box
    box = FBox()
    gfw.world.add(gfw.layer.box,box)

    global Countdown,state,bgm
    Countdown = 34
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

           
           
            if collision(taker,LS):
                Call(LS)
                bgm.play()
                if collision(LS,LS1):
                     Reversecall(LS)
                elif collision(LS,LS2):
                     Reversecall(LS)
                elif collision(LS,LS3):
                     Reversecall(LS)
                elif collision(LS,LS4):
                     Reversecall(LS)
                elif collision(LS,LS5):
                     Reversecall(LS)
                elif collision(LS,LS6):
                     Reversecall(LS)
                elif collision(LS,LS7):
                     Reversecall(LS)
                elif collision(LS,LS8):
                     Reversecall(LS)
                elif collision(LS,LS9):
                     Reversecall(LS)
                elif collision(LS,LS10):
                     Reversecall(LS)
                elif collision(LS,LS11):
                     Reversecall(LS)
                elif collision(LS,LS12):
                     Reversecall(LS)
                elif collision(LS,LS13):
                     Reversecall(LS)
            elif collision(taker,LS1):
                Call(LS1)
                bgm.play()
                if collision(LS1,LS):
                     Reversecall(LS1)
                elif collision(LS1,LS2):
                     Reversecall(LS1)
                elif collision(LS1,LS3):
                     Reversecall(LS1)
                elif collision(LS1,LS4):
                     Reversecall(LS1)
                elif collision(LS1,LS5):
                     Reversecall(LS1)
                elif collision(LS1,LS6):
                     Reversecall(LS1)
                elif collision(LS1,LS7):
                     Reversecall(LS1)
                elif collision(LS1,LS8):
                     Reversecall(LS1)
                elif collision(LS1,LS9):
                     Reversecall(LS1)
                elif collision(LS1,LS10):
                     Reversecall(LS1)
                elif collision(LS1,LS11):
                     Reversecall(LS1)
                elif collision(LS1,LS12):
                     Reversecall(LS1)
                elif collision(LS1,LS13):
                     Reversecall(LS1)
                elif collision(LS1,box):
                     Reversecall(LS1)
              
            elif collision(taker,LS2):
                Call(LS2)
                bgm.play()
                if collision(LS2,LS):
                     Reversecall(LS2)
                elif collision(LS2,LS1):
                     Reversecall(LS2)
                elif collision(LS2,LS3):
                     Reversecall(LS2)
                elif collision(LS2,LS4):
                     Reversecall(LS2)
                elif collision(LS2,LS5):
                     Reversecall(LS2)
                elif collision(LS2,LS6):
                     Reversecall(LS2)
                elif collision(LS2,LS7):
                     Reversecall(LS2)
                elif collision(LS2,LS8):
                     Reversecall(LS2)
                elif collision(LS2,LS9):
                     Reversecall(LS2)
                elif collision(LS2,LS10):
                     Reversecall(LS2)
                elif collision(LS2,LS11):
                     Reversecall(LS2)
                elif collision(LS2,LS12):
                     Reversecall(LS2)
                elif collision(LS2,LS13):
                     Reversecall(LS2)
                elif collision(LS2,box):
                     Reversecall(LS2)
            elif collision(taker,LS3):
                Call(LS3)
                bgm.play()
                if collision(LS3,LS):
                     Reversecall(LS3)
                elif collision(LS3,LS1):
                     Reversecall(LS1)
                elif collision(LS3,LS2):
                     Reversecall(LS3)
                elif collision(LS3,LS4):
                     Reversecall(LS3)
                elif collision(LS3,LS5):
                     Reversecall(LS3)
                elif collision(LS3,LS6):
                     Reversecall(LS3)
                elif collision(LS3,LS7):
                     Reversecall(LS3)
                elif collision(LS3,LS8):
                     Reversecall(LS3)
                elif collision(LS3,LS9):
                     Reversecall(LS3)
                elif collision(LS3,LS10):
                     Reversecall(LS3)
                elif collision(LS3,LS11):
                     Reversecall(LS3)
                elif collision(LS3,LS12):
                     Reversecall(LS3)
                elif collision(LS3,LS13):
                     Reversecall(LS3)
                elif collision(LS3,box):
                     Reversecall(LS3)

                
            
            elif collision(taker,LS4):
                Call(LS4)
                bgm.play()
                if collision(LS4,LS):
                     Reversecall(LS4)
                elif collision(LS4,LS1):
                     Reversecall(LS4)
                elif collision(LS4,LS2):
                     Reversecall(LS4)
                elif collision(LS4,LS3):
                     Reversecall(LS4)
                elif collision(LS4,LS5):
                     Reversecall(LS4)
                elif collision(LS4,LS6):
                     Reversecall(LS4)
                elif collision(LS4,LS7):
                     Reversecall(LS4)
                elif collision(LS4,LS8):
                     Reversecall(LS4)
                elif collision(LS4,LS9):
                     Reversecall(LS4)
                elif collision(LS4,LS10):
                     Reversecall(LS4)
                elif collision(LS4,LS11):
                     Reversecall(LS4)
                elif collision(LS4,LS12):
                     Reversecall(LS4)
                elif collision(LS4,LS13):
                     Reversecall(LS4)
                elif collision(LS4,box):
                     Reversecall(LS4)

            elif collision(taker,LS5):
                Call(LS4)
                bgm.play()
                if collision(LS5,LS):
                     Reversecall(LS5)
                elif collision(LS,LS1):
                     Reversecall(LS5)
                elif collision(LS5,LS2):
                     Reversecall(LS5)
                elif collision(LS5,LS3):
                     Reversecall(LS)
                elif collision(LS5,LS4):
                     Reversecall(LS5)
                elif collision(LS5,LS6):
                     Reversecall(LS5)
                elif collision(LS5,LS7):
                     Reversecall(LS5)
                elif collision(LS5,LS8):
                     Reversecall(LS5)
                elif collision(LS5,LS9):
                     Reversecall(LS5)
                elif collision(LS5,LS10):
                     Reversecall(LS5)
                elif collision(LS5,LS11):
                     Reversecall(LS5)
                elif collision(LS5,LS12):
                     Reversecall(LS5)
                elif collision(LS5,LS13):
                     Reversecall(LS5)
                elif collision(LS5,box):
                     Reversecall(LS5)

            elif collision(taker,LS6):
                Call(LS6)
                bgm.play()
                if collision(LS6,LS):
                     Reversecall(LS6)
                elif collision(LS6,LS1):
                     Reversecall(LS6)
                elif collision(LS6,LS2):
                     Reversecall(LS6)
                elif collision(LS6,LS3):
                     Reversecall(LS6)
                elif collision(LS6,LS4):
                     Reversecall(LS6)
                elif collision(LS6,LS5):
                     Reversecall(LS6)
                elif collision(LS6,LS7):
                     Reversecall(LS6)
                elif collision(LS6,LS8):
                     Reversecall(LS6)
                elif collision(LS6,LS9):
                     Reversecall(LS6)
                elif collision(LS6,LS10):
                     Reversecall(LS6)
                elif collision(LS6,LS11):
                     Reversecall(LS6)
                elif collision(LS6,LS12):
                     Reversecall(LS6)
                elif collision(LS6,LS13):
                     Reversecall(LS6)
                elif collision(LS6,box):
                     Reversecall(LS6)

            elif collision(taker,LS7):
                Call(LS7)
                bgm.play()
                if collision(LS7,LS):
                     Reversecall(LS7)
                elif collision(LS7,LS1):
                     Reversecall(LS7)
                elif collision(LS7,LS2):
                     Reversecall(LS7)
                elif collision(LS7,LS3):
                     Reversecall(LS7)
                elif collision(LS7,LS4):
                     Reversecall(LS7)
                elif collision(LS7,LS5):
                     Reversecall(LS7)
                elif collision(LS7,LS6):
                     Reversecall(LS7)
                elif collision(LS7,LS8):
                     Reversecall(LS7)
                elif collision(LS7,LS9):
                     Reversecall(LS7)
                elif collision(LS7,LS10):
                     Reversecall(LS7)
                elif collision(LS7,LS11):
                     Reversecall(LS7)
                elif collision(LS7,LS12):
                     Reversecall(LS7)
                elif collision(LS7,LS13):
                     Reversecall(LS7)
                elif collision(LS7,box):
                     Reversecall(LS7)
            
            elif collision(taker,LS8):
                Call(LS8)
                bgm.play()
                if collision(LS8,LS):
                     Reversecall(LS8)
                elif collision(LS8,LS1):
                     Reversecall(LS8)
                elif collision(LS8,LS2):
                     Reversecall(LS8)
                elif collision(LS8,LS3):
                     Reversecall(LS8)
                elif collision(LS8,LS4):
                     Reversecall(LS8)
                elif collision(LS8,LS5):
                     Reversecall(LS8)
                elif collision(LS8,LS6):
                     Reversecall(LS8)
                elif collision(LS8,LS7):
                     Reversecall(LS8)
                elif collision(LS8,LS9):
                     Reversecall(LS8)
                elif collision(LS8,LS10):
                     Reversecall(LS8)
                elif collision(LS8,LS11):
                     Reversecall(LS8)
                elif collision(LS8,LS12):
                     Reversecall(LS8)
                elif collision(LS8,LS13):
                     Reversecall(LS8)
                elif collision(LS8,box):
                     Reversecall(LS8)

            elif collision(taker,LS9):
                Call(LS9)
                bgm.play()
                if collision(LS9,LS):
                     Reversecall(LS9)
                elif collision(LS9,LS1):
                     Reversecall(LS9)
                elif collision(LS9,LS2):
                     Reversecall(LS9)
                elif collision(LS9,LS3):
                     Reversecall(LS9)
                elif collision(LS9,LS4):
                     Reversecall(LS9)
                elif collision(LS9,LS5):
                     Reversecall(LS9)
                elif collision(LS9,LS6):
                     Reversecall(LS9)
                elif collision(LS9,LS7):
                     Reversecall(LS9)
                elif collision(LS9,LS8):
                     Reversecall(LS9)
                elif collision(LS9,LS10):
                     Reversecall(LS9)
                elif collision(LS9,LS11):
                     Reversecall(LS9)
                elif collision(LS9,LS12):
                     Reversecall(LS9)
                elif collision(LS9,LS13):
                     Reversecall(LS9)
                elif collision(LS9,box):
                     Reversecall(LS9)

            elif collision(taker,LS10):
                Call(LS10)
                bgm.play()
                if collision(LS10,LS):
                     Reversecall(LS10)
                elif collision(LS10,LS1):
                     Reversecall(LS10)
                elif collision(LS10,LS2):
                     Reversecall(LS10)
                elif collision(LS10,LS3):
                     Reversecall(LS10)
                elif collision(LS10,LS4):
                     Reversecall(LS10)
                elif collision(LS10,LS5):
                     Reversecall(LS10)
                elif collision(LS10,LS6):
                     Reversecall(LS10)
                elif collision(LS10,LS7):
                     Reversecall(LS10)
                elif collision(LS10,LS8):
                     Reversecall(LS10)
                elif collision(LS10,LS9):
                     Reversecall(LS10)
                elif collision(LS10,LS11):
                     Reversecall(LS10)
                elif collision(LS10,LS12):
                     Reversecall(LS10)
                elif collision(LS10,LS13):
                     Reversecall(LS10)
                elif collision(LS10,box):
                     Reversecall(LS10)

            elif collision(taker,LS11):
                Call(LS11)
                bgm.play()
                if collision(LS11,LS):
                     Reversecall(LS11)
                elif collision(LS11,LS1):
                     Reversecall(LS11)
                elif collision(LS11,LS2):
                     Reversecall(LS11)
                elif collision(LS11,LS3):
                     Reversecall(LS11)
                elif collision(LS11,LS4):
                     Reversecall(LS11)
                elif collision(LS11,LS5):
                     Reversecall(LS11)
                elif collision(LS11,LS6):
                     Reversecall(LS11)
                elif collision(LS11,LS7):
                     Reversecall(LS11)
                elif collision(LS11,LS8):
                     Reversecall(LS11)
                elif collision(LS11,LS9):
                     Reversecall(LS11)
                elif collision(LS11,LS10):
                     Reversecall(LS11)
                elif collision(LS11,LS12):
                     Reversecall(LS11)
                elif collision(LS11,LS13):
                     Reversecall(LS11)
                elif collision(LS11,box):
                     Reversecall(LS11)
            elif collision(taker,LS12):
                Call(LS12)
                bgm.play()
                if collision(LS12,LS):
                     Reversecall(LS12)
                elif collision(LS12,LS1):
                     Reversecall(LS12)
                elif collision(LS12,LS2):
                     Reversecall(LS12)
                elif collision(LS12,LS3):
                     Reversecall(LS12)
                elif collision(LS12,LS4):
                     Reversecall(LS12)
                elif collision(LS12,LS5):
                     Reversecall(LS12)
                elif collision(LS12,LS6):
                     Reversecall(LS12)
                elif collision(LS12,LS7):
                     Reversecall(LS12)
                elif collision(LS12,LS8):
                     Reversecall(LS12)
                elif collision(LS12,LS9):
                     Reversecall(LS12)
                elif collision(LS12,LS10):
                     Reversecall(LS12)
                elif collision(LS12,LS11):
                     Reversecall(LS12)
                elif collision(LS12,LS13):
                     Reversecall(LS12)
                elif collision(LS12,box):
                     Reversecall(LS12)

            elif collision(taker,LS13):
                Call(LS13)
                bgm.play()
                if collision(LS13,LS):
                     Reversecall(LS13)
                elif collision(LS13,LS1):
                     Reversecall(LS13)
                elif collision(LS13,LS2):
                     Reversecall(LS13)
                elif collision(LS13,LS3):
                     Reversecall(LS13)
                elif collision(LS13,LS4):
                     Reversecall(LS13)
                elif collision(LS13,LS5):
                     Reversecall(LS13)
                elif collision(LS13,LS6):
                     Reversecall(LS13)
                elif collision(LS13,LS7):
                     Reversecall(LS13)
                elif collision(LS13,LS8):
                     Reversecall(LS13)
                elif collision(LS13,LS9):
                     Reversecall(LS13)
                elif collision(LS13,LS10):
                     Reversecall(LS13)
                elif collision(LS13,LS12):
                     Reversecall(LS13)
                elif collision(LS13,LS11):
                     Reversecall(LS13)
                elif collision(LS13,box):
                     Reversecall(LS13)
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
