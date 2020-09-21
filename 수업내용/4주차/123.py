from pico2d import *

os.chdir('C:\\Users\\op389\\OneDrive\\바탕 화면\\파이썬\\2017182044-2D-02\\수업내용\\3주차')

KPU_HEIGHT, KPU_WIDTH = 1024,1280

def handle_events():
    global running
    global x,y
    events=get_events()
    for e in events:
        if e.type==SDL_QUIT:
            running=False
        elif e.type==SDL_MOUSEMOTION:
            x,y=e.x, KPU_HEIGHT -1 -e.y
        elif e.type==SDL_KEYDOWN and e.key==SDLK_ESCAPE:
            running = False
           

open_canvas(KPU_WIDTH,KPU_HEIGHT)
grass=load_image('grass.png')
character=load_image('run_animation.png')

running = True
x,y = KPU_WIDTH//2, KPU_HEIGHT // 2
frame=0


while running:
    clear_canvas()
    grass.draw(KPU_WIDTH//2,KPU_HEIGHT // 2)
    character.clip_draw(frame*100,0,100,100,x,y)
    update_canvas()
    handle_events()
    frame=(frame+1)%8
   
    delay(0.01)
