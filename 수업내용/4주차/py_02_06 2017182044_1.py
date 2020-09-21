
from pico2d import *
from helper import *

WIDTH,HEIGHT =800,600

def handle_events():
    global running
    global dx,x,y,target
    global sp,temp
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False
        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running = False 
        elif event.type ==SDL_MOUSEBUTTONDOWN:
            a.append((event.x,HEIGHT-1-event.y))
            if delta((x,y),a[0],sp)==0:
                a.pop(0)
            sp += 1

open_canvas(WIDTH,HEIGHT)

gra =load_image('res/grass.png')
cha =load_image('res/run_animation.png')

x=WIDTH//2
y=HEIGHT//2

target=x,y
a=[target]
sp=1
done=True
fidx=0
running =True

while running:
    clear_canvas()
    gra.draw(WIDTH//2,HEIGHT//2)
    (x,y),done=move_toward((x,y),delta((x,y),a[0],sp),a[0])
    if done == True and len(a) == 1:
        speed =1
    if len(a) !=1 and delta((x,y),a[0],sp) == (0,0):
        a.pop(0)
    print(a[0])
    cha.clip_draw(fidx*100,0,100,100,x,y)
    update_canvas()

    handle_events()
    fidx =(fidx + 1)%8
    delay(0.01)
close_canvas()